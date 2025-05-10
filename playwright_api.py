from fastapi import FastAPI
from pydantic import BaseModel
from playwright_loader import PlaywrightLoader, html_to_markdown

app = FastAPI(docs_url="/swagger", redoc_url="/redoc", openapi_url="/openapi.json")


class UrlRequest(BaseModel):
    url: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/fetch_markdown")
async def fetch_markdown(request: UrlRequest):
    loader = PlaywrightLoader()
    content = await loader.async_load(request.url)
    markdown = html_to_markdown(content)
    return {"markdown": markdown}


@app.post("/fetch_html")
async def fetch_html(request: UrlRequest):
    loader = PlaywrightLoader()
    content = await loader.async_load(request.url)
    return {"html": content}
