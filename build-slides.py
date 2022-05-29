import os
import time
import json
from os import path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

dirname = path.abspath(path.dirname(__file__))
if not os.path.exists(path.join(dirname, 'dist')):
    os.mkdir(path.join(dirname, 'dist'))

chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=2')
chrome_options.add_argument('--window-size=1920x1024')

print_settings = {
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "local",
        "account": "",
    }],
    "selectedDestinationId": "Save as PDF",
    "version": 2,
    "isHeaderFooterEnabled": False,
    "isCssBackgroundEnabled": True,
    "customMargins": {
        "margin-top": "0cm",
        "margin-bottom": "0cm",
        "margin-left": "0cm",
        "margin-right": "0cm"
    },
    "marginsType": 2,
    # "scaling": 100,
    # "scalingType": 3,
    # "scalingTypePdf": 3,
}
prefs = {
    'printing.print_preview_sticky_settings.appState': json.dumps(print_settings),
    'savefile.default_directory': path.join(dirname, 'dist'),
}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')
chrome_options.add_argument('--enable-print-browser')

driver = webdriver.Chrome(chrome_options=chrome_options, )
driver.get("file://" + path.join(dirname, 'slides.md.html'))

time.sleep(5)

driver.save_screenshot('dist/screenshot-slides.png')
driver.execute_script('window.print();')

driver.quit()