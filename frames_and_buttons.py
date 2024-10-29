import tkinter as tk
import tkinter.messagebox 

class MyGUI:
    def __init__(self):
        #create the main window widget
        self.main_window = tk.Tk()

        #configure the main window
        self.main_window.geometry('500x200')
        self.main_window.title('Frame and Button Demo')

        #create 2 frame widgets
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)
        self.button_frame = tk.Frame(self.main_window)

        #create 3 label widgets for the top frame
        self.label1 = tk.Label(self.top_frame, text="Natalie")
        self.label2 = tk.Label(self.top_frame, text="Alexandra")
        self.label3 = tk.Label(self.top_frame, text="Pierce")

        #pack our labels
        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.label3.pack(side='right')


        #create 3 label widgets for the bottom frame
        self.label4 = tk.Label(self.bottom_frame, text="Jordan")
        self.label5 = tk.Label(self.bottom_frame, text="Hayden")
        self.label6 = tk.Label(self.bottom_frame, text="Cole")

        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='right')
        
        #create two button widgets 
        self.mybutton = tk.Button(self.button_frame,text='Click Me!',command=self.do_something)
        self.quitbutton = tk.Button(self.button_frame,text='Quit',command=self.main_window.destroy)

        self.mybutton.pack(side='left')
        self.quitbutton.pack(side='right')

        self.top_frame.pack()
        self.bottom_frame.pack()
        self.button_frame.pack()
    
        tk.mainloop()
    
    def do_something(self):
        tk.messagebox.showinfo('Response','Thanks for clicking me!')

#create an instance of the class
my_gui = MyGUI()

print('Moving on...')