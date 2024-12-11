from tkinter import Tk, Label, Entry, Button
from pytube import YouTube

def download_high():
    url = link_entry.get()
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    status_label.config(text="Downloaded in High Quality!")

def download_low():
    url = link_entry.get()
    yt = YouTube(url)
    stream = yt.streams.get_lowest_resolution()
    stream.download()
    status_label.config(text="Downloaded in Low Quality!")

def download_audio():
    url = link_entry.get()
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download()
    status_label.config(text="Audio Downloaded!")

root = Tk()
root.title("YouTube Downloader")

title_label = Label(root, text="YouTube Downloader")
title_label.pack()

link_label = Label(root, text="Enter Video Link:")
link_label.pack()
link_entry = Entry(root, width=50)
link_entry.pack()

high_button = Button(root, text="High Quality", command=download_high)
high_button.pack()

low_button = Button(root, text="Low Quality", command=download_low)
low_button.pack()

audio_button = Button(root, text="Audio Only", command=download_audio)
audio_button.pack()

status_label = Label(root, text="")
status_label.pack()

root.mainloop()