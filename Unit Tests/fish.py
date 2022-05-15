from Tkinter import (N, S, E, W, BOTH, BOTTOM, END, FLAT, HORIZONTAL, LEFT, NO, RAISED, RIGHT, TOP, YES,
Button, Entry, Frame, Grid, Label, Pack, Scale, Text, Tk)

from operator import mul

root = Tk()
root.title('Example')

class Environment:
    def __init__(self, parent):

        # layout
        self.myParent = parent

        self.main_frame = Frame(parent, background="light blue")
        self.main_frame.pack(expand=YES, fill=BOTH)

        self.main_left_frame = Frame(self.main_frame, background="light blue")
        self.main_left_frame.pack(side=LEFT, expand=YES, fill=BOTH)

        self.main_right_frame = Frame(self.main_frame, background="light blue")
        self.main_right_frame.pack(side=RIGHT, expand=YES, fill=BOTH)

        self.water = Scale(self.main_right_frame, from_=0.01, to=1.00, orient=HORIZONTAL, bd=0, label="Aquatic",
        background="white", troughcolor="cyan", length=50, width=10, sliderlength=10, resolution=0.01)
        self.water.pack()
        self.water.set(1.00)

        self.soil = Scale(self.main_right_frame, from_=0.01, to=1.00, orient=HORIZONTAL, bd=0, label="Terrestrial",
        background="white", troughcolor="saddle brown", length=50, width=10, sliderlength=10, resolution=0.01)
        self.soil.pack()
        self.soil.set(1.00)

        self.id_frame = Frame(self.main_left_frame, background="white")
        self.id_frame.pack(side=BOTTOM)

        # submit button
        self.submitbutton = Button(self.main_left_frame,text="Submit", background="black", foreground="white",
        width=6, padx="2m", pady="1m")
        self.submitbutton.pack(side=TOP)
        self.submitbutton.bind("<Button-1>", self.submitbuttonclick)
        self.submitbutton.bind("<Return>", self.submitbuttonclick)

        #Animal Matrix
        s = self.soil.get
        w = self.water.get
        sw = lambda:1-(1-self.soil.get())*(1-self.water.get())
        
        self.animal = [
        ('Odocoileous virginiana','White-tailed Deer',s,0.99,0.01,0.99),
        ('Anguilla anguilla','American Eel',w,0.99,0.01,0.99),
        ('Trachemys scripta','Red-eared Slider',sw,0.99,0.01,0.99)]

    def submitbuttonclick(self, event):
        self.id_frame.destroy()
        self.id_frame = Frame(self.main_left_frame, background="white")
        self.id_frame.pack(side=BOTTOM)

        A=self.animal

        #equation
        sigma = float(sum(reduce(mul,item[3:]) for item in A))
        B = [(item[0], "%.2f" % (item[2]()*reduce(mul, item[3:])/sigma)) for item in A]
        C = sorted(B, key=lambda item: item[1], reverse=True)  

        Label(self.id_frame, text = C[0], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = C[1], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = C[2], background = "white").pack(side=TOP, anchor = W)
        
environment = Environment(root)       
root.mainloop()




































