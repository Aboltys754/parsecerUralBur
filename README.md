# parsecerUralBur
python 3.12

Для запуска:
1. py -3.12 -m venv venv
2. venv\Scripts\Activate.ps1
3. python.exe -m pip install --upgrade pip
4. pip install -r requirements.txt
5. uvicorn main:app --reload

- ссылка для запросов http://127.0.0.1:8000/url_to_html/
- ссылка надоку http://127.0.0.1:8000/docs
- ссылка на CromeDriver https://googlechromelabs.github.io/chrome-for-testing/#stable


unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver

apk add chromium