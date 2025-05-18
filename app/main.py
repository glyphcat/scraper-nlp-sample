from typing import Union

from fastapi import FastAPI
from scraper import Scraper


app = FastAPI()
scraper = Scraper()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# @app.get("/{word}")
# async def search_google(word):
#       return scraper.google_search(word)

@app.get("/scraping/execute")
async def execute():
      return await scraper.get_source_from_url('https://shin-kichi.com/category/spot/')