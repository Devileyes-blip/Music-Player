from tkinter import Tk,Button,filedialog,Frame
import Child_window
import pygame
import os
import tkinter
import threading


#Initialize pygame mixer
class Music_Player:
    #Class for every action in the music player
    def __init__(self):
        #Initialize the Music Player attributes
        pygame.mixer.init()
        self.ispause = False

    def play_song(self,path):
        #Play a song when button click and stop a song playing before starting a new one
        pygame.mixer.music.stop()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

    def close(self):
        #Will destroy the window
        pygame.mixer.music.stop()
        root.destroy()

    def multiple_task(self,path):
        #To peform multiple task in the button
        threading.Thread(target = self.play_song, args = (path,), daemon = True).start()
        Child_window.open_window(root,self)
        

    def pause_(self):
        #Pause the song which is playing
        if self.ispause == True:
            self.ispause = False
            pygame.mixer.music.unpause()
        elif self.ispause == False:
            self.ispause = True
            pygame.mixer.music.pause()


class Song_Path_Loader:
    #To load the Song path
    def __init__(self,player):
        #Initalize for the song path loader class
        self.songs = {}
        self.player = player
    
    def song_add(self):
        #To add a song
        file_path = filedialog.askopenfilename(title = 'Select song',filetypes = [('Audio Files','*.mp3')])
        if file_path:
            song_name = os.path.basename(file_path)
            self.songs[song_name] = file_path
            button = Button(root,text = song_name,command = lambda: self.player.multiple_task(file_path))
            button.pack(pady= 5, fill= tkinter.X)
    

class Create_Widgets:
    #Make GUI of the application
    def __init__(self,root,add,player):
        #Initialize the Music Player attributes
        self.root = root
        self.add = add
        self.player = player
        self.create_widget()
        
    
    def create_widget(self):
        #Create Add button
        button_frame = Frame(self.root)
        button_frame.pack(pady= 20)
        add_button = Button(button_frame,text='Add',command = self.add.song_add)
        add_button.pack(side= 'left',padx = 10)

        close_button = Button(button_frame, text= 'Close',command= self.player.close)
        close_button.pack(side = 'left',padx = 10)

        pause_button = Button(button_frame, text= 'Pause',command= self.player.pause_)
        pause_button.pack(side= 'left',padx = 10)

def on_closing():
    #Function to stop the song when the 'X' button is clicked on the title bar
    pygame.mixer.music.stop()
    root.destroy()
    
def set_background(root,image_path):
    #Set the background
    image = Image.open(image_path)
    image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(image)
    background_label = Label(root,image = bg_image)
    background_label.image = bg_image
    background_label.place(x = 0,y = 0,relwidth = 1,relheight = 1)
#Main Window
root = Tk()
root.title('Music Player Home')
root.protocol("WM_DELETE_WINDOW", on_closing)
app = Music_Player()
song_load = Song_Path_Loader(app)
widget = Create_Widgets(root,song_load,app)
set_background(root,"C:\\Users\\ryzen\\OneDrive\\Desktop\\Music_Player\\image_back.png")


root.mainloop()

