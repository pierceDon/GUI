import tkinter as tk
import tkinter.messagebox 

class KiloConverter:
    def __init__(self):
        #create the main window widget
        self.main_window = tk.Tk()

        #configure the main window
        self.main_window.geometry('300x100')
        self.main_window.title('Frame and Button Demo')

        #create 2 frame widgets
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        #create 3 label widgets for the top frame
        self.prompt = tk.Label(self.top_frame, text="Enter distance in Kms: ")
        self.kilo_entry = tk.Entry(self.top_frame,width=10)

        #pack our labels
        self.prompt.pack(side='left')
        self.kilo_entry.pack(side='left')

        
        #create two button widgets 
        self.calcbutton = tk.Button(self.bottom_frame,text='Convert!',command=self.convert)
        self.quitbutton = tk.Button(self.bottom_frame,text='Quit',command=self.main_window.destroy)

        self.calcbutton.pack(side='left')
        self.quitbutton.pack(side='right')

        self.top_frame.pack()
        self.bottom_frame.pack()
    
        tk.mainloop()
    
    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = round(kilo * 0.6214, 2)


        tk.messagebox.showinfo('Response',str(kilo) + ' kilometers is equal to ' + str(miles) + ' miles.')

#create an instance of the class
my_gui = KiloConverter()

print('Moving on...')