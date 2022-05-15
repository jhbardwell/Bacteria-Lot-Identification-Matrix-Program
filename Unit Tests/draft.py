from tkinter import *

class MyApp:
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

        self.shape_option   = StringVar()

        self.meta_option = StringVar()

        self.cat_option = StringVar()

        self.oxi_option = StringVar()

        self.endo_option = StringVar()

        self.motil_option = StringVar()

        self.h2s_option = StringVar()

        self.ind_option = StringVar()

        self.cit_option = StringVar()

        self.nit_option = StringVar()

        self.urea_option = StringVar()

        self.glu_option = StringVar()

        self.arab_option = StringVar()

        self.glyc_option = StringVar()

        self.lac_option = StringVar()

        self.man_option = StringVar()

        self.sal_option = StringVar()

        self.sorb_option = StringVar()

        self.suc_option = StringVar()

        self.xyl_option = StringVar()

        self.salt_option = StringVar()

        self.temp_option = StringVar()

        ## Layout

        self.myParent = parent

        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        # main left frame
        self.main_left_frame = Frame(self.myContainer1)
        self.main_left_frame.pack(side=LEFT, expand=NO,  padx=10, pady=5, ipadx=5, ipady=5)

        # heading frame
        self.heading_frame = Frame(self.main_left_frame)
        self.heading_frame.pack(side=TOP, expand=NO,  padx=10, pady=5, ipadx=5, ipady=5)

        message="Use these phenotypic traits to identify your bacteria. \n Highlight trait names for required tests/agers and result interpretation\n"
        Label(self.heading_frame, text=message, justify=LEFT).pack(side=TOP, anchor=W)

        # bottom frame
        self.bottom_frame = Frame(self.main_left_frame)
        self.bottom_frame.pack(side=BOTTOM, expand=NO,  padx=10, pady=5, ipadx=5, ipady=5)

        # control_frame
        self.control_frame = Frame(self.main_left_frame)
        self.control_frame.pack(side=TOP, expand=NO,  padx=10, pady=5, ipadx=5, ipady=5)

        # control_left_frame
        self.control_left_frame = Frame(self.control_frame)
        self.control_left_frame.pack(side=LEFT, expand=NO,  padx=10, pady=5, ipadx=5, ipady=5)

        # control_right_frame
        self.control_right_frame = Frame(self.control_frame)
        self.control_right_frame.pack(side=LEFT, expand=NO,  padx=10, pady=5, ipadx=5, ipady=5)

        # main right frame
        self.main_right_frame = Frame(self.myContainer1) 
        self.main_right_frame.pack(side=RIGHT, expand=YES, fill=BOTH)

        # id frame
        self.id_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.id_frame.pack(side=TOP, fill=BOTH)

        # graphics frame
        self.graphics_frame = Frame(self.main_right_frame, background="light blue",borderwidth=5, relief=RIDGE, width=250)
        self.graphics_frame.pack(side=BOTTOM, expand=YES, fill=BOTH)

        gram_options = ["GRAM STAIN:", "+", "--"]
        shape_options = ["SHAPE:", "bacillus", "coccus", "spirochete"]
        meta_options = ["METABOLISM:", "aerobe", "fac anaerobe"]
        cat_options = ["CATALASE:", "+", "--"]
        oxi_options = ["OXIDASE:", "+", "--"]
        endo_options = ["ENDOSPORE:", "+", "--"]
        motil_options = ["MOTILITY:", "+", "--"]
        h2s_options = ["HYDROGEN SULFIDE:", "+", "--"]
        ind_options = ["INDOLE:", "+", "--"]
        cit_options = ["CITRATE:", "+", "--"]
        nit_options = ["NITRATE REDUC:", "+", "--"]
        urea_options = ["UREA HYDROL:", "+", "--"]
        glu_options = ["GLUCOSE FERM:", "+", "--"]
        arab_options = ["ARABINOSE FERM:", "+", "--"]
        glyc_options = ["GLYCEROL FERM:", "+", "--"]
        lac_options = ["LACTOSE FERM:", "+", "--"]
        man_options = ["MANNITOL FERM:", "+", "--"]
        sal_options = ["SALICIN FERM:", "+", "--"]
        sorb_options = ["SORBITOL FERM:", "+", "--"]
        suc_options = ["SUCROSE FERM:", "+", "--"]
        xyl_options = ["XYLOSE FERM:", "+", "--"]
        salt_options = ["SALINITY RANGE:", "<6%", "6-8%", ">8%"]
        temp_options = ["TEMP RANGE:", "25C", "35C", "45C"] 


        self.gram_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.gram_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.shape_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.shape_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.meta_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.meta_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.cat_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.cat_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.oxi_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.oxi_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.endo_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.endo_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.motil_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.motil_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.h2s_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.h2s_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.ind_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.ind_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.cit_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.cit_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.nit_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.nit_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.urea_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.urea_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.glu_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.glu_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.arab_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.arab_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.glyc_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.glyc_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.lac_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.lac_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.man_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.man_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.sal_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.sal_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.sorb_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.sorb_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.suc_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.suc_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.xyl_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.xyl_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.salt_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.salt_options_frame.pack(side=TOP, expand=YES, anchor=W)

        self.temp_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.temp_options_frame.pack(side=TOP, expand=YES, anchor=W)

        # phenotype radiobuttons
        for option in gram_options:
            button = Radiobutton(self.gram_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.gram_option)
            button.pack(side=LEFT)

        for option in shape_options:
            button = Radiobutton(self.shape_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.shape_option)
            button.pack(side=LEFT)

        for option in meta_options:
            button = Radiobutton(self.meta_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.meta_option)
            button.pack(side=LEFT)

        for option in cat_options:
            button = Radiobutton(self.cat_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.cat_option)
            button.pack(side=LEFT)

        for option in oxi_options:
            button = Radiobutton(self.oxi_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.oxi_option)
            button.pack(side=LEFT)

        for option in endo_options:
            button = Radiobutton(self.endo_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.endo_option)
            button.pack(side=LEFT)

        for option in motil_options:
            button = Radiobutton(self.motil_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.motil_option)
            button.pack(side=LEFT)

        for option in h2s_options:
            button = Radiobutton(self.h2s_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.h2s_option)
            button.pack(side=LEFT)

        for option in ind_options:
            button = Radiobutton(self.ind_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.ind_option)
            button.pack(side=LEFT)

        for option in cit_options:
            button = Radiobutton(self.cit_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.cit_option)
            button.pack(side=LEFT)

        for option in nit_options:
            button = Radiobutton(self.nit_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.nit_option)
            button.pack(side=LEFT)

        for option in urea_options:
            button = Radiobutton(self.urea_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.urea_option)
            button.pack(side=LEFT)

        for option in glu_options:
            button = Radiobutton(self.glu_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.glu_option)
            button.pack(side=LEFT)

        for option in arab_options:
            button = Radiobutton(self.arab_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.arab_option)
            button.pack(side=LEFT)

        for option in glyc_options:
            button = Radiobutton(self.glyc_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.glyc_option)
            button.pack(side=LEFT)

        for option in lac_options:
            button = Radiobutton(self.lac_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.lac_option)
            button.pack(side=LEFT)

        for option in man_options:
            button = Radiobutton(self.man_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.man_option)
            button.pack(side=LEFT)

        for option in sal_options:
            button = Radiobutton(self.sal_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.sal_option)
            button.pack(side=LEFT)

        for option in sorb_options:
            button = Radiobutton(self.sorb_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.sorb_option)
            button.pack(side=LEFT)

        for option in suc_options:
            button = Radiobutton(self.suc_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.suc_option)
            button.pack(side=LEFT)

        for option in xyl_options:
            button = Radiobutton(self.xyl_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.xyl_option)
            button.pack(side=LEFT)

        for option in salt_options:
            button = Radiobutton(self.salt_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.salt_option)
            button.pack(side=LEFT)

        for option in temp_options:
            button = Radiobutton(self.temp_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.temp_option)
            button.pack(side=LEFT)


        # reset button

        self.resetbutton = Button(self.bottom_frame,text="Reset", background="white",
        width=button_width, padx=button_padx, pady=button_pady)

        self.resetbutton.pack(side=RIGHT)

        self.resetbutton.bind("<Button-1>", self.resetbuttonclick)
        self.resetbutton.bind("<Return>", self.resetbuttonclick)



        # id button

        self.idbutton = Button(self.bottom_frame, text="ID", background="white",
        width=button_width, padx=button_padx, pady=button_pady)

        self.idbutton.pack(side=LEFT)

        self.idbutton.bind("<Button-1>", self.idbuttonclick)
        self.idbutton.bind("<Return>", self.idbuttonclick)



    def resetbuttonclick(self, event):

        self.gram_option.set("gram")
        self.shape_option.set("shape")
        self.meta_option.set("meta")
        self.cat_option.set("cat")
        self.oxi_option.set("oxi")
        self.endo_option.set("endo")
        self.motil_option.set("motil")
        self.h2s_option.set("h2s")
        self.ind_option.set("ind")
        self.cit_option.set("cit")
        self.nit_option.set("nit")
        self.urea_option.set("urea")
        self.glu_option.set("glu")
        self.arab_option.set("arab")
        self.glyc_option.set("glyc")
        self.lac_option.set("lac")
        self.man_option.set("man")
        self.sal_option.set("sal")
        self.sorb_option.set("sorb")
        self.suc_option.set("suc")
        self.xyl_option.set("xyl")
        self.salt_option.set("salt")
        self.temp_option.set("temp")

        self.id_frame.destroy()
        self.id_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.id_frame.pack(side=TOP, fill=BOTH)


    def idbuttonclick(self, event):

        self.id_frame.destroy()
        self.id_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.id_frame.pack(side=TOP, fill=BOTH)

        if (self.gram_option.get()==("+") or
        self.shape_option.get()==("bacillus")):
            id = "Bacillus sp."
            Label(self.id_frame, text = id, background = "white").pack(side=TOP, anchor = W)

        if (self.gram_option.get()==("+") 
        self.shape_option.get()==("coccus")):
            id = "Bogus sp."
            Label(self.id_frame, text = id, background = "white").pack(side=TOP, anchor = W)
            
        else: Label(self.id_frame, text = "Error: need more data", background = "white").pack(side=TOP, anchor = N)




 
root = Tk()
root.title("Freshwater Bacteria Database")
myapp = MyApp(root)
#root.withdraw()
root.mainloop()
