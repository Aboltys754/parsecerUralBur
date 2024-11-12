from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import pathlib

path_app = os.getcwd()
path_chrome = os.path.join(path_app, 'chrome-linux64', 'chrome')
path_chromedriver = os.path.join(path_app, 'chromedriver-linux64', 'chromedriver')

service = Service(executable_path=path_chromedriver)
options = webdriver.ChromeOptions()
options.binary_location = path_chrome

def parser_url(url: str):
    print(url)
    try:
        browser = webdriver.Chrome(service=service, options=options)
        browser.implicitly_wait(5)
        browser.get(url)
        html = browser.page_source
        print(type(html))
    except Exception as e:
        print(e)
    finally:
        browser.quit()

    return html
