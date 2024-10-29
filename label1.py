import tkinter as tk

class MyGUI:
    def __init__(self):
        #create the main window widget
        self.main_window = tk.Tk()

        #configure the main window
        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        #create 2 label widgets
        self.label1 = tk.Label(self.main_window, text="Hello World!")
        self.label2 = tk.Label(self.main_window, text="This is my GUI program.")

        #pack our labels
        self.label1.pack(side='left')
        self.label2.pack(side='right')

        tk.mainloop()

#create an instance of the class
my_gui = MyGUI()

print('Moving on...')