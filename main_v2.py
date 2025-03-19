import os
import sys

# Correctly add the directory containing libcairo-2.dll
os.environ['path'] += r';C:/Program Files/UniConvertor-2.0rc5/dlls'

import cairosvg

print("hello world")




from ui_UI_V4 import *
from Custom_Widgets.Widgets import *
from pytubefix import YouTube
from pytubefix import Playlist
import moviepy.editor as mp
from spotdl import Spotdl
import yt_dlp as youtube_dl
from PySide6.QtWidgets import QFileDialog
from pytubefix.cli import on_progress

#from spotify import *





def browse(self):
    file = QFileDialog.getExistingDirectory(self,"Path of the video","Downloads")
    return file


# YouTube download and merge
def download_and_merge(url, resu, self,output_dir):
    #self.ui.donwload.setText(QCoreApplication.translate("MainWindow", u"     Downloading", None))
        #self.ui.donwload.setStyleSheet(u"color: rgb(255, 255, 0);\n"
#"text-align:center;")
    yt = YouTube(url)
    print("done1")
    print(yt.streams)
        
    if resu == "Mp3(only-audio)":
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file = audio_stream.download(filename=f"{yt.title}.mp3", output_path=output_dir)
            #self.ui.ding.hide()
            #self.ui.donwload.show()
        print("Download and merge complete")
    else:
            # Get the resolution video stream without audio
        video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True, res=resu).desc().first()
            
            # Get the best audio stream
        audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
            
            # Download video and audio separately
        video_file = video_stream.download(filename="video.mp4", output_path=os.path.join(os.path.expanduser("~"), "Documents"))
        audio_file = audio_stream.download(filename="audio.mp4", output_path=os.path.join(os.path.expanduser("~"), "Documents"))
            
            # Load video and audio
        video_clip = mp.VideoFileClip(video_file)
        audio_clip = mp.AudioFileClip(audio_file)
            
            # Merge video and audio
        final_clip = video_clip.set_audio(audio_clip)
        final_clip.write_videofile(os.path.join(output_dir, f"{yt.title}.mp4"), codec="libx264", audio_codec="aac")
            #final_clip.write_videofile(f"{yt.title}.mp4", codec="libx264", audio_codec="aac")
        os.remove(video_file)
        os.remove(audio_file)
            
            #self.ui.ding.hide()
            #self.ui.donwload.show()
        print("Download and merge complete")


########playlist
def playlist_fun(url,resu,self,output_dir):
    p = Playlist(url)
    for video in p.video_urls:
        print(video)
        print(type(video))
        download_and_merge(video,resu,self,output_dir)

        
# Spotify download

def spotify_download(url, self,output_dir):

    obj = Spotdl(client_id="#",client_secret="#",no_cache=True)
    #self.ui.ding.show()
    print("test spotify-2")
    song_objs = obj.search([url])  # url
    print("test spotify-3")
    # Check if the directory exists
    if not os.path.exists(output_dir):
        print(f"Directory does not exist: {output_dir}")
        os.makedirs(output_dir)  # Optionally create it if it doesn't exist
    os.chdir(output_dir)
    print(song_objs)
    obj.download_songs(song_objs)
    
        #self.ui.ding.hide()
        #self.ui.donwload.show()
        
        

# Facebook download
def facebook_download(url, self,output_dir):
    #self.ui.ding.show()
    y = {"format": "best"}
    path = "C:/Users/Hazem Ahmed/Desktop/python"
    os.chdir(output_dir)
    with youtube_dl.YoutubeDL(y) as u:
        print("Downloading........." + url)
        u.download([url])
    
    #try:
    #    y = {"format": "best"}
    #    path = "C:/Users/Hazem Ahmed/Desktop/python"
    #    os.chdir(output_dir)
    #    with youtube_dl.YoutubeDL(y) as u:
    #        print("Downloading........." + url)
    #        u.download([url])
        #self.ui.ding.hide()
        #self.ui.donwload.show()
    #except Exception as e:
    #    print("Invalid link or selected resolution unavailable!")
        #self.ui.ding.hide()
        #self.ui.donwload.hide()
        #self.ui.error.show()
        
        

    print("Download completed!")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        if getattr(sys, 'frozen', False):
    # If running in a bundle
            bundle_dir = sys._MEIPASS
        else:
    # If running in normal python environment
            bundle_dir = os.path.abspath(os.path.dirname(__file__))

        style_path = os.path.join(bundle_dir, 'style.json')
        
        loadJsonStyle(self, self.ui)
        self.show()

        self.selected_url = None
        self.selected_resolution = None
        self.ui.donwload.hide()
        self.ui.ding.hide()
        self.ui.error.hide()
        self.ui.label_2.hide()
        self.ui.lineEdit.clear()

        # Initialize flags
        self.youtube_selected = True
        self.spotify_selected = False
        self.facebook_selected = False

        # Connect the buttons to their respective setup methods
        self.ui.y_btn.clicked.connect(self.setup_youtube_download)
        self.ui.t_btn.clicked.connect(self.setup_spotify_download)
        self.ui.i_btn.clicked.connect(self.setup_facebook_download)
        self.ui.info_btn.clicked.connect(self.show_info)

        # Connect the download button to download_video method
        self.ui.d_Btn.clicked.connect(self.download_video)

        
        


    def setup_youtube_download(self):
        self.youtube_selected = True
        self.spotify_selected = False
        self.facebook_selected = False
        self.ui.resolutionComboBox.show()
        self.ui.checkBox.show()
        self.ui.label_2.hide()
        self.ui.lineEdit.clear()
        self.ui.error.hide()
        self.ui.donwload.hide()

    def setup_spotify_download(self):
        self.youtube_selected = False
        self.spotify_selected = True
        self.facebook_selected = False
        self.ui.resolutionComboBox.hide()
        self.ui.checkBox.hide()
        self.ui.label_2.hide()
        self.ui.lineEdit.clear()
        self.ui.error.hide()
        self.ui.donwload.hide()

    def setup_facebook_download(self):
        self.youtube_selected = False
        self.spotify_selected = False
        self.facebook_selected = True
        self.ui.resolutionComboBox.hide()
        self.ui.checkBox.hide()
        self.ui.label_2.hide()
        self.ui.lineEdit.clear()
        self.ui.error.hide()
        self.ui.donwload.hide()

    def show_info(self):
        self.ui.label_2.show()

    def download_video(self):
        if self.youtube_selected:
            self.ui.error.hide()
            self.ui.ding.hide()
            self.ui.donwload.hide()
            self.download_video_y()
        elif self.spotify_selected:
            self.ui.error.hide()
            self.ui.ding.hide()
            self.ui.donwload.hide()
            self.download_video_s()
        elif self.facebook_selected:
            self.ui.error.hide()
            self.ui.ding.hide()
            self.ui.donwload.hide()
            self.download_video_f()

    def download_video_y(self):
        print("YouTube download started")
        self.selected_url = self.ui.lineEdit.text()
        self.selected_resolution = self.ui.resolutionComboBox.currentText()
        self.ui.donwload.hide()
        self.ui.error.hide()
        if self.selected_url and self.selected_resolution:
            print(f"Downloading video from URL: {self.selected_url} with resolution {self.selected_resolution}")
            
            file = QFileDialog.getExistingDirectory(parent=self,caption="Path of the video",dir=os.path.join(os.path.expanduser("~"), "Downloads"))###############################################
            print(file)
            try:
                self.ui.ding.show()
                QApplication.processEvents()
                if self.ui.checkBox.isChecked():
                    playlist_fun(self.selected_url, self.selected_resolution, self,file)
                else:
                    download_and_merge(self.selected_url, self.selected_resolution, self,file)
                self.ui.ding.hide()
                self.ui.donwload.show()
            except:
                self.ui.ding.hide()
                self.ui.donwload.hide()
                self.ui.error.show()
                print("An error occurred:")

        else:
            print("Error: URL or resolution are not selected")
            self.ui.ding.hide()
            self.ui.donwload.hide()
            self.ui.error.show()


    def download_video_s(self):
        print("Spotify download started")
        self.selected_url = self.ui.lineEdit.text()
        self.ui.donwload.hide()
        self.ui.error.hide()
        if self.selected_url:
            file = QFileDialog.getExistingDirectory(parent=self,caption="Path of the song",dir=os.path.join(os.path.expanduser("~"), "Downloads"))###############################################
            print(file)
            try:
                self.ui.ding.show()
                QApplication.processEvents()
                print("test-spotify")
                spotify_download(self.selected_url, self,file)
                #spotify_download_2(self.selected_url,self,file)
                self.ui.ding.hide()
                self.ui.donwload.show()
            except:
                print("an error accurad:")
                self.ui.ding.hide()
                self.ui.donwload.hide()
                self.ui.error.show()
        else:
            print("Error: URL not selected")
            self.ui.ding.hide()
            self.ui.donwload.hide()
            self.ui.error.show()

    def download_video_f(self):
        print("Facebook download started")
        self.selected_url = self.ui.lineEdit.text()
        self.ui.donwload.hide()
        self.ui.error.hide()
        if self.selected_url:
            file = QFileDialog.getExistingDirectory(parent=self,caption="Path of the video",dir=os.path.join(os.path.expanduser("~"), "Downloads"))###############################################
            print(file)
            try:
                self.ui.ding.show()
                QApplication.processEvents()
                facebook_download(self.selected_url, self,file)
                self.ui.ding.hide()
                self.ui.donwload.show()
            except:
                print("Invalid link or selected resolution unavailable!")
                self.ui.ding.hide()
                self.ui.donwload.hide()
                self.ui.error.show()
        else:
            print("Error: URL not selected")
            self.ui.ding.hide()
            self.ui.donwload.hide()
            self.ui.error.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
