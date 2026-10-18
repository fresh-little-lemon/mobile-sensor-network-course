from pathlib import Path
import json,hashlib,re
p=Path(__file__).parent;manifest=json.loads((p/'run-manifest.json').read_text());results=[]
for c in manifest['chunks']:
 f=p/(c['label']+'.raw.json')
 if not f.exists():continue
 x=json.loads(f.read_text());dur=c['window_end_seconds']-c['window_start_seconds'];alerts=[];last=0
 for s in x['segments']:
  if s['start']<0 or s['end']>dur+1:alerts.append({'type':'segment_out_of_window','segment_id':s['id'],'start':s['start'],'end':s['end']})
  if s.get('no_speech_prob',0)>0.5:alerts.append({'type':'high_no_speech_score','segment_id':s['id'],'value':s['no_speech_prob']})
  for w in s.get('words',[]):
   a=w['start'];b=w['end'];t=w['word']
   if b<a or a<last-0.05:alerts.append({'type':'nonmonotonic_word','word':t,'start':a,'end':b,'previous_end':last})
   if b-a<=0.011:alerts.append({'type':'near_zero_duration','word':t,'start':a+c['window_start_seconds'],'end':b+c['window_start_seconds']})
   if b-a>2:alerts.append({'type':'long_word_duration','word':t,'start':a+c['window_start_seconds'],'end':b+c['window_start_seconds']})
   if w.get('probability',1)<0.45:alerts.append({'type':'low_decoder_score','word':t,'start':a+c['window_start_seconds'],'end':b+c['window_start_seconds'],'score':w.get('probability')})
   last=b
 rawhash=hashlib.sha256(f.read_bytes()).hexdigest();savedhash=(p/(c['label']+'.sha256')).read_text().split()[0]
 assert rawhash==savedhash,(f,rawhash,savedhash)
 results.append({'label':c['label'],'raw_json_sha256':rawhash,'verified_hash':True,'segment_count':len(x['segments']),'first_segment_start_absolute':x['segments'][0]['start']+c['window_start_seconds'] if x['segments'] else None,'last_segment_end_absolute':x['segments'][-1]['end']+c['window_start_seconds'] if x['segments'] else None,'alert_count':len(alerts),'alerts':alerts})
q={'note':'Heuristic review flags only; decoder scores are not calibrated correctness probabilities. Silence and stop-start speech can cause long/zero-duration anchors. No words changed.','completed_chunks':len(results),'planned_chunks':len(manifest['chunks']),'results':results}
(p/'integrity-review-flags.json').write_text(json.dumps(q,ensure_ascii=False,indent=2));print(json.dumps({'completed_chunks':len(results),'flag_counts':{r['label']:r['alert_count'] for r in results}},ensure_ascii=False))
