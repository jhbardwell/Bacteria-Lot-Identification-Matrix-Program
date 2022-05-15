from tkinter import*


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

        self.raf_option = StringVar()

        self.sal_option = StringVar()

        self.sorb_option = StringVar()

        self.suc_option = StringVar()

        self.xyl_option = StringVar()

        self.salt_option = StringVar()

        self.temp_option = StringVar()


        #top-level menu
        def donothing():
            filewin = Toplevel(background="red")
            button = Button(filewin, text="Do nothing button")
            button.pack(side=LEFT, expand=NO,  padx=10, pady=5, ipadx=5, ipady=5)
            filewin.title("Nothing")



        menubar = Menu(root, background="blue", foreground="white")


        datamenu = Menu(menubar, background="blue", foreground="white", tearoff=0)
        datamenu.add_command(label="Guidelines", command=donothing)
        datamenu.add_separator()
        datamenu.add_command(label="Search", command=donothing)
        menubar.add_cascade(label="Bacteria Database", menu=datamenu)

        labmenu = Menu(menubar, background="blue", foreground="white", tearoff=0)
        labmenu.add_command(label="Lab Safety", command=donothing)
        labmenu.add_separator()
        labmenu.add_command(label="Colony Counts", command=donothing)
        labmenu.add_separator()
        labmenu.add_command(label="Gram Stain", command=donothing)
        labmenu.add_command(label="Fluid Thio", command=donothing)
        labmenu.add_command(label="SIM", command=donothing)
        labmenu.add_command(label="Catalase", command=donothing)
        labmenu.add_command(label="Oxidase", command=donothing)
        labmenu.add_command(label="Citrate", command=donothing)
        labmenu.add_command(label="Fermentation", command=donothing)
        menubar.add_cascade(label="Lab Procedure", menu=labmenu)

        helpmenu = Menu(menubar, background="blue", foreground="white", tearoff=0)
        helpmenu.add_command(label="Making Plates", command=donothing)
        helpmenu.add_separator()
        helpmenu.add_command(label="MAC", command=donothing)
        helpmenu.add_command(label="MSA", command=donothing)
        helpmenu.add_command(label="SS", command=donothing)
        helpmenu.add_command(label="TSA", command=donothing)
        menubar.add_cascade(label="Agar Selection", menu=helpmenu)

        root.config(menu=menubar)


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
        Label(self.heading_frame, text="TEST OPTIONS", font=8, justify=CENTER).pack(side=TOP, anchor=N)
        Label(self.heading_frame, justify=LEFT).pack(side=TOP, anchor=W)

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
        self.main_right_frame = Frame(self.myContainer1, background="white") 
        self.main_right_frame.pack(side=RIGHT, expand=NO, fill=BOTH)

        # id frame
        self.id_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.id_frame.pack(expand=NO, fill=BOTH)
        Label(self.id_frame, text="IDENTIFICATION \n", font=8, background="white").pack(side=TOP,anchor=N)


        gram_options = ["+", "--"]
        shape_options = ["bacillus", "coccus", "spirillus"]
        meta_options = ["aerobe", "fac anaerobe"]
        cat_options = ["+", "--"]
        oxi_options = ["+", "--"]
        endo_options = ["+", "--"]
        motil_options = ["+", "--"]
        h2s_options = ["+", "--"]
        ind_options = ["+", "--"]
        cit_options = ["+", "--"]
        nit_options = ["+", "--"]
        urea_options = ["+", "--"]
        glu_options = ["+", "--"]
        arab_options = ["+", "--"]
        glyc_options = ["+", "--"]
        lac_options = ["+", "--"]
        man_options = ["+", "--"]
        raf_options = ["+", "--"]
        sal_options = ["+", "--"]
        sorb_options = ["+", "--"]
        suc_options = ["+", "--"]
        xyl_options = ["+", "--"]
        salt_options = ["<6%", "6-8%", ">8%"]
        temp_options = ["25C", "35C", "45C"] 


        self.gram_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.gram_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.gram_options_frame, text="GRAM STAIN:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.shape_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.shape_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.shape_options_frame, text="SHAPE:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.meta_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.meta_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.meta_options_frame, text="METABOLISM:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.cat_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.cat_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.cat_options_frame, text="CATALASE:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.oxi_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.oxi_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.oxi_options_frame, text="OXIDASE:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.endo_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.endo_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.endo_options_frame, text="ENDOSPORE:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.motil_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.motil_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.motil_options_frame, text="MOTILITY:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.h2s_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.h2s_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.h2s_options_frame, text="HYDROGEN SULFIDE:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.ind_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.ind_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.ind_options_frame, text="INDOLE:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.cit_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.cit_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.cit_options_frame, text="CITRATE:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.nit_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.nit_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.nit_options_frame, text="NITRATE", relief=RAISED).pack(side=LEFT,anchor=W)

        self.urea_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.urea_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.urea_options_frame, text="UREA HYDROL:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.glu_options_frame = Frame(self.control_left_frame, borderwidth=5)
        self.glu_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.glu_options_frame, text="GLUCOSE FERM:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.arab_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.arab_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.arab_options_frame, text="ARABINOSE FERM:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.glyc_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.glyc_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.glyc_options_frame, text="GLYCEROL FERM:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.lac_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.lac_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.lac_options_frame, text="LACTOSE FERM:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.man_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.man_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.man_options_frame, text="MANNITOL FERM:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.raf_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.raf_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.raf_options_frame, text="RAFFINOSE FERM:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.sal_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.sal_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.sal_options_frame, text="SALICIN FERM:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.sorb_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.sorb_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.sorb_options_frame, text="SORBITOL FERM:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.suc_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.suc_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.suc_options_frame, text="SUCROSE FERM:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.xyl_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.xyl_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.xyl_options_frame, text="XYLOSE FERM:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.salt_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.salt_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.salt_options_frame, text="SALINITY RANGE:", relief=RAISED).pack(side=LEFT,anchor=W)

        self.temp_options_frame = Frame(self.control_right_frame, borderwidth=5)
        self.temp_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.temp_options_frame, text="TEMP RANGE:", relief=RAISED).pack(side=LEFT,anchor=W)


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

        for option in raf_options:
            button = Radiobutton(self.raf_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.raf_option)
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
            value=option,  padx=5, variable=self.suc_option)
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


        # identify button

        self.idbutton = Button(self.bottom_frame,text="Identify", background="white",
        width=button_width, padx=button_padx, pady=button_pady)

        self.idbutton.pack(side=LEFT)

        self.idbutton.bind("<Button-1>", self.id_click)
        self.idbutton.bind("<Return>", self.id_click)


        # reset button

        self.resetbutton = Button(self.bottom_frame,text="Reset", background="white",
        width=button_width, padx=button_padx, pady=button_pady)

        self.resetbutton.pack(side=RIGHT)

        self.resetbutton.bind("<Button-1>", self.resetbuttonclick)
        self.resetbutton.bind("<Return>", self.resetbuttonclick)


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
        self.raf_option.set("raf")
        self.sal_option.set("sal")
        self.sorb_option.set("sorb")
        self.suc_option.set("suc")
        self.xyl_option.set("xyl")
        self.salt_option.set("salt")
        self.temp_option.set("temp")

        self.id_frame.destroy()
        self.id_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.id_frame.pack(side=TOP, fill=BOTH)
        Label(self.id_frame, text="IDENTIFICATION \n", font=8, background="white").pack(side=TOP,anchor=N)

        self.graphics_frame.destroy()
        self.graphics_frame = Frame(self.main_right_frame, background="light blue",borderwidth=5, relief=RIDGE)
        self.graphics_frame.pack(side=BOTTOM, expand=YES, fill=BOTH)



    def id_click(self):

        self.id_frame.destroy()
        self.id_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.id_frame.pack(side=TOP, fill=BOTH)
        Label(self.id_frame, text="IDENTIFICATION \n", font=8, background="white").pack(side=TOP,anchor=N)

       
        if (self.gram_option.get()==("--") and
            self.shape_option.get()==("bacillus") and
            self.meta_option.get()==("fac anaerobe")):
            Label(self.id_frame, text = id, background = "white").pack(side=TOP, anchor = W)
        else: Label(self.id_frame, text = "Error: need more data", background = "white").pack(side=TOP, anchor = N)


 
root = Tk()
root.title("Freshwater Bacteria Compilation")
myapp = MyApp(root)
#root.withdraw()
root.mainloop()
