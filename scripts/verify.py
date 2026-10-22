#!/usr/bin/env python3
"""Verify case identity, source coverage and generated locale parity."""
import hashlib,json,pathlib,re,subprocess,sys

ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from build_readmes import LANGS,render

data=json.loads((ROOT/'data/gemini-4-carbon-usecase-curated.json').read_text());cases=data['cases'];errors=[]
if [c['number'] for c in cases]!=list(range(1,len(cases)+1)):errors.append('Case numbers are not contiguous')
if data['case_count']!=len(cases):errors.append('Case count differs from dataset')
if len({c['source_id'] for c in cases})!=len(cases):errors.append('Duplicate primary source')
ids=[]
for c in cases:
 if c['type'] not in ['Demo','Tutorial','Evaluation','Integration','Benchmark','Limit']:errors.append(f"Unknown case type: {c['id']}")
 if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',c['date']):errors.append(f"Invalid date: {c['id']}")
 for m in c['media']:
  ids.append(m['id'])
  if not (ROOT/m['poster_path']).is_file():errors.append(f"Missing poster: {m['id']}")
  if m['type']=='video' and not m.get('playable_url','').startswith('https://'):errors.append(f"Missing video URL: {m['id']}")
if len(ids)!=len(set(ids)):errors.append('Retained media ids repeated across cases')
for code,_,filename in LANGS:
 p=ROOT/filename;locale=json.loads((ROOT/f'data/locales/{code}.json').read_text())
 if len(locale['cases'])!=len(cases) or any(len(row)!=3 or not all(row) for row in locale['cases']):errors.append(f'Incomplete locale {code}')
 if not p.is_file():errors.append(f'Missing {filename}');continue
 text=p.read_text()
 if text!=render(data,locale):errors.append(f'Generated content drift: {filename}')
 if re.findall(r'^<a id="case-(\d+)"></a>$',text,re.M)!=[str(i) for i in range(1,len(cases)+1)]:errors.append(f'Anchor order: {filename}')
 for c in cases:
  if f']({c["source_url"]})' not in text or f']({c["author_url"]})' not in text:errors.append(f'Source missing: {filename} {c["number"]}')
  if f'{c["type"]} | ' not in text or c['date'] not in text:errors.append(f'Metadata missing: {filename}')
 for m_id in ids:
  media=next(m for c in cases for m in c['media'] if m['id']==m_id)
  if media.get('poster_url',media['poster_path']) not in text:errors.append(f'Media missing: {filename} {m_id}')
  playback=media.get('playable_url',media.get('image_url',media['source_media_url']))
  if playback not in text:errors.append(f'Media destination missing: {filename} {m_id}')
 for c in cases:
  for source in c.get('related_sources',[]):
   if source['source_url'] not in text:errors.append(f'Related source missing: {filename} {c["number"]}')
 if re.search(r'^#{1,6} .*Prompt|^\*\*Prompt:',text,re.M):errors.append(f'Unexpected prompt section: {filename}')
 if re.search(r'\bTODO\b|\bTBD\b|translation pending|\{\{',text):errors.append(f'Placeholder: {filename}')
if errors:
 print('\n'.join(errors));raise SystemExit(1)
print(json.dumps({'status':'passed','cases':len(cases),'locales':len(LANGS),'retained_visuals':len(ids),'case_locale_pairs':len(cases)*len(LANGS)},indent=2))
