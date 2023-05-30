from pytube import YouTube
from ytmusicapi import YTMusic
import PySimpleGUI as sg
import pafy
import time
import os
import sys

sg.theme("DarkGrey3")

def Title(Song):
    search = ytmusic.search(Song, "songs", None, 1, False)
    return str(search[0]['title'])

def Link(Song):
    search = ytmusic.search(Song, "songs", None, 1, False)
    Link = "https://youtube.com/watch?v=" + str(search[0]['videoId'])
    return Link

layout = [
    [sg.Text("Music Downloader")],
    [sg.Text("Enter the Musicname: "), sg.Input()],
    [sg.Text("Where should the File be saved: "), sg.FolderBrowse(key="-IN-")],
    [sg.Button("MP3"), sg.Button("WAV"), sg.Button("FLAC"), sg.Button("OGG")]
]

window = sg.Window("Music Downloader", icon="Icon.ico", element_justification='c').Layout(layout)
ytmusic = YTMusic()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "MP3":
        file = Title(values[0]) + ".mp3"
        yt = YouTube(Link(values[0])).streams.filter(only_audio=True).get_audio_only().download(output_path=values["-IN-"], filename=file)
        sg.Popup("Done!")
        window.close()
    elif event == "WAV":
        file = Title(values[0]) + ".wav"
        yt = YouTube(Link(values[0])).streams.filter(only_audio=True).get_audio_only().download(output_path=values["-IN-"], filename=file)
        sg.Popup("Done!")
        window.close()
    elif event == "FLAC":
        file = Title(values[0]) + ".flac"
        yt = YouTube(Link(values[0])).streams.filter(only_audio=True).get_audio_only().download(output_path=values["-IN-"], filename=file)
        sg.Popup("Done!")
        window.close()
    elif event == "OGG":
        file = Title(values[0]) + ".ogg"
        yt = YouTube(Link(values[0])).streams.filter(only_audio=True).get_audio_only().download(output_path=values["-IN-"], filename=file)
        sg.Popup("Done!")
        window.close()



window.close()