#!/usr/bin/env python3
"""Build the README collection from curated cases and complete locale copy."""
import argparse,json,pathlib,urllib.parse

ROOT=pathlib.Path(__file__).resolve().parents[1]
LANGS=[('en','English','README.md'),('es','Español','README_es.md'),('pt','Português','README_pt.md'),('ja','日本語','README_ja.md'),('ko','한국어','README_ko.md'),('de','Deutsch','README_de.md'),('fr','Français','README_fr.md'),('tr','Türkçe','README_tr.md'),('zh-TW','繁體中文','README_zh-TW.md'),('zh-CN','简体中文','README_zh-CN.md'),('ru','Русский','README_ru.md')]
CATEGORIES=[('mechanical','⚙️'),('voxel','🏞️'),('svg','🎨'),('games','🎮'),('comparison','🔬')]
BADGES='\n'.join(f'[![{name}](https://img.shields.io/badge/{urllib.parse.quote(name)}-2563eb)]({filename})' for _,name,filename in LANGS)
LANDING='https://evolink.ai?utm_source=github&utm_medium=banner&utm_campaign=gemini-4-carbon-usecases&utm_content=readme-cover'
NAV={
 'en':('Community use cases','Guide and Use Cases','Guide and Prompts'),
 'es':('Casos de uso de la comunidad','Guía y casos de uso','Guía e instrucciones'),
 'pt':('Casos de uso da comunidade','Guia e casos de uso','Guia e instruções'),
 'ja':('コミュニティ活用事例','ガイドと活用事例','ガイドとプロンプト'),
 'ko':('커뮤니티 활용 사례','가이드와 활용 사례','가이드와 프롬프트'),
 'de':('Anwendungsfälle aus der Community','Leitfaden und Anwendungsfälle','Leitfaden und Prompts'),
 'fr':('Cas d’usage de la communauté','Guide et cas d’usage','Guide et instructions'),
 'tr':('Topluluk kullanım örnekleri','Rehber ve kullanım örnekleri','Rehber ve istemler'),
 'zh-TW':('社群使用案例','指南與使用案例','指南與提示詞'),
 'zh-CN':('社区使用案例','指南与使用案例','指南与提示词'),
 'ru':('Примеры использования сообщества','Руководство и примеры использования','Руководство и запросы'),
}

def render(data,locale):
    cases=data['cases'];translations=locale['cases'];g=locale['copy'];nav=NAV[locale['language']];banner=data.get('banner_url','assets/banner.svg')
    assert len(cases)==len(translations)==25
    chunks=[f'<div align="center">\n\n<a href="{LANDING}"><img src="{banner}" alt="Gemini 4 Carbon — {nav[0]}" width="760"></a>\n\n[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)\n\n{BADGES}\n\n</div>\n',f'## 🍌 {g["introduction"]}\n\n{g["intro"]}\n\n**{g["purpose"]}**\n',f'## 📊 {g["overview"]}\n\n{g["stats"]}\n\n> [!NOTE]\n> {g["evidence"]}\n',f'<a id="quick-start"></a>\n## ⚡ {g["quick_start"]}\n\n{g["steps"]}\n',f'## 📑 {g["menu"]}\n\n| {g["case"]} | {g["category"]} | {g["type"]} |\n|---|---|---|']
    for c,t in zip(cases,translations):chunks.append(f'| [{c["number"]}. {t[0]}](#case-{c["number"]}) | {g["categories"][c["category"]]} | {c["type"]} |')
    chunks.append('')
    for category,emoji in CATEGORIES:
        chunks.append(f'## {emoji} {g["categories"][category]}\n')
        for c,t in zip(cases,translations):
            if c['category']!=category:continue
            chunks.append(f'<a id="case-{c["number"]}"></a>\n### {g["case"]} {c["number"]}: [{t[0]}]({c["source_url"]}) ({g["by"]} [@{c["author_handle"]}]({c["author_url"]}))\n\n**{t[1]}**\n\n{t[2]}\n')
            for related in c.get('related_sources',[]):
                chunks.append(f'([@{related["author_handle"]}]({related["source_url"]}))\n')
            cells=[]
            for index,m in enumerate(c['media'],1):
                url=m.get('playable_url',m.get('image_url',m['source_media_url']));poster=m.get('poster_url',m['poster_path'])
                label=g['comparison_video'] if m.get('role')=='model-comparison' else (g['video'] if m['type']=='video' else g['image'])
                cells.append(f'<td align="center"><a href="{url}"><img src="{poster}" alt="{t[0]} — {index}" width="560"></a><br>{label}</td>')
            chunks.append('<table><tr>'+''.join(cells)+'</tr></table>\n')
            chunks.append(f'{g["type"]}: {c["type"]} | {g["date"]}: {c["date"]}\n\n---\n')
    chunks.append(f'<a id="related-repositories"></a>\n## {g["related"]}\n\n- [Gemini 3.6 Flash — {nav[1]}](https://github.com/Evolink-AI/awesome-gemini-3.6-flash-guide-and-use-cases)\n- [Gemini Omni — {nav[2]}](https://github.com/Evolink-AI/awesome-gemini-omni-guide-api-and-prompt)\n')
    authors=list(dict.fromkeys((c['author_handle'],c['author_url']) for c in cases))
    chunks.append(f'<a id="acknowledge"></a>\n## 🙏 {g["acknowledge"]}\n\n{g["thanks"]}\n\n'+', '.join(f'[@{handle}]({url})' for handle,url in authors)+f'\n\n{g["corrections"]}\n')
    return '\n'.join(chunks).rstrip()+'\n'

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--english-only',action='store_true');parser.add_argument('--check',action='store_true');args=parser.parse_args()
    data=json.loads((ROOT/'data/gemini-4-carbon-usecase-curated.json').read_text());fail=[]
    for code,_,filename in LANGS:
        if args.english_only and code!='en':continue
        locale=json.loads((ROOT/f'data/locales/{code}.json').read_text());out=render(data,locale);target=ROOT/filename
        if args.check:
            if not target.exists() or target.read_text()!=out:fail.append(filename)
        else:target.write_text(out)
    if fail:raise SystemExit('README drift: '+', '.join(fail))
    print('README generation check passed' if args.check else 'README files generated')
if __name__=='__main__':main()
