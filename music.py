import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.playlist = []
        self.current_track = 0

        self.load_playlist_button = tk.Button(root, text="Load Playlist", command=self.load_playlist)
        self.load_playlist_button.pack()

        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack()

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.pause_button.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_track)
        self.next_button.pack()

        self.previous_button = tk.Button(root, text="Previous", command=self.previous_track)
        self.previous_button.pack()

        self.volume_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", label="Volume", command=self.adjust_volume)
        self.volume_scale.set(50)
        self.volume_scale.pack()

        pygame.mixer.init()

    def load_playlist(self):
        folder_path = filedialog.askdirectory(initialdir="./", title="Select Folder")
        if folder_path:
            self.playlist = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith(".mp3")]
            if self.playlist:
                self.current_track = 0
                self.play_music()

    def play_music(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def next_track(self):
        if self.playlist:
            self.current_track = (self.current_track + 1) % len(self.playlist)
            self.play_music()

    def previous_track(self):
        if self.playlist:
            self.current_track = (self.current_track - 1) % len(self.playlist)
            self.play_music()

    def adjust_volume(self, volume):
        pygame.mixer.music.set_volume(int(volume) / 100)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
