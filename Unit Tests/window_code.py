from Tkinter import*
from operator import*

root = Tk()
root.title("Jungle")

class Jungle:
    def __init__(self, parent):

        # variables
        self.group_option = StringVar()
        self.lions = DoubleVar()
        self.tigers = DoubleVar()
        self.bears = DoubleVar()

        group_options = ["Lions","Tigers","Bears"]

        # layout
        self.myParent = parent

        self.main_left_frame = Frame(parent, background="red")
        self.main_left_frame.pack(side=LEFT, expand=YES, fill=BOTH)

        for option in group_options:
            button = Radiobutton(self.main_left_frame, text=str(option), indicatoron=1,
            value=option, padx=5, variable=self.group_option, background="red")
            button.pack(side=TOP, anchor=W)

        self.main_right_frame = Frame(parent, background="red")
        self.main_right_frame.pack(side=RIGHT, expand=YES, fill=BOTH)

        self.lions = Entry(self.main_right_frame, width=4)
        self.lions.pack(side=TOP, expand=NO)

        self.tigers = Entry(self.main_right_frame, width=4)
        self.tigers.pack(side=TOP, expand=NO)

        self.bears = Entry(self.main_right_frame, width=4)
        self.bears.pack(side=TOP, expand=NO)


fruit = Jungle(root)
root.mainloop()
