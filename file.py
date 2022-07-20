from pytube import YouTube


SAVE_PATH="D:/donwloaded_videos"


youtube_url="https://www.youtube.com/watch?v=JGulAZnnTKA&list=RDMM&index=15"

yt=YouTube(youtube_url)

class download_vidoes:
    def __init__(self,youtubelink,savepath,resolution):
        self.youtube_url= youtubelink
        self.savepath=savepath
        self.res=resolution
        self.yt=YouTube(youtube_url)

    def get_title(self):
        return self.yt.title
    # def donwload_video(self):
    #     self.res
