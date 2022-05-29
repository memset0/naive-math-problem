import os
import time
import json
from os import path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

dirname = path.abspath(path.dirname(__file__))

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=2')
chrome_options.add_argument('--window-size=1920x1024')

print_settings = {
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "local",
        "account": "",
    }],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}
prefs = {
    'printing.print_preview_sticky_settings.appState': json.dumps(print_settings),
    'savefile.default_directory': path.join(dirname, 'dist'),
}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')

driver = webdriver.Chrome(
    chrome_options=chrome_options,
)

def convertToPdf(source, delay):
    driver.get("file://" + path.join(dirname, source))
    
    # driver.implicitly_wait(10)
    # driver.find_element_by_id("md")
    time.sleep(delay)
    
    # driver.save_screenshot('test.png')
    driver.execute_script('window.print();')


if os.path.exists(path.join(dirname, 'dist')):
    for filename in os.listdir(path.join(dirname, 'dist')):
        os.remove(path.join(dirname, 'dist', filename))
    os.removedirs(path.join(dirname, 'dist'))
os.mkdir(path.join(dirname, 'dist'))

convertToPdf('slides.md.html', 3)
convertToPdf('latex.md.html', 5)

print(os.listdir(path.join(dirname, 'dist')))