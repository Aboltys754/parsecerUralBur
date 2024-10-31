import urllib.parse
from fastapi import FastAPI
import urllib
from parser import parser_url


app = FastAPI()



@app.get("/get_url/") 
async def root(url: str) :
	original_url = urllib.parse.unquote(url)
	html = parser_url(original_url)
	print(html)
	return {"html": html}
