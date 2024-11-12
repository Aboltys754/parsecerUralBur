import urllib.parse
from fastapi import FastAPI, Response
import urllib
from parcer import parser_url


app = FastAPI()


# получает url отдает голый html страницы
@app.get("/url_to_html/") 
async def root(url: str):
	print(url)
	try:
		original_url = urllib.parse.unquote(url)
		html = parser_url(original_url)
		return Response(content=html, media_type="text/plain")
	except Exception as e:
		return Response(content=e, media_type="text/plain")
