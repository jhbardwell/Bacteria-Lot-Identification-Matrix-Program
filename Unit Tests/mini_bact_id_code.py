from tkinter import*
from operator import*

class Fruit:
    def __init__(self, parent):



        #------ constants for controlling layout of buttons ------
        button_width = 6
        button_padx = "2m"
        button_pady = "1m"
        buttons_frame_padx =  "3m"
        buttons_frame_pady =  "2m"
        buttons_frame_ipadx = "3m"
        buttons_frame_ipady = "1m"
        # -------------- end constants ----------------


        # variables

        self.gram_option = StringVar()
        self.meta_option = StringVar()
        self.cat_option = StringVar()
        self.oxi_option = StringVar()
        
        ## Layout

        self.myParent = parent

        self.myContainer1 = Frame(parent, background="light blue")
        self.myContainer1.pack(expand=YES, fill=BOTH)


        # main left frame
        self.main_left_frame = Frame(self.myContainer1, background="light blue")
        self.main_left_frame.pack(side=LEFT, expand=YES, padx=5, pady=5, ipadx=5, ipady=5)

        # bottom frame
        self.bottom_frame = Frame(self.main_left_frame, background="light blue")
        self.bottom_frame.pack(side=BOTTOM, expand=YES, ipadx=1, ipady=1)

        # control_frame
        self.control_frame = Frame(self.main_left_frame, background="light blue")
        self.control_frame.pack(side=TOP, expand=YES, padx=5, pady=5, ipadx=5, ipady=5)

        # control_left_frame
        self.control_left_frame = Frame(self.control_frame, background="light blue")
        self.control_left_frame.pack(side=LEFT, anchor=N, expand=YES, padx=10, pady=5, ipadx=5, ipady=5)

        # control_center_frame
        self.control_center_frame = Frame(self.control_frame, background="light blue")
        self.control_center_frame.pack(side=LEFT, anchor=N, expand=YES, padx=10, pady=5, ipadx=5, ipady=5)

        # control_right_frame
        self.control_right_frame = Frame(self.control_frame, background="light blue")
        self.control_right_frame.pack(side=LEFT, anchor=N, expand=YES, fill=X, padx=10, pady=5, ipadx=5, ipady=5)

        # main right frame
        self.main_right_frame = Frame(self.myContainer1, background="white") 
        self.main_right_frame.pack(side=RIGHT, expand=YES, fill=BOTH)

        # heading frame
        self.heading_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.heading_frame.pack(expand=NO)
        Label(self.heading_frame, text="      IDENTIFICATION      ", font=8, background="white").pack(side=TOP,anchor=N)
        
        # id frame
        self.id_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.id_frame.pack(expand=NO, fill=BOTH)

        # test result radiobuttons
        cat_options = ["+", "--"]
        gram_options = ["+", "--"]
        meta_options = ["aerobe", "fac anaerobe"]
        oxi_options = ["+", "--"]


        def change():
            color="white"
        color="light blue"
        
        
        self.gram_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.gram_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.gram_options_frame, text="GRAM STAIN:", relief=RAISED, background=color).pack(side=LEFT,anchor=W)
        for option in gram_options:
            button = Radiobutton(self.gram_options_frame, text=str(option), indicatoron=0,
            value=option, command=change, padx=5, variable=self.gram_option, background="light blue")
            button.pack(side=LEFT)

        self.meta_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.meta_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.meta_options_frame, text="METABOLISM:", relief=RAISED, background=color).pack(side=LEFT,anchor=W)
        for option in meta_options:
            button = Radiobutton(self.meta_options_frame, text=str(option), indicatoron=0,
            value=option, command=change, padx=5, variable=self.meta_option, background="light blue")
            button.pack(side=LEFT)
    
        self.cat_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.cat_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.cat_options_frame, text="CATALASE:", relief=RAISED, background=color).pack(side=LEFT,anchor=W)
        for option in cat_options:
            button = Radiobutton(self.cat_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.cat_option, background="light blue")
            button.pack(side=LEFT)
    
        self.oxi_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.oxi_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.oxi_options_frame, text="OXIDASE:", relief=RAISED, background=color).pack(side=LEFT,anchor=W)
        for option in oxi_options:
            button = Radiobutton(self.oxi_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.oxi_option, background="light blue")
            button.pack(side=LEFT)
  

        # identify button

        self.idbutton = Button(self.bottom_frame,text="Identify", background="dark green", foreground="white",
        width=button_width, padx=button_padx, pady=button_pady)

        self.idbutton.pack(side=LEFT)

        self.idbutton.bind("<Button-1>", self.idbuttonclick)
        self.idbutton.bind("<Return>", self.idbuttonclick)


        # reset button

        self.resetbutton = Button(self.bottom_frame,text="Reset", background="red", foreground="white",
        width=button_width, padx=button_padx, pady=button_pady)

        self.resetbutton.pack(side=RIGHT)

        self.resetbutton.bind("<Button-1>", self.resetbuttonclick)
        self.resetbutton.bind("<Return>", self.resetbuttonclick)



        x=0.50
        self.bac=[
        ('Aeromonas',0.95,x),
        ('Bacillus',0.05, 0.95),
        ('Hafnia',0.51, 0.51)]

      

    
        
    def searchbuttonclick(self):

        nothing
    
    def resetbuttonclick(self, event):

        self.cat_option.set("cat")
        self.gram_option.set("gram")
        self.meta_option.set("meta")
        self.oxi_option.set("oxi")

        
        self.id_frame.destroy()
        self.id_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.id_frame.pack(side=TOP, fill=BOTH)



    def idbuttonclick(self, event):

        self.id_frame.destroy()
        self.id_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.id_frame.pack(side=TOP, fill=BOTH)

        
        if (self.gram_option.get()=="+" and
        self.meta_option.get()=="aerobe"):
            Label(self.id_frame, text = "Gram Positive Aerobe", background = "white").pack(side=TOP, anchor = N)
            bac=self.bac

            
           

    
        else: Label(self.id_frame, text = "Error: Not enough data", background = "white").pack(side=TOP, anchor = N)
    
        def plus(matrix, i):
            return [row[i] for row in matrix]

        def minus(matrix, i):
            return [1.00-row[i] for row in matrix]

        def average(lst):
            return sum(lst) / len(lst)

        bact=zip(*bac)
        bact2=bact[0:1]
        bact3=bact[0:1]

        if self.cat_option.get()=="+":
            bact2.append(plus(bac,1))
            bact3.append(plus(bac,1))
        if self.cat_option.get()=="--":
            bact2.append(minus(bac,1))
            bact3.append(plus(bac,1))

        if self.oxi_option.get()=="+":
            bact2.append(plus(bac,2))
            bact3.append(plus(bac,2))

        if self.oxi_option.get()=="--":
            bact2.append(minus(bac,2))
            bact3.append(plus(bac,2))


        bac2=zip(*bact2)
        bac3=zip(*bact3)
        
        
        #experimental additive probability
        #bac4 = [(bac2[0],reduce(mul,bac2[1:])) for bac2 in bac2]

        #experimental mean probability
        #bac4 = [(bac2[0], average(bac2[1:])) for bac2 in bac2]
        bac4 = [(bac2[0], average(filter(lambda elt: elt != 0.50, bac2[1:]))) for bac2 in bac2]

        #experimental additive probability / expected outcome additive probability
        #bac4 = [(bac2[0],reduce(mul,bac2[1:])/reduce(mul,bac3[1:])) for (bac2,bac3) in zip(bac2,bac3)]
        
        bac5 = tuple(sorted(bac4, key=lambda item: item[1], reverse=True))


        Label(self.id_frame, text = bac5[0], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = bac5[1], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = bac5[2], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = bac5[3], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = bac5[4], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = bac5[5], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = bac5[6], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = bac5[7], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = bac5[8], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = bac5[9], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = bac5[10], background = "white").pack(side=TOP, anchor = W)

root = Tk()
fruit = Fruit(root)
#root.withdraw()
root.mainloop()
