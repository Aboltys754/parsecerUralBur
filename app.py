import urllib.parse
from fastapi import FastAPI, Response
import urllib
from parser import parser_url


app = FastAPI()



@app.get("/get_url/") 
async def root(url: str) :
	try:
		original_url = urllib.parse.unquote(url)
		html = parser_url(original_url)
		return Response(content=html, media_type="text/plain")
	except Exception as e:
		return Response(content=e, media_type="text/plain")
