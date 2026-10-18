import os
from pathlib import Path
R=Path(os.environ.get('COURSE_ASR_RUN_DIR', str(Path(__file__).resolve().parent/'asr_run'))); R.mkdir(parents=True,exist_ok=True); B=R.parent
os.environ['HF_HOME']=str(B/'hf_cache')
os.environ['TOKENIZERS_PARALLELISM']='false'
import json,time,datetime,hashlib,subprocess,fcntl,collections
lock=open(R/'runner.lock','a+');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(p,d):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(d,ensure_ascii=False,indent=2));t.replace(p)
def log(d):print(json.dumps({'at':now(),**d},ensure_ascii=False),flush=True)
import torch,soundfile as sf,transformers
from transformers import AutoProcessor,AutoModelForMultimodalLM
torch.set_num_threads(6)
MID='Qwen/Qwen3-ASR-0.6B-hf'; REV='7f1569a48a89f3e3f4dc3a5c9d28bddd903bc76c'
log({'event':'loading','model':MID,'revision':REV})
p=AutoProcessor.from_pretrained(MID,revision=REV)
m=AutoModelForMultimodalLM.from_pretrained(MID,revision=REV,dtype=torch.bfloat16).to('cpu').eval()
prov={'model':MID,'revision':REV,'torch':torch.__version__,'transformers':transformers.__version__,'dtype':'bfloat16','device':'cpu','threads':6,'window':120,'overlap':10,'max_new_tokens':1024,'prompt':None,'language':'auto','generation':'greedy','rerun_date':now(),'note':'Recovery rerun in new runtime, not byte-identical replay of lost outputs.'}
save(R/'provenance.json',prov)
rows=json.loads((B/'mobile-sensor-network-course/source_manifest.json').read_text())['recordings'][8:]
for row in rows:
 rid=row['recording_id'];out=R/'results'/rid
 if (out/'recording.json').exists():continue
 audio=B/'course_audio'/f'{rid}.m4a'
 while not audio.exists(): save(R/'progress.json',{'status':'waiting_audio','recording_id':rid,'at':now()});time.sleep(15)
 wav=R/f'{rid}.wav'
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(audio),'-ac','1','-ar','16000',str(wav)],check=True)
 y,sr=sf.read(wav,dtype='float32');duration=len(y)/sr
 ah=hashlib.sha256(audio.read_bytes()).hexdigest();chunks=[]
 def infer(start,end,path):
  if path.exists():return json.loads(path.read_text())
  t=time.monotonic();inputs=p.apply_transcription_request(audio=y[int(start*sr):int(end*sr)],sampling_rate=sr).to(m.device,m.dtype)
  with torch.inference_mode():ids=m.generate(**inputs,max_new_tokens=1024,do_sample=False)
  g=ids[:,inputs['input_ids'].shape[1]:];raw=p.decode(g)[0];text=p.decode(g,return_format='transcription_only')[0]
  tok=g[0].tolist();words=text.lower().split();grams=collections.Counter(tuple(words[i:i+8]) for i in range(max(0,len(words)-7)));flags=[]
  if not text.strip():flags.append('empty_output')
  if len(tok)>=1024:flags.append('generation_cap')
  if grams and max(grams.values())>=3:flags.append('repetition')
  d={'start_seconds':start,'end_seconds':end,'text':text,'raw_decoded':raw,'generated_tokens':len(tok),'last_token':tok[-1] if tok else None,'flags':flags,'inference_seconds':time.monotonic()-t,'at':now(),'source_sha256':ah}
  save(path,d);return d
 for i,start in enumerate(range(0,len(y),110*sr)):
  s=start/sr;e=min(duration,s+120);c=infer(s,e,out/'raw_chunks'/f'chunk_{i:05d}.json');chunks.append(c)
  if any(f in c['flags'] for f in ['generation_cap','repetition']):
   mid=(s+e)/2;infer(s,min(e,mid+5),out/'split_checks'/f'{i:05d}_a.json');infer(max(s,mid-5),e,out/'split_checks'/f'{i:05d}_b.json')
  save(R/'progress.json',{'status':'running','recording_id':rid,'completed_chunks':i+1,'covered_until_seconds':e,'duration_seconds':duration,'at':now()});log({'event':'chunk_complete','id':rid,'index':i,'end':e,'flags':c['flags']})
  if e>=duration:break
 tail=infer(max(0,duration-90),duration,out/'tail_verification.json')
 save(out/'recording.json',{'id':rid,'status':'complete','duration':duration,'audio_sha256':ah,'provenance':prov,'segments':chunks,'tail':tail,'coverage_start':0,'coverage_end':duration,'sample_count':len(y),'sample_rate':sr,'note':'All samples processed; text correctness requires editorial review.'})
 log({'event':'recording_complete','id':rid,'chunks':len(chunks),'duration':duration})
 wav.unlink()
save(R/'progress.json',{'status':'queue_complete','completed':len(rows),'at':now()});log({'event':'queue_complete','completed':len(rows)})
