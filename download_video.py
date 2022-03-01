from pytube import YouTube
import pafy
import sys


def progress(stream, chunk, bytes_remaining):
    filesize = stream.filesize
    current = ((filesize - bytes_remaining) / filesize)
    percent = ('{0:.1f}').format(current * 100)
    progress = int(50 * current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()


def download(url):
    ptvideo = YouTube(url, on_progress_callback=progress)
    my_streams = ptvideo.streams.order_by('resolution').desc()
    # print('All available streams')
    # for v in my_streams:
    #     print(v)

    mp4_stream = my_streams.filter(file_extension='mp4', progressive=True, resolution='720p')

    # print('720p mp4 stream')
    # for v in mp4_stream:
    #     print(v)

    print("Video is being downloaded as '%s.mp4'" % ptvideo.title)
    mp4_stream.first().download('Download/')


link = ["https://www.youtube.com/watch?v=xypzmu5mMPY", "https://www.youtube.com/watch?v=N4a9Db9_ijc"]
for i in link:
    download(i)
    print('\nDownload completed')
