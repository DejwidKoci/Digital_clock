from tkinter import Label, Tk
import time

class Clock:
    def __init__(self):
        self.window = Tk()
        self.window.title("Digital clock")
        self.window.geometry("420x150")
        self.window.resizable(0,0)
        
        self.text_font = ("Boulder", 68, 'bold')
        self.background = "#66FF33"
        self.foreground = "#363529"
        self.border_width = 25
        
        self.show_clock()
        self.digital_clock()
        self.window.mainloop()
    
    def show_clock(self):
        self.label = Label(self.window, font = self.text_font, bg = self.background,
                      fg = self.foreground, bd = self.border_width)
        self.label.grid(row = 0, column = 1)

    def digital_clock(self):
        time_live = time.strftime("%H:%M:%S")
        self.label.config(text = time_live)
        self.label.after(200, self.digital_clock)

if __name__ == "__main__":
    zegar = Clock()

    
