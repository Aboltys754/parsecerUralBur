import urllib.parse
from fastapi import FastAPI, Response
import urllib
from parcer import parser_url
import redis


app = FastAPI()


# получает url отдает голый html страницы


@app.get("/url_to_html/")
async def root(url: str):
    try:
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        original_url = urllib.parse.unquote(url)
        print(original_url)
        if r.get(original_url):
            print("есть")
            html = r.get(original_url)
            return Response(content=html, media_type="text/plain")
        else:
            print("нет")
            html = parser_url(original_url)
            r.set(original_url, html)
            return Response(content=html, media_type="text/plain")
    except Exception as e:
        print(e)
        return Response(content=f"{e}", media_type="text/plain")
    # try:
    #     original_url = urllib.parse.unquote(url)
    #     print(original_url)
    #     html = parser_url(original_url)
    #     return Response(content=html, media_type="text/plain")
    # except Exception as e:
    #     return Response(content=f"{e}", media_type="text/plain")
