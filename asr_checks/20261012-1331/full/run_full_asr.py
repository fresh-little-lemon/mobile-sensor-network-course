import concurrent.futures as cf,os,json,time,hashlib,pathlib,subprocess,wave,datetime,dataclasses,math,importlib.metadata,traceback
import numpy as np
from faster_whisper import WhisperModel
ROOT=pathlib.Path(__file__).parent
SOURCE=ROOT.parent/'asr-0940'/'20261012-1331.m4a'
MODEL_PATH=(ROOT.parent/'asr-0940'/'medium.en-model-path.txt').read_text().strip()
MODEL_META=json.loads((ROOT.parent/'asr-0940'/'medium.en-model-metadata.json').read_text())
DURATION=5622.281333;CORE=180;CONTEXT=15
SOURCE_SHA='b710201745efeb5071757d4e3b086ce30937f038bbe1bbe6ae18bd74aa7239ff'
PARAMS={'language':'en','beam_size':5,'temperature':0.0,'initial_prompt':None,'condition_on_previous_text':False,'vad_filter':False,'word_timestamps':True}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def atomjson(path,x):
 tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(x,ensure_ascii=False,indent=2));tmp.replace(path)
def init():
 global MODEL
 MODEL=WhisperModel(MODEL_PATH,device='cpu',compute_type='int8',cpu_threads=4,num_workers=1,local_files_only=True)
def tc(t):return f'{int(t//3600):02}:{int(t%3600//60):02}:{t%60:06.3f}'
def run(chunk):
 label=chunk['label'];prefix=ROOT/label;raw=ROOT/(label+'.raw.json');clock=time.perf_counter()
 if raw.exists():
  old=json.loads(raw.read_text());return {'label':label,'status':'reused_complete','raw_sha256':sha(raw),'elapsed_seconds':old['run_metadata']['elapsed_seconds'],'segments':len(old['segments'])}
 try:
  wavp=ROOT/(label+'.wav')
  if not wavp.exists():
   subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-ss',str(chunk['window_start_seconds']),'-i',str(SOURCE),'-t',str(chunk['window_end_seconds']-chunk['window_start_seconds']),'-ac','1','-ar','16000','-c:a','pcm_s16le',str(wavp)],check=True)
  with wave.open(str(wavp),'rb') as wav:
   assert wav.getframerate()==16000 and wav.getnchannels()==1 and wav.getsampwidth()==2
   pcm=np.frombuffer(wav.readframes(wav.getnframes()),dtype=np.int16).astype(np.float32)/32768.0
  segs,info=MODEL.transcribe(pcm,**PARAMS);results=[]
  with (ROOT/(label+'.raw.jsonl')).open('w') as f:
   for s in segs:
    d=dataclasses.asdict(s);results.append(d);f.write(json.dumps(d,ensure_ascii=False)+'\n');f.flush()
  elapsed=time.perf_counter()-clock
  result={'run_metadata':{'chunk':chunk,'model':MODEL_META,'source_audio_filename':SOURCE.name,'source_audio_sha256':SOURCE_SHA,'audio_window_filename':wavp.name,'audio_window_sha256':sha(wavp),'absolute_offset_seconds':chunk['window_start_seconds'],'parameters':PARAMS,'runtime':{'faster_whisper':importlib.metadata.version('faster-whisper'),'ctranslate2':importlib.metadata.version('ctranslate2'),'device':'cpu','compute_type':'int8','cpu_threads':4},'elapsed_seconds':elapsed,'machine_utc_completed':datetime.datetime.now(datetime.timezone.utc).isoformat(),'verification':'Raw ASR output. Not human-listened. Context overlap retained intact. Not a corrected transcript.'},'transcription_info':dataclasses.asdict(info),'segments':results}
  atomjson(raw,result)
  offset=chunk['window_start_seconds'];txt='\n'.join(f"[{tc(s['start']+offset)} --> {tc(s['end']+offset)}] {s['text'].strip()}" for s in results)+'\n'
  (ROOT/(label+'.absolute.txt')).write_text(txt)
  (ROOT/(label+'.sha256')).write_text(sha(raw)+'  '+raw.name+'\n'+sha(ROOT/(label+'.raw.jsonl'))+'  '+label+'.raw.jsonl\n'+sha(ROOT/(label+'.absolute.txt'))+'  '+label+'.absolute.txt\n')
  return {'label':label,'status':'complete','raw_sha256':sha(raw),'elapsed_seconds':elapsed,'segments':len(results),'window_seconds':chunk['window_end_seconds']-chunk['window_start_seconds']}
 except Exception as e:
  err={'label':label,'status':'failed','error':str(e),'traceback':traceback.format_exc()};atomjson(ROOT/(label+'.error.json'),err);return err

def main():
 chunks=[]
 for i in range(math.ceil(DURATION/CORE)):
  a=i*CORE;b=min((i+1)*CORE,DURATION)
  chunks.append({'index':i+1,'label':f'chunk-{i+1:03}','core_start_seconds':a,'core_end_seconds':b,'window_start_seconds':max(0,a-CONTEXT),'window_end_seconds':min(DURATION,b+CONTEXT),'overlap_policy':'15 seconds of context on each available side. Full raw outputs retained; no automatic deduplication.'})
 manifest={'course':'20261012-1331','duration_seconds':DURATION,'source_audio_sha256':SOURCE_SHA,'model':MODEL_META,'parameters':PARAMS,'core_seconds':CORE,'context_each_side_seconds':CONTEXT,'parallel_workers':2,'cpu_threads_per_worker':4,'chunks':chunks,'audio_not_in_text_publish_batch':True,'raw_first_no_correction':True}
 atomjson(ROOT/'run-manifest.json',manifest)
 start=time.perf_counter();completed=[]
 with cf.ProcessPoolExecutor(max_workers=2,initializer=init) as pool:
  futures={pool.submit(run,c):c for c in chunks}
  for f in cf.as_completed(futures):
   r=f.result();completed.append(r);elapsed=time.perf_counter()-start
   status={'completed_count':sum(c['status'] in ['complete','reused_complete'] for c in completed),'failed_count':sum(c['status']=='failed' for c in completed),'total_chunks':len(chunks),'elapsed_seconds':elapsed,'results':sorted(completed,key=lambda x:x['label'])}
   if status['completed_count']:status['estimated_remaining_seconds_linear']=elapsed/status['completed_count']*(len(chunks)-len(completed))
   atomjson(ROOT/'progress.json',status)
   print(json.dumps({'event':'chunk_done','result':r,'progress':{k:v for k,v in status.items() if k!='results'}},ensure_ascii=False),flush=True)
 print('ALL_JOBS_FINISHED',flush=True)
if __name__=='__main__':main()
