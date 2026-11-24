from playwright.sync_api import sync_playwright
import json
ROOT=__import__('pathlib').Path(__file__).parents[1] / 'site'
CSS=(ROOT/'styles.css').read_text()
APP=(ROOT/'app.js').read_text()
DATA=(ROOT/'data/guidance.json').read_text()
def load(page):
    page.set_content('<!doctype html><html><head><meta charset=\"utf-8\"></head><body><div id=\"app\"></div></body></html>')
    page.add_style_tag(content=CSS)
    page.evaluate('''(()=>{const mk=()=>{const m=new Map();return{getItem:k=>m.get(k)||null,setItem:(k,v)=>m.set(k,String(v)),removeItem:k=>m.delete(k),clear:()=>m.clear()}};Object.defineProperty(window,'localStorage',{configurable:true,value:mk()});Object.defineProperty(window,'sessionStorage',{configurable:true,value:mk()});window.history.pushState=function(){};window.history.replaceState=function(){};})()''')
    page.evaluate('window.fetch=async ()=>new Response('+json.dumps(DATA)+',{status:200,headers:{\"content-type\":\"application/json\"}})')
    page.add_script_tag(content=APP)
    page.wait_for_selector('.landing-card')
checks=[]
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page(viewport={'width':1440,'height':950},device_scale_factor=1)
 errors=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 load(page)
 page.wait_for_selector('.landing-card')
 assert page.get_by_role('heading',name='Apprentices',exact=True).count()==1
 checks.append('Landing two audiences: PASS')
 page.locator('[data-audience="apprentice"]').click()
 page.wait_for_selector('#standard-select')
 assert 'Quantity Surveying & Project Management' in page.locator('#pathway-select').input_value() or page.locator('#pathway-select').input_value()=='quantity-surveying-project-management'
 paths=page.locator('#pathway-select option').all_text_contents()
 assert len(paths)==3,paths
 checks.append('Three ST0331 occupational options/default QS: PASS')
 assert page.locator('#apc-pathway-select').count()==0
 page.get_by_role('button',name='View RICS APC pathways (optional)').click()
 assert page.locator('#apc-pathway-select').count()==1
 assert page.locator('#apc-pathway-select option').count()==4
 page.locator('#apc-pathway-select').select_option('project-management')
 assert page.locator('#pathway-select').input_value()=='quantity-surveying-project-management'
 checks.append('Four optional APC choices independently selected: PASS')
 page.get_by_role('button',name='1-page summary').first.click()
 assert page.get_by_role('heading',name='Gateway & EPA | One-page summary').count()==1
 assert 'Quantity Surveying & Project Management' in page.locator('.print-head').inner_text()
 page.get_by_role('button',name='Back to guidance').click()
 page.wait_for_selector('#apc-pathway-select')
 checks.append('One-page summary and return context: PASS')
 page.get_by_role('button',name='Compare standards').first.click()
 assert page.locator('.matrix tbody tr').count()==7
 page.locator('[data-level="4"]').click()
 assert page.locator('.matrix tbody tr').count()==3
 page.locator('[data-level="all"]').click()
 page.get_by_role('button',name='Return to guidance').click()
 checks.append('Seven-standard comparison/filter/return: PASS')
 page.locator('[data-section="gateway"]').first.click()
 page.wait_for_selector('.requirement')
 assert page.locator('.requirement').count()==7
 page.locator('[data-requirement]').first.select_option(label='Prepared (self-check)')
 page.locator('[data-view="summary"]').first.click()
 page.get_by_role('button',name='Back to guidance').click()
 assert page.locator('[data-requirement]').first.input_value()=='Prepared (self-check)'
 checks.append('Gateway checklist retained through print navigation: PASS')
 page.locator('#standard-select').select_option('ST0047')
 assert page.locator('#pathway-select').count()==0
 assert 'CIOB' in page.locator('.selection-meta').inner_text()
 checks.append('CIOB standard selection: PASS')
 page.locator('#role-switch').select_option('staff')
 page.get_by_role('button',name='Questions & support').first.click()
 assert page.get_by_role('heading',name='Staff & WPLA practice questions').count()==1
 checks.append('Staff view and role-specific FAQs: PASS')
 # Legacy URL mapping is covered by the Floot source tests, as the test browser blocks localhost navigations.
 mobile=b.new_page(viewport={'width':393,'height':852},device_scale_factor=1)
 load(mobile)
 mobile.locator('[data-audience=apprentice]').click()
 mobile.locator('#pathway-select').select_option('property')
 mobile.locator('[data-section=dates]').first.click()
 mobile.wait_for_selector('#rics-session')
 assert 'Land and Property' in mobile.locator('#rics-session').locator('option:checked').inner_text()
 checks.append('Mobile/property RICS session default: PASS')
 mobile.screenshot(path='/mnt/data/CUBE_Gateway_EPA_GitHub_v0.5.2/tests/mobile-preview.png',full_page=True)
 page.locator('#standard-select').select_option('ST0331')
 page.locator('#role-switch').select_option('apprentice')
 page.locator('[data-section=overview]').first.click()
 page.wait_for_selector('.overview-hero')
 page.screenshot(path='/mnt/data/CUBE_Gateway_EPA_GitHub_v0.5.2/tests/desktop-preview.png',full_page=True)
 if errors: raise AssertionError('page JS errors: '+repr(errors))
 b.close()
print('\n'.join(checks))
open('/mnt/data/CUBE_Gateway_EPA_GitHub_v0.5.2/tests/smoke-results.json','w').write(json.dumps({'checks':checks,'passed':len(checks),'failed':0},indent=2))
