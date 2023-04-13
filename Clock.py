from tkinter import Label, Tk
import time

class Clock:
    def __init__(self):
        self.window = Tk()
        self.window.title("Digital clock")
        self.window.geometry("420x150")
        self.window.resizable(1,1)
        