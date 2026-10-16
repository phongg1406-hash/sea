from playwright.sync_api import sync_playwright
from pathlib import Path
root=Path(__file__).resolve().parent.parent
html=(root/'index.html').read_text();css=(root/'styles.css').read_text();js=(root/'app.js').read_text()
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
    failures=[]
    for w,h in [(360,740),(390,844),(768,950),(800,1000),(801,950),(1024,768),(1440,900),(1920,1080)]:
        page=b.new_page(viewport={'width':w,'height':h},device_scale_factor=1)
        errs=[];page.on('pageerror',lambda e:errs.append(str(e)))
        page.set_default_timeout(3000)
        page.set_content(html,wait_until='domcontentloaded');page.add_style_tag(content=css);page.add_script_tag(content=js)
        page.wait_for_timeout(80)
        d=page.evaluate('''() => ({scrollWidth:document.documentElement.scrollWidth,screen:innerWidth, scene:window.__sunlitDebug.state.active, mobile:window.__sunlitDebug.state.mobile, interactive:document.querySelectorAll('button').length, scrollHeight:document.documentElement.scrollHeight})''')
        if errs or d['scrollWidth']>w+1:failures.append([w,h,errs,d])
        print(f'{w}x{h}: mobile={d["mobile"]}, overflow={d["scrollWidth"]-w}, buttons={d["interactive"]}')
        if w==1440:
            world=page.locator('#world').bounding_box()
            page.mouse.move(1300,470)
            page.mouse.down();page.mouse.move(900,600,steps=8);page.mouse.up()
            moved=page.locator('#world').bounding_box()
            print(' drag pan delta',round(moved['x']-world['x']),round(moved['y']-world['y']))
            if abs(moved['x']-world['x'])<100:failures.append('drag did not pan')
            page.locator('.map-panel [data-goto="archive"]').click()
            page.wait_for_timeout(660)
            print(' archive reached',page.locator('#scene-label').inner_text())
            page.locator('[data-view="list"]').click(force=True)
            if 'list-view' not in page.locator('#archive-items').get_attribute('class'):failures.append('list view toggle')
            page.keyboard.press('Escape')
        page.close()
    print('FAILURES:',failures)
    b.close()
    if failures:raise SystemExit(1)
