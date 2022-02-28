from fastapi import FastAPI, Form, UploadFile, File
from fastapi.responses import FileResponse
from youtube_firefox import get_channel_detail
app = FastAPI()

@app.get("/info")
def _info(keyword):
    return get_channel_detail(keyword)