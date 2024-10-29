import tkinter as tk
import tkinter.messagebox 

class MyGUI:
    def __init__(self):
        #create the main window widget
        self.main_window = tk.Tk()

        #configure the main window
        self.main_window.geometry('300x100')
        self.main_window.title('Frame and Button Demo')

        #create 2 frame widgets
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        #create an IntVar to use with radio buttons
        self.radio_var = tk.IntVar()

        #self.radio_var.set(1)

        self.rb1 = tk.Radiobutton(self.top_frame,
                                  text='Option 1',
                                  variable=self.radio_var,
                                  value=1)
        
        self.rb2 = tk.Radiobutton(self.top_frame,
                                  text='Option 2',
                                  variable=self.radio_var,
                                  value=2)
        
        self.rb3 = tk.Radiobutton(self.top_frame,
                                  text='Option 3',
                                  variable=self.radio_var,
                                  value=3)

        #create a version of rb3 that doesn't require you to press ok
        # self.rb3 = tk.Radiobutton(self.top_frame,
        #                           text='Option 3',
        #                           variable=self.radio_var,
        #                           value=3,command=self.show_choice)
        

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        #create two button widgets 
        self.okbutton = tk.Button(self.bottom_frame,text='Ok',command=self.show_choice).pack(side='left')
        self.quitbutton = tk.Button(self.bottom_frame,text='Quit',command=self.main_window.destroy).pack(side='left')
        self.resetbutton = tk.Button(self.bottom_frame, text='Reset', command=self.reset).pack(side="left")


        self.top_frame.pack()
        self.bottom_frame.pack()
    
        tk.mainloop()
    
    def show_choice(self):
        tk.messagebox.showinfo('Selection', 'You have selected option ' + str(self.radio_var.get()))

    def reset(self):
        self.radio_var.set(1)


#create an instance of the class
my_gui = MyGUI()

print('Moving on...')