from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver\\chromedriver.exe")

def parser_url(url: str):
    try:
        browser = webdriver.Chrome(service=service)
        browser.implicitly_wait(5)
        browser.get(url)
        html = browser.page_source
        print(type(html))
    except Exception as e:
        print(e)
    finally:
        browser.quit()

    return html
