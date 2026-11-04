from pathlib import Path
import base64
root=Path(__file__).parent
css=(root/'style.css').read_text()
js=(root/'vendor/fflate.js').read_text()+'\n'+(root/'excel.js').read_text()+'\n'+(root/'app.js').read_text()
emblem=base64.b64encode((root/'emblem.png').read_bytes()).decode()
html='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><title>明·成长｜2604成绩管理</title><meta name="description" content="适合初一的成绩记录与分析，本地浏览器保存，支持备份恢复"><style>'''+css+'''</style></head><body><div id="app"></div><script>const EMBLEM="'''+emblem+'''";\n'''+js+'''</script></body></html>'''
(root/'index.html').write_text(html)
print(root/'index.html',len(html),'bytes')
