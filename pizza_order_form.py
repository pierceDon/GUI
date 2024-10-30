import tkinter as tk
import tkinter.messagebox 

class PizzaForm:
    def __init__(self):
        #create the main window widget
        self.main_window = tk.Tk()

        #configure the main window
        self.main_window.geometry('500x600')
        self.main_window.title('Pizza Order Form')

        #create 2 frame widgets
        self.top_frame = tk.Frame(self.main_window)
        
        self.mid_frame = tk.Frame(self.main_window)

        self.bottom_frame = tk.Frame(self.main_window)


        #create 2 label widgets for the top frame
        self.name_label = tk.Label(self.top_frame, text="Name: ")
        self.name_entry = tk.Entry(self.top_frame,width=10, )
        self.address_label = tk.Label(self.top_frame, text="Address: ")
        self.address_entry = tk.Entry(self.top_frame,width=10)
        

        #pack our labels
        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')
        self.address_label.pack(side='left')
        self.address_entry.pack(side='left')

        self.sauce_label = tk.Label(self.mid_frame, text="Choose your sauce:").pack()
        self.select = tk.StringVar()
        self.sauce_menu = tk.OptionMenu(self.mid_frame, self.select, 'Tomato','Alfredo','Pesto').pack()

#create an IntVar to use with radio buttons
        self.size_var = tk.IntVar()

        #self.radio_var.set(1)

        self.rb1 = tk.Radiobutton(self.mid_frame,
                                  text='Small ($6.99)',
                                  variable=self.size_var,
                                  value=7)
        
        self.rb2 = tk.Radiobutton(self.mid_frame,
                                  text='Medium ($7.99)',
                                  variable=self.size_var,
                                  value=8)
        
        self.rb3 = tk.Radiobutton(self.mid_frame,
                                  text='Large ($8.99)',
                                  variable=self.size_var,
                                  value=9)
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        
#create an IntVar to use with checkboxes
        self.cb_var1 = tk.IntVar()
        self.cb_var2 = tk.IntVar()
        self.cb_var3 = tk.IntVar()

        #self.radio_var.set(1)
        self.cb1 = tk.Checkbutton(self.mid_frame,
                                  text='Pepperoni ($0.99)',
                                  variable=self.cb_var1)
        
        self.cb2 = tk.Checkbutton(self.mid_frame,
                                  text='Mushrooms ($0.99)',
                                  variable=self.cb_var2)
        
        self.cb3 = tk.Checkbutton(self.mid_frame,
                                  text='Extra Cheese ($0.99)',
                                  variable=self.cb_var3)
        
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        
        #create two radio button widgets 
        self.receive_var = tk.IntVar()

        self.rb4 = tk.Radiobutton(self.bottom_frame,
                                  text='Pickup',
                                  variable=self.receive_var,
                                  value=0)
        self.rb5 = tk.Radiobutton(self.bottom_frame,
                                  text='Delivery ($3)',
                                  variable=self.receive_var,
                                  value=3)
        
        self.rb4.pack( )
        self.rb5.pack()
        
        #create total button
        
        self.totalbutton = tk.Button(self.bottom_frame,text="Calculate Total",command=self.calcTotal).pack()
        self.total_label = tk.Label(self.bottom_frame,text="Total (including tax and delivery): $").pack()
        self.total_var = tk.StringVar()
        self.total_price = tk.Label(self.bottom_frame,textvariable=self.total_var).pack()
        
        # create widgets for bottom frame
        self.confirmbutton = tk.Button(self.bottom_frame,text='Confirm Order',command=self.confirmation)
        self.quitbutton = tk.Button(self.bottom_frame,text='Quit',command=self.main_window.destroy)

        self.confirmbutton.pack(side='left')
        self.quitbutton.pack(side='right')

        self.top_frame.pack()
        
        self.mid_frame.pack()

        self.bottom_frame.pack()
    
        tk.mainloop()

    # def calcTotal(self):
    #     if self.

    def calcTotal(self):
        subtotal = (float(self.size_var.get()) - 0.01) + 0.99*float(self.cb_var1.get()) + 0.99*float(self.cb_var2.get()) + 0.99*float(self.cb_var3.get()) + (float(self.receive_var.get()))
        total = str(round(subtotal*1.08,2))
        self.total_var.set(total)

    def confirmation(self):
        self.calcTotal
        name = str(self.name_entry.get())
        address = str(self.address_entry.get())
       
        if self.receive_var.get() == 3:
            tk.messagebox.showinfo('Response', f'Order confirmed for {name}.\nFresh pizza will be delivered to {address} shortly!\nTotal: ${self.total_var.get()}')
        else:
             tk.messagebox.showinfo('Response', f'Order confirmed for {name}!\nTotal: ${self.total_var.get()}')


    

#create an instance of the class
my_gui = PizzaForm()

