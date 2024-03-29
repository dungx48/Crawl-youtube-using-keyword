from fastapi import FastAPI, Form, UploadFile, File
from fastapi.responses import FileResponse
from crawl_youtube import get_channel_detail
from download_video import download
app = FastAPI()

@app.get("/get_info")
def _info(keyword):
    return get_channel_detail(keyword)

@app.get("/download")
def _download(keyword):
    return download(keyword)