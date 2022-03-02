from fastapi import FastAPI, Form, UploadFile, File
from fastapi.responses import FileResponse
from youtube_firefox import get_channel_detail
from download_video import download
app = FastAPI()

@app.get("/info")
def _info(keyword):
    return get_channel_detail(keyword)

@app.get("/download")
def _download(keyword):
    return download(keyword)