from Tkinter import*

class Fruit:
    def __init__(self, parent):

        # variables
        self.texture_option = StringVar()
        self.climate_option = StringVar()

        # layout
        self.myParent = parent

        self.main_frame = Frame(parent, background="light blue")
        self.main_frame.pack(expand=YES, fill=BOTH)

        texture_options = ["Soft", "Crunchy","?"]
        climate_options = ["Temperate", "Tropical","?"]

        self.texture_option.set("?")
        self.climate_option.set("?")

        self.texture_options_frame = Frame(self.main_frame, borderwidth=3, background="light blue")
        self.texture_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.texture_options_frame, text="Texture:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in texture_options:
            button = Radiobutton(self.texture_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.texture_option, background="light blue")
            button.pack(side=LEFT)

        self.climate_options_frame = Frame(self.main_frame, borderwidth=3, background="light blue")
        self.climate_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.climate_options_frame, text="Climate:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in climate_options:
            button = Radiobutton(self.climate_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.climate_option, background="light blue")
            button.pack(side=LEFT)
    
        #search button
        self.search_frame = Frame(self.main_frame, borderwidth=5, height=50, background="light blue")
        self.search_frame.pack(expand=NO)

        self.enter = Entry(self.search_frame, width=30)
        self.enter.pack(side=LEFT, expand=NO, padx=5, pady=5, ipadx=5, ipady=5)

        self.searchbutton = Button(self.search_frame, text="Search", foreground="white", background="blue",
        width=6, padx="2m", pady="1m")
        self.searchbutton.pack(side=LEFT, pady=5)
        self.searchbutton.bind("<Button-1>", self.searchbuttonclick)
        self.searchbutton.bind("<Return>", self.searchbuttonclick)


    def searchbuttonclick(self,event):
        #fruit  texture  climate 
        fruit_bowl=[
        ('Apple', 'Crunchy','Temperate'),
        ('Apricot','Soft','Tropical'),
        ('Orange', 'Soft','Tropical'),
        ('Pawpaw','Soft','Temperate'),
        ('Pear','Crunchy','Temperate')]

        for fruit in fruit_bowl:
            i = fruit_bowl.index(fruit)
            if self.enter.get()==fruit_bowl[i][0]:
                self.texture_option.set(fruit_bowl[i][1])
                self.climate_option.set(fruit_bowl[i][2]) 


root = Tk()
root.title("Fruit Bowl")
fruit = Fruit(root)
root.mainloop()
