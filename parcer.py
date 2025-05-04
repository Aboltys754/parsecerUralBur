from selenium import webdriver
import time
import os

base_path = os.getcwd()
driver_path = os.path.join(base_path, "chromedriver", "chromedriver.exe")
сhrome_path = os.path.join(base_path, "chrome", "chrome.exe")


def parser_url(url_str: str):
    html = None
    service = webdriver.ChromeService(executable_path=driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-ssl-errors')
    # options.add_argument("headless")
    options.add_argument("disable-gpu")
    options.binary_location = сhrome_path

    browser = webdriver.Chrome(options=options, service=service)
    try:
        browser.implicitly_wait(5)
        browser.get(url_str)
        html = browser.page_source
        # time.sleep(20)
    except Exception as e:
        print(e)
    finally:
        browser.quit()
        return html
