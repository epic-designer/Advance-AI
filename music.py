from playsound import playsound
import glob

def Create_Playlist(path):
    for song in glob.glob(path):
        print("Playing" + song)
        playsound(song)

Create_Playlist("E:\My_Playlist__1\Deno James")