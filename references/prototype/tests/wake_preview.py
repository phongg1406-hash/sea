from playwright.sync_api import sync_playwright
from pathlib import Path
root=Path(__file__).resolve().parent.parent
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 pg=b.new_page(viewport={'width':1440,'height':900},device_scale_factor=1)
 pg.set_content((root/'index.html').read_text(),wait_until='domcontentloaded')
 pg.add_style_tag(content=(root/'styles.css').read_text())
 pg.add_script_tag(content=(root/'app.js').read_text())
 pg.mouse.move(365,515)
 for i in range(24):
  x=365+i*18
  y=515+39*__import__('math').sin(i/5)
  pg.mouse.move(x,y)
  pg.wait_for_timeout(24)
 pg.screenshot(path=str(root/'tests'/'water-wake-preview.png'))
 print('Wake screenshot; live points:',pg.evaluate('window.__sunlitDebug.getWakeCount()'))
 b.close()
