from Tkinter import*
from operator import*

class MyApp:
    def __init__(self, parent):


        # variables
        self.ala_option = StringVar()
        self.algo_option = StringVar()
        self.arab_option = StringVar()
        self.arg_option = StringVar()
        self.asp_option = StringVar()
        self.cas_option = StringVar()
        self.cat_option = StringVar()
        self.cit_option = StringVar()
        self.CI_option = StringVar()
        self.dul_option = StringVar()
        self.endo_option = StringVar()
        self.esc_option = StringVar()
        self.fru_option = StringVar()
        self.gel_option = StringVar()
        self.glu_option = StringVar()
        self.glut_option = StringVar()
        self.glyc_option = StringVar()
        self.gram_option = StringVar()
        self.group_option = StringVar()
        self.h2s_option = StringVar()
        self.hip_option = StringVar()
        self.hist_option = StringVar()
        self.ind_option = StringVar()
        self.ino_option = StringVar()
        self.lac_option = StringVar()
        self.lys_option = StringVar()
        self.mal_option = StringVar()
        self.man_option = StringVar()
        self.meta_option = StringVar()
        self.motil_option = StringVar()
        self.nit1_option = StringVar()
        self.nit2_option = StringVar()        
        self.orn_option = StringVar()
        self.oxi_option = StringVar()
        self.phen_option = StringVar()
        self.raf_option = StringVar()
        self.rham_option = StringVar()
        self.sal_option = StringVar()
        self.salt_option = StringVar()
        self.shape_option  = StringVar()
        self.sorb_option = StringVar()
        self.starch_option = StringVar()
        self.suc_option = StringVar()
        self.temp_option = StringVar()
        self.tre_option = StringVar()
        self.urea_option = StringVar()
        self.val_option = StringVar()
        self.xyl_option = StringVar()
  
    
        #top-level menu (and menu-selection definitions)

        def donothing():
            filewin = Toplevel(background="red")
            button = Button(filewin, text="Do nothing button")
            button.pack(side=LEFT, expand=NO, padx=10, pady=5, ipadx=5, ipady=5)
            filewin.title("Nothing")
    
        def intronothing():
            filewin = Toplevel(background="yellow")
            Label(filewin, text=". . .\n \
            Welcome to the wonderful world of freshwater bacteria identification without DNA samples. \n\n \
            This database includes over 300 common taxa likely found in lotic or lentic environments. \n \
            Any inland habitat with dirt, oxygen, and water! \n \n \
            This compilation does not include protozoa, plankton, pathogens, halophiles, thermophiles, anaerobes, \n \
            bacteria which cannot be lab cultured, or require special nutrients and conditions for growth. \n \
            Bacteria strains are variable, constantly mutating, and individual test results may not provide an exact match. \n \
            Several taxonomic splits after 1995 are missing or unavailable: email suggestions and test updates.   \n \n \
            Enter the phenotypic test results of an unidentified bacteria colony. \n \
            Use 'Identify' to display bacteria which best match your current results and 'Reset' to clear the slate. \n \
            Instructions on how to run and interpret these tests is available in the top menu \n \
            along with the option to search the database for phenotypic traits of a known bacterium. \n \
            All tests performed on 48 hour old colony cultures except gram stains (24hr) and endospore tests (1 week)\n \
            For any given test per taxa, > 85% success scores + , < 15% success scores --, and those in between are unscored. \n \n \
            This program is freeware published and distributed under the GNU public license.  Please credit author. \n \n \
            - Jeff Bardwell, 2012 \n \
              (mudnwater@yahoo.com)\n\n\n", justify=LEFT, font=10, background="yellow", foreground="dark green").pack()
            filewin.title("Freshwater Bacteria Compilation v 1.0")


        def searchnothing():
            filewin = Toplevel(background="dark green")
            
            guess = StringVar()
            Entry(filewin, textvariable=guess).pack(side=LEFT, expand=NO, padx=5, pady=5, ipadx=5, ipady=5)
            
            self.searchbutton = Button(filewin, text="Search",
            width=6, padx="2m", pady="1m")
            self.searchbutton.pack(side=LEFT, pady=5)
            self.searchbutton.bind("<Button-1>", self.searchbuttonclick)
            self.searchbutton.bind("<Return>", self.searchbuttonclick)
        
            filewin.title("Search Database")
 
        def referencenothing():
            filewin = Toplevel(background="white")

            Label(filewin, text=". . .\n \
        Acidophilium \n\
                Wichlacz,P.L., Unz,R.F., Langworthy,T.A. 1986. Acidiphilium angustum sp. nov. Acidiphilium facilis sp. nov. and Acidiphilium vubrum sp. nov. : \n\
                    Acidophilic Heterotrophic Bacteria Isolated from Acidic Coal Mine DrainageInt J Syst Bacteriol 36:197-201. \n\
        Acinetobacter \n\
                Bouvet,P.J.M., Grimont,P.A.D. 1986. Taxonomy of the Genus Acinetobacter with the Recognition of Acinetobacter baumannii sp. nov. Acinetobacter haemolyticus sp. \n\
                    nov. Acinetobacter johnsonii sp. nov. and Acinetobacter junii sp. nov. and Emended Descriptions of Acinetobacter calcoaceticus and Acinetobacter lwofii. \n\
                    Int J Syst Bacteriol 36:228-240. \n\
                Gerner-Smidt,P., Tjernberg,I., Ursing,J. J 1991. Reliability of Phenotypic Tests for Identification of Acinetobacter Species. Clin Microbiol 29:277-282. \n\
        Aeromonas \n\
                Janda,J.M., Abbott,S.L. 2010. The Genus Aeromonas: Taxonomy, Pathogenicity, and Infection. Clin Microbiol Rev 23:35-73. \n\
        Chromobacterium \n\
                Kaufman,S.C., Ceraso,D., Schugurensky,A. 1986. First Case Report from Argentina of Fatal Septicemia Caused by Chromobacterium violaceum. J Clin Microbiol 23:956-948. \n\
                Lee,J., Kim,J.S., Nahm,C.H., Choi,J.W., Kim,J., Pai,S.H. 1999. Two Cases of Chromobacterium violaceum Infection after Injury in a Subtropical Region. \n\
                    J Clin Microbiol 37:2068-2070. \n\
        Citrobacter \n\
                Bardiya,N., Jae-Ho,B. 2004. Role of Citrobacter amalonaticus and Citrobacter farmeri in dissimilatory perchlorate reduction. J Basic Microbiol 44:88-97. \n\
                Brenner,D.J., O'Hara,C.M., Grimont,A.D., Janda,M.L., Falsen,E., Aldova,E., Ageron,E., Schindler,J. 1999. Biochemical Identification of Citrobacter Species \n\
                    Defined by DNA Hybridization and Description of Citrobacter gillenii sp. nov. (Formerly Citrobacter Genomospecies 10) and Citrobacter murliniae sp. nov. \n\
                    (Formerly Citrobacter Genomospecies 11). J Clin Microbiol 37:2619-2624. \n\
        Deinobacter \n\
                Oyaizu,H., Stackebrandt,E., Schleifer,K.H., Ludwig,W., Pohla,H., Ito,H., Hirata,A., Oyaizu,Y., Komagata,K. 1987. A Radiation-Resistant Rod-Shaped Bacterium, \n\
                    Deinobacter grandisgen. nov., sp. nov., with Peptidoglycan Containing Ornithine Int J Syst Bacteriol 37:62-67. \n\
        Erwinia \n\
                Hao,M.V., Brenner,D.J., Steigerwalt,A.G., Kosako,Y., Komagata,K. 1990. Erwinia persicinus, a New Species Isolated from Plants. Int J Syst Bacteriol 40:379-383. \n\
                Kwon,S., Go,S., Kang,H., Ryu,J., Jo,J. 1997. Phylogenetic Analysis of Erwinia Species Based on 16s rRNA Gene Sequences. Int J Syst Bacteriol 47:1061-1067. \n\
                Mergaert,J., Hauben,L., Cnockaert,M.C., Swings,J. Int J Syst Bacteriol 1999. Reclassification of non-pigmented Erwinia herbicola strains from trees as Ennrinia \n\
                    billingiae sp. nov.. 49:377-383. \n\
                Verdonck,L., Mergaert,J., Rijckaert,C., Swings,J., Kersters,K., De Ley,J. 1987. Genus Erwinia: Numerical Analysis of Phenotypic Features. Int J System Bacteriol 37:4-18. \n\
        Pantoea \n\
                De Baere,T., Verhelst,R., Labit, C., Verschraegen,G., Wauters,G. Claeys,G., Vaneechoutte,M. 2004. Bacteremic Infection with Pantoea ananatis. J Clin Microbiol 42:4393-4395. \n\
                Mergaert,J., Verdonck,L., Kersters,K. 1993. Transfer of Erwinia ananas (synonym, Erwinia uredovora) and Erwinia stewartii to the Genus Pantoea emend. as Pantoea \n\
                    ananas (Serrano 1928) comb. nov. and Pantoea stewartii(Smith 1898) comb, nov., Respectively, and Description of Pantea stewartii subsp. indologenes subsp. nov. \n\
                    Int J Syst Bacteriol 43:162-173. \n\
        Pectobacterium \n\
                Gardan,L., Gouy,C., Christen,R., Samson,R. 2003. Elevation of three subspecies of Pectobacterium carotovorum to species level: Pectobacterium atrosepticum sp. nov., \n\
                    Pectobacterium betavasculorum sp. nov. and Pectobacterium wasabiae sp. nov. Int J Syst Evol Microbiol 53:381-391. \n\
        Rahnella \n\
                  Verdonck,L., Mergaert,J., Rijckaert,C., Swings,J., Kersters,K., De Ley,J. 1987. Genus Erwinia: Numerical Analysis of Phenotypic Features. Int J System Bacteriol 37:4-18. \n\n",
            justify=LEFT, background="white", foreground="black", wraplength=1000).pack()
            filewin.title("References")

        menubar = Menu(root)

        intromenu = Menu(menubar, tearoff=0)
        intromenu.add_command(label="Read Me", command=intronothing)
        intromenu.add_command(label="Credits", command=donothing)        
        menubar.add_cascade(label="Introduction", menu=intromenu)

        datamenu = Menu(menubar, tearoff=0)
        datamenu.add_command(label="Search", command=searchnothing)
        datamenu.add_command(label="References", command=referencenothing)
        menubar.add_cascade(label="Bacteria Database", menu=datamenu)

        labmenu = Menu(menubar, tearoff=0)
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
        labmenu.add_command(label="Nitrate Reduction", command=donothing) 
        labmenu.add_command(label="Fermentation, Sugar", command=donothing)       
        labmenu.add_command(label="Amino Acid, Enzymes", command=donothing)
        labmenu.add_command(label="Hydrolysis", command=donothing)       
        menubar.add_cascade(label="Lab Procedure", menu=labmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Making Plates", command=donothing)
        helpmenu.add_separator()
        helpmenu.add_command(label="MAC", command=donothing)
        helpmenu.add_command(label="MSA", command=donothing)
        helpmenu.add_command(label="SS", command=donothing)
        helpmenu.add_command(label="TSA", command=donothing)
        menubar.add_cascade(label="Agar Selection", menu=helpmenu)

        analysismenu = Menu(menubar, tearoff=0)
        analysismenu.add_command(label="Statistics", command=donothing)
        analysismenu.add_separator()
        analysismenu.add_command(label="Bayes Theorem", command=donothing)
        analysismenu.add_command(label="Additive Probability", command=donothing)
        analysismenu.add_command(label="Geometric Mean", command=donothing)
        analysismenu.add_command(label="Correlation", command=donothing)
        menubar.add_cascade(label="Analysis", menu=analysismenu)

        root.config(menu=menubar)




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
        self.control_frame.pack(side=TOP, expand=YES, padx=2, pady=2, ipadx=2, ipady=2)

        # control_left_frame
        self.control_left_frame = Frame(self.control_frame, background="light blue")
        self.control_left_frame.pack(side=LEFT, anchor=N, expand=YES, padx=2, pady=2, ipadx=2, ipady=2)

        # control_center_frame
        self.control_center_frame = Frame(self.control_frame, background="light blue")
        self.control_center_frame.pack(side=LEFT, anchor=N, expand=YES, padx=2, pady=2, ipadx=2, ipady=2)

        # control_right_frame
        self.control_right_frame = Frame(self.control_frame, background="light blue")
        self.control_right_frame.pack(side=LEFT, anchor=N, expand=YES, fill=X, padx=2, pady=2, ipadx=2, ipady=2)

        # main right frame
        self.main_right_frame = Frame(self.myContainer1, background="white") 
        self.main_right_frame.pack(side=RIGHT, expand=YES, fill=BOTH)

        # algorithm frame
        self.algo_frame = Frame(self.main_right_frame, borderwidth=5, background="light gray")
        self.algo_frame.pack(expand=NO, fill=BOTH)
        Label(self.algo_frame, text="ANALYSIS", font=8, background="light gray").pack(side=TOP,anchor=N)

        self.algo_left_frame = Frame(self.algo_frame, borderwidth=5, background="light gray")
        self.algo_left_frame.pack(side=TOP, anchor=E, expand=NO, fill=BOTH)
        algo_options = ["Additive Probability", "Geometric Mean", "Bayes Theorem", "Correlation"]
        for option in algo_options:
            button = Radiobutton(self.algo_left_frame, text=str(option), indicatoron=1,
            value=option, padx=5, variable=self.algo_option, background="light gray")
            button.pack(side=TOP, anchor=W)

        self.algo_option.set("Bayes Theorem")

        self.algo_right_frame = Frame(self.algo_frame, borderwidth=5, background="light gray")
        self.algo_right_frame.pack(side=BOTTOM, anchor=N, expand=NO, fill=BOTH)
        Label(self.algo_right_frame, text="Confidence Interval", font=8, background="light gray").pack(side=TOP,anchor=N)
        CI_options = ["0.99", "0.95", "0.90"]
        for option in CI_options:
            button = Radiobutton(self.algo_right_frame, text=str(option), indicatoron=1,
            value=option, padx=5, variable=self.CI_option, background="light gray")
            button.pack(side=LEFT, anchor=N)

        self.CI_option.set("0.95")
        
        # heading frame
        self.heading_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.heading_frame.pack(expand=NO)
        Label(self.heading_frame, text="            IDENTIFICATION             ", font=8, background="white").pack(side=TOP,anchor=N)
        
        # id frame
        self.id_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.id_frame.pack(expand=NO, fill=BOTH)










        # test result radiobuttons
        ala_options = ["+", "--", "?"]
        arab_options = ["+", "--", "?"]
        arg_options = ["+", "--", "?"]
        asp_options = ["+", "--", "?"]
        cas_options = ["+", "--", "?"]
        cat_options = ["+", "--", "?"]
        cit_options = ["+", "--", "?"]
        dul_options = ["+", "--", "?"]
        endo_options = ["+", "--", "?"]
        esc_options = ["+", "--", "?"]
        fru_options = ["+", "--", "?"]
        gel_options = ["+", "--", "?"]
        glu_options = ["+", "--", "?"]
        glut_options = ["+", "--", "?"]
        glyc_options = ["+", "--", "?"]
        gram_options = ["+", "--", "?"]
        h2s_options = ["+", "--", "?"]
        hip_options = ["+", "--", "?"]
        hist_options = ["+", "--", "?"]
        ind_options = ["+", "--", "?"]
        ino_options = ["+", "--", "?"]
        lac_options = ["+", "--", "?"]
        lys_options = ["+", "--", "?"]
        mal_options = ["+", "--", "?"]
        man_options = ["+", "--", "?"]
        meta_options = ["aerobe", "fac anaerobe", "?"]
        motil_options = ["+", "--", "?"]
        nit1_options = ["+", "--", "?"]
        nit2_options = ["+", "--", "?"]        
        orn_options = ["+", "--", "?"]
        oxi_options = ["+", "--", "?"]
        phen_options = ["+", "--", "?"]
        raf_options = ["+", "--", "?"]
        rham_options = ["+", "--", "?"]
        sal_options = ["+", "--", "?"]
        salt_options = ["<6%", ">6%", "?"]
        shape_options = ["bacillus", "coccus", "spirillus", "?"]
        sorb_options = ["+", "--", "?"]
        starch_options = ["+", "--", "?"]
        suc_options = ["+", "--", "?"]
        temp_options = ["25C", "35C", "45C", "?"] 
        tre_options = ["+", "--", "?"]
        urea_options = ["+", "--", "?"]
        val_options = ["+", "--", "?"]
        xyl_options = ["+", "--", "?"]


    
        
        self.gram_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.gram_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.gram_options_frame, text="GRAM STAIN:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in gram_options:
            button = Radiobutton(self.gram_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.gram_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
       
        self.shape_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.shape_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.shape_options_frame, text="SHAPE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in shape_options:
            button = Radiobutton(self.shape_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.shape_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.meta_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.meta_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.meta_options_frame, text="METABOLISM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in meta_options:
            button = Radiobutton(self.meta_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.meta_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
    
        self.endo_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.endo_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.endo_options_frame, text="ENDOSPORE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in endo_options:
            button = Radiobutton(self.endo_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.endo_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
    
        self.cat_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.cat_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.cat_options_frame, text="CATALASE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in cat_options:
            button = Radiobutton(self.cat_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.cat_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
    
        self.oxi_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.oxi_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.oxi_options_frame, text="OXIDASE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in oxi_options:
            button = Radiobutton(self.oxi_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.oxi_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.salt_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.salt_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.salt_options_frame, text="SALINITY RANGE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in salt_options:
            button = Radiobutton(self.salt_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.salt_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.temp_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.temp_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.temp_options_frame, text="TEMP RANGE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in temp_options:
            button = Radiobutton(self.temp_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.temp_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.motil_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.motil_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.motil_options_frame, text="MOTILITY:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in motil_options:
            button = Radiobutton(self.motil_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.motil_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.h2s_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.h2s_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.h2s_options_frame, text="HYDROGEN SULFIDE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in h2s_options:
            button = Radiobutton(self.h2s_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.h2s_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.ind_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.ind_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.ind_options_frame, text="INDOLE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in ind_options:
            button = Radiobutton(self.ind_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.ind_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
    
        self.cit_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.cit_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.cit_options_frame, text="CITRATE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in cit_options:
            button = Radiobutton(self.cit_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.cit_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
    
        self.nit1_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.nit1_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.nit1_options_frame, text="NO3->NO2:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in nit1_options:
            button = Radiobutton(self.nit1_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.nit1_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.nit2_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.nit2_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.nit2_options_frame, text="NO3->NO2->N2:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in nit2_options:
            button = Radiobutton(self.nit2_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.nit2_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.glu_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.glu_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.glu_options_frame, text="GLUCOSE FERM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in glu_options:
            button = Radiobutton(self.glu_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.glu_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
    
        self.arab_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.arab_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.arab_options_frame, text="ARABINOSE FERM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in arab_options:
            button = Radiobutton(self.arab_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.arab_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
    
        self.dul_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.dul_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.dul_options_frame, text="DULCITOL FERM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in dul_options:
            button = Radiobutton(self.dul_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.dul_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.fru_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.fru_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.fru_options_frame, text="FRUCTOSE FERM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in fru_options:
            button = Radiobutton(self.fru_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.fru_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.glyc_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.glyc_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.glyc_options_frame, text="GLYCEROL FERM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in glyc_options:
            button = Radiobutton(self.glyc_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.glyc_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.ino_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.ino_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.ino_options_frame, text="INOSITOL FERM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in ino_options:
            button = Radiobutton(self.ino_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.ino_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.lac_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.lac_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.lac_options_frame, text="LACTOSE FERM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in lac_options:
            button = Radiobutton(self.lac_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.lac_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.mal_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.mal_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.mal_options_frame, text="MALTOSE FERM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in mal_options:
            button = Radiobutton(self.mal_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.mal_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.man_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.man_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.man_options_frame, text="MANNITOL FERM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in man_options:
            button = Radiobutton(self.man_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.man_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.raf_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.raf_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.raf_options_frame, text="RAFFINOSE FERM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in raf_options:
            button = Radiobutton(self.raf_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.raf_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.rham_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.rham_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.rham_options_frame, text="RHAMNOSE FERM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in rham_options:
            button = Radiobutton(self.rham_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.rham_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.sal_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.sal_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.sal_options_frame, text="SALICIN FERM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in sal_options:
            button = Radiobutton(self.sal_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.sal_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.sorb_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.sorb_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.sorb_options_frame, text="SORBITOL FERM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in sorb_options:
            button = Radiobutton(self.sorb_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.sorb_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.suc_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.suc_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.suc_options_frame, text="SUCROSE FERM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in suc_options:
            button = Radiobutton(self.suc_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.suc_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.tre_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.tre_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.tre_options_frame, text="TREHALOSE FERM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in tre_options:
            button = Radiobutton(self.tre_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.tre_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.xyl_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.xyl_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.xyl_options_frame, text="XYLOSE FERM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in xyl_options:
            button = Radiobutton(self.xyl_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.xyl_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.ala_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.ala_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.ala_options_frame, text="ALANINE ENZYM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in ala_options:
            button = Radiobutton(self.ala_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.ala_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.arg_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.arg_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.arg_options_frame, text="ARGININE ENZYM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in arg_options:
            button = Radiobutton(self.arg_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.arg_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.asp_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.asp_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.asp_options_frame, text="ASPARAGINE ENZYM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in asp_options:
            button = Radiobutton(self.asp_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.asp_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
    
        self.glut_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.glut_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.glut_options_frame, text="GLUTAMIC ACID ENZYM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in glut_options:
            button = Radiobutton(self.glut_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.glut_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
    
        self.hist_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.hist_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.hist_options_frame, text="HISTIDINE ENZYM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in hist_options:
            button = Radiobutton(self.hist_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.hist_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.lys_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.lys_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.lys_options_frame, text="LYSINE ENZYM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in lys_options:
            button = Radiobutton(self.lys_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.lys_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
    
        self.orn_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.orn_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.orn_options_frame, text="ORNITHINE ENZYM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in orn_options:
            button = Radiobutton(self.orn_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.orn_option, background="light blue")
            button.pack(side=LEFT, anchor=E) 
    
        self.phen_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.phen_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.phen_options_frame, text="PHENYLALANINE ENZYM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in phen_options:
            button = Radiobutton(self.phen_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.phen_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
        
        self.val_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.val_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.val_options_frame, text="VALINE ENZYM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in val_options:
            button = Radiobutton(self.val_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.val_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
        
        self.cas_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.cas_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.cas_options_frame, text="CASEIN HYDROL:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in cas_options:
            button = Radiobutton(self.cas_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.cas_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.esc_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.esc_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.esc_options_frame, text="ESCULIN HYDROL:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in esc_options:
            button = Radiobutton(self.esc_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.esc_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.gel_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.gel_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.gel_options_frame, text="GELATIN HYDROL:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in gel_options:
            button = Radiobutton(self.gel_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.gel_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.hip_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.hip_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.hip_options_frame, text="HIPPURATE HYDROL:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in hip_options:
            button = Radiobutton(self.hip_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.hip_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.starch_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.starch_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.starch_options_frame, text="STARCH HYDROL:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in starch_options:
            button = Radiobutton(self.starch_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.starch_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.urea_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.urea_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.urea_options_frame, text="UREA HYDROL:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in urea_options:
            button = Radiobutton(self.urea_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.urea_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        
        # identify button

        self.idbutton = Button(self.bottom_frame,text="Identify", background="dark green", foreground="white",
        width=6, padx="2m", pady="1m")

        self.idbutton.pack(side=LEFT)

        self.idbutton.bind("<Button-1>", self.idbuttonclick)
        self.idbutton.bind("<Return>", self.idbuttonclick)


        # reset button

        self.resetbutton = Button(self.bottom_frame,text="Reset", background="red", foreground="white",
        width=6, padx="2m", pady="1m")

        self.resetbutton.pack(side=RIGHT)

        self.resetbutton.bind("<Button-1>", self.resetbuttonclick)
        self.resetbutton.bind("<Return>", self.resetbuttonclick)


        # default button settings
        
        self.ala_option.set("?")
        self.arab_option.set("?")
        self.arg_option.set("?")
        self.asp_option.set("?")
        self.cas_option.set("?")
        self.cat_option.set("?")
        self.cit_option.set("?")
        self.dul_option.set("?")
        self.endo_option.set("?")
        self.esc_option.set("?")
        self.fru_option.set("?")        
        self.gel_option.set("?")
        self.glu_option.set("?")
        self.glut_option.set("?")
        self.glyc_option.set("?")
        self.gram_option.set("?")
        self.h2s_option.set("?")
        self.hip_option.set("?")
        self.hist_option.set("?")
        self.ind_option.set("?")
        self.ino_option.set("?")
        self.lac_option.set("?")
        self.lys_option.set("?")
        self.mal_option.set("?")
        self.man_option.set("?")
        self.meta_option.set("?")
        self.motil_option.set("?")
        self.nit1_option.set("?")
        self.nit2_option.set("?")
        self.orn_option.set("?")
        self.oxi_option.set("?")
        self.phen_option.set("?")
        self.raf_option.set("?")
        self.rham_option.set("?")
        self.sal_option.set("?")
        self.salt_option.set("?")
        self.shape_option.set("?")
        self.sorb_option.set("?")
        self.starch_option.set("?")
        self.suc_option.set("?")
        self.temp_option.set("?")
        self.tre_option.set("?")
        self.urea_option.set("?")
        self.val_option.set("?")
        self.xyl_option.set("?")
    
    def searchbuttonclick(self):
    
        nothing
        
    
    def resetbuttonclick(self, event):

        self.ala_option.set("?")
        self.arab_option.set("?")
        self.arg_option.set("?")
        self.asp_option.set("?")
        self.cas_option.set("?")
        self.cat_option.set("?")
        self.cit_option.set("?")
        self.dul_option.set("?")
        self.endo_option.set("?")
        self.esc_option.set("?")
        self.fru_option.set("?")        
        self.gel_option.set("?")
        self.glu_option.set("?")
        self.glut_option.set("?")
        self.glyc_option.set("?")
        self.gram_option.set("?")
        self.h2s_option.set("?")
        self.hip_option.set("?")
        self.hist_option.set("?")
        self.ind_option.set("?")
        self.ino_option.set("?")
        self.lac_option.set("?")
        self.lys_option.set("?")
        self.mal_option.set("?")
        self.man_option.set("?")
        self.meta_option.set("?")
        self.motil_option.set("?")
        self.nit1_option.set("?")
        self.nit2_option.set("?")
        self.orn_option.set("?")
        self.oxi_option.set("?")
        self.phen_option.set("?")
        self.raf_option.set("?")
        self.rham_option.set("?")
        self.sal_option.set("?")
        self.salt_option.set("?")
        self.shape_option.set("?")
        self.sorb_option.set("?")
        self.starch_option.set("?")
        self.suc_option.set("?")
        self.temp_option.set("?")
        self.tre_option.set("?")
        self.urea_option.set("?")
        self.val_option.set("?")
        self.xyl_option.set("?")
        
        self.id_frame.destroy()
        self.id_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.id_frame.pack(side=TOP, fill=BOTH)


    def idbuttonclick(self, event):

        self.id_frame.destroy()
        self.id_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.id_frame.pack(side=TOP, fill=BOTH)

        bac={}

        x=0.50
        
        if (self.gram_option.get()=="?" or
        self.shape_option.get()=="?" or
        self.meta_option.get()=="?" or
        self.endo_option.get()=="?" or
        self.cat_option.get()=="?" or
        self.oxi_option.get()=="?"):
            Label(self.id_frame, text = "Error: need more data \n", background = "white").pack(side=TOP, anchor = N)

        if (self.gram_option.get()=="--" and
        self.shape_option.get()=="bacillus" and
        self.meta_option.get()=="aerobe" and
        self.endo_option.get()=="--" and
        self.cat_option.get()=="+" and
        self.oxi_option.get()=="--"):
            Label(self.id_frame, text = "Gram Negative \n Aerobe Bacillus \n", background = "white").pack(side=TOP, anchor = N)
            bac=[
            ('Acinetobacter baumannii/calcoaceticus complex',0.99,0.01,0.01,0.01,0.01,0.99,0.01,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x),
            ('Acinetobacter haemolyticus',0.99,0.01,0.01,0.01,0.01,0.91,0.01,0.01,0.52,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.96,x,x,x),
            ('Acinetobacter junii',0.99,0.01,0.01,0.01,0.01,0.82,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x),
            ('Acinetobacter sp 6',0.99,0.01,0.01,0.01,0.01,0.99,0.01,0.01,0.66,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x),
            ('Acinetobacter johnsonii',0.99,0.01,0.01,0.01,0.01,0.99,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x),
            ('Acinetobacter lwoffii',0.99,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.06,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x),
            ('Acinetobacter sp 10',0.99,0.01,0.01,0.01,0.01,0.99,0.01,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x),
            ('Acinetobacter sp 11',0.99,0.01,0.01,0.01,0.01,0.99,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x),
            ('Acinetobacter sp 12',0.99,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.33,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x),
            ('Deinobacter grandis',0.99,0.01,0.01,0.01,0.01,x,0.99,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,0.99,x,0.99,0.01),
            ('Flavimonas oryzihabitans',0.99,0.01,x,0.01,0.01,0.99,0.01,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,0.01,x)]

        if (self.gram_option.get()=="--" and
        self.shape_option.get()=="bacillus" and
        self.meta_option.get()=="aerobe" and
        self.endo_option.get()=="--" and
        self.cat_option.get()=="+" and
        self.oxi_option.get()=="+"):
            Label(self.id_frame, text = "Gram Negative \n Aerobe Bacillus \n", background = "white").pack(side=TOP, anchor = N)
            bac=[
            ('Acidovorax',0.99,0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Alcaligenes',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Argobacterium',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Argomonas',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Azobacter',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Azomonas',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Comamonas',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Cupriavidis',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Ensifer',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Flavobacterium',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Hydrogenophila',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Pseudomonas',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Rhizobacter',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Roseomonas',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Serpens',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Shingobacterium',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Variovorax',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Zoogloea',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)]

        if (self.gram_option.get()=="--" and
        self.shape_option.get()=="bacillus" and
        self.meta_option.get()=="fac anaerobe" and
        self.endo_option.get()=="--" and
        self.cat_option.get()=="+" and
        self.oxi_option.get()=="--"):
            Label(self.id_frame, text = "Gram Negative \n Facultative Anaerobe Bacillus \n", background = "white").pack(side=TOP, anchor = N)
            # cat   oxi     motil   h2s     ind     cit     nit1    nit2    glu     arab    dul     fru     glyc    ino     lac     mal     man     raf     rham    sal     sorb    suc     tre     xyl     ala     arg     asp     glut    hist    lys     orn     phen    val     cas     esc     gel     hip     stch    urea   
            bac=[
            ('Budvicia aquatica',0.99,0.01,0.51,0.83,0.01,0.01,0.99,0.01,0.99,0.83,0.01,x,0.01,0.01,0.83,0.01,0.51,0.01,0.99,0.01,0.01,0.01,0.01,0.99,x,0.01,x,x,x,0.01,0.01,0.01,x,x,0.01,0.01,x,x,0.51),
            ('Buttiauxella agrestis',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.51,0.01,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.01,0.99,0.99,x,0.01,x,x,x,0.01,0.99,0.01,x,x,0.99,0.01,x,x,0.01),
            ('Citrobacter amalonaticus',0.99,0.01,0.83,0.18,0.99,0.99,0.99,0.01,0.99,0.99,0.01,x,0.51,0.01,0.51,0.99,0.99,0.01,0.99,0.18,0.99,0.01,0.99,0.99,x,0.83,x,x,x,0.01,0.99,0.01,x,x,0.01,0.01,x,x,0.83),
            ('Citrobacter braakii',0.99,0.01,0.83,0.51,0.18,0.83,0.99,0.01,0.99,x,0.51,x,0.99,x,0.83,x,x,0.18,x,0.01,x,0.18,x,x,x,0.51,x,x,x,x,x,x,x,x,0.01,x,x,x,0.51),
            ('Citrobacter farmeri',0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.01,0.99,x,0.01,x,0.83,x,0.01,x,x,0.99,x,0.01,x,0.99,x,x,x,0.99,x,x,x,x,x,x,x,x,0.01,x,x,x,0.51),
            ('Citrobacter freundii',0.99,0.01,0.83,0.83,0.18,0.83,0.99,0.01,0.99,0.99,0.18,x,0.99,0.01,0.83,0.99,0.99,0.83,0.99,0.01,0.99,0.83,0.99,0.99,x,0.51,x,x,x,0.01,0.18,0.01,x,x,0.01,0.01,x,x,0.51),
            ('Citrobacter gillenii',0.99,0.01,0.83,0.83,0.01,0.51,0.99,0.01,0.99,x,0.01,x,0.51,x,0.51,x,x,0.18,x,0.18,x,0.18,x,x,x,0.18,x,x,x,x,x,x,x,x,0.01,x,x,x,0.01),
            ('Citrobacter (diversus) koseri',0.99,0.01,0.99,0.01,0.99,0.99,0.99,0.01,0.99,0.99,0.51,x,0.99,0.01,0.51,0.99,0.99,0.01,0.99,0.01,0.99,0.51,0.99,0.99,x,0.99,x,x,x,0.01,0.99,0.01,x,x,0.01,0.01,x,x,0.51),
            ('Citrobacter murliniae',0.99,0.01,0.99,0.51,0.99,0.83,0.99,0.01,0.99,x,0.99,x,0.99,x,0.51,x,x,0.18,x,0.18,x,0.18,x,x,x,0.51,x,x,x,x,x,x,x,x,0.01,x,x,x,0.51),
            ('Citrobacter rodentium',0.99,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.99,x,0.01,x,0.01,x,0.99,x,x,0.01,x,0.01,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,x,0.01,x,x,x,0.83),
            ('Citrobacter sedlakii',0.99,0.01,0.99,0.01,0.99,0.83,0.99,0.01,0.99,x,0.99,x,0.83,x,0.99,x,x,0.01,x,0.18,x,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,0.18,x,x,x,0.99),
            ('Citrobacter werkmanii',0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.01,0.99,x,0.01,x,0.99,x,0.18,x,x,0.01,x,0.01,x,0.01,x,x,x,0.83,x,x,x,x,x,x,x,x,0.01,x,x,x,0.99),
            ('Citrobacter youngae',0.99,0.01,0.99,0.83,0.01,0.83,0.99,0.01,0.99,x,0.83,x,0.99,x,0.18,x,x,0.01,x,0.01,x,0.18,x,x,x,0.51,x,x,x,x,x,x,x,x,0.01,x,x,x,0.51),
            ('Edwardsiella hoshinae',0.99,0.01,0.99,0.01,0.18,0.01,0.99,0.01,0.99,0.18,0.01,x,0.51,0.01,0.01,0.99,0.99,0.01,0.01,0.51,0.01,0.99,0.99,0.01,x,0.01,x,x,x,0.99,0.99,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Edwardsiella ictaluri',0.99,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.99,0.01,0.01,x,0.01,0.01,0.01,0.99,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,x,0.01,x,x,x,0.99,0.51,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Edwardsiella tarda',0.99,0.01,0.99,0.99,0.99,0.01,0.99,0.01,0.99,0.01,0.01,x,0.51,0.01,0.01,0.99,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,x,0.01,x,x,x,0.99,0.99,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Enterobacter aerogenes',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,x,0.01,x,x,x,0.99,0.99,0.01,x,x,0.99,0.01,x,x,0.01),
            ('Enterobacter agglomerans',0.99,0.01,0.83,0.01,0.18,0.51,0.83,0.01,0.99,0.99,0.18,x,0.51,0.18,0.51,0.99,0.99,0.51,0.83,0.51,0.51,0.83,0.99,0.99,x,0.01,x,x,x,0.01,0.01,0.18,x,x,0.51,0.01,x,x,0.18),
            ('Enterobacter amnigenus biogroup 1',0.99,0.01,0.99,0.01,0.01,0.51,0.99,0.01,0.99,0.99,0.01,x,0.01,0.01,0.51,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.99,0.99,x,0.01,x,x,x,0.01,0.51,0.01,x,x,0.99,0.01,x,x,0.01),
            ('Enterobacter amnigenus biogroup 2',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.01,0.01,0.51,0.99,0.99,0.01,0.99,0.99,0.99,0.01,0.99,0.99,x,0.51,x,x,x,0.01,0.99,0.01,x,x,0.99,0.01,x,x,0.01),
            ('Enterobacter asburiae',0.99,0.01,0.01,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.18,0.01,0.83,0.99,0.99,0.51,0.01,0.99,0.99,0.99,0.99,0.99,x,0.18,x,x,x,0.01,0.99,0.01,x,x,0.99,0.01,x,x,0.51),
            ('Enterobacter cancerogenus',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.01,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,0.01,0.99,0.99,x,0.99,x,x,x,0.01,0.99,0.01,x,x,0.99,0.01,x,x,0.01),
            ('Enterobacter cloacae',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.18,x,0.51,0.18,0.99,0.99,0.99,0.99,0.99,0.83,0.99,0.99,0.99,0.99,x,0.99,x,x,x,0.01,0.99,0.01,x,x,0.51,0.01,x,x,0.51),
            ('Enterobacter (Erwinia) dissolvens',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.01,0.51,0.51,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,x,0.99,x,x,x,0.01,0.99,0.01,x,x,0.99,0.01,x,x,0.99),
            ('Enterobacter gergoviae',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.99,0.01,0.51,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.99,0.99,x,0.01,x,x,x,0.99,0.99,0.01,x,x,0.99,0.01,x,x,0.99),
            ('Enterobacter hormaechei',0.99,0.01,0.51,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.83,x,0.01,0.01,0.01,0.99,0.99,0.01,0.99,0.51,0.01,0.99,0.99,0.99,x,0.83,x,x,x,0.01,0.99,0.01,x,x,0.01,0.01,x,x,0.83),
            ('Enterobacter intermedius',0.99,0.01,0.99,0.01,0.01,0.51,0.99,0.01,0.99,0.99,0.99,x,0.99,0.01,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.51,0.99,0.99,x,0.01,x,x,x,0.01,0.99,0.01,x,x,0.99,0.01,x,x,0.01),
            ('Enterobacter (Erwinia) nimipressuralis',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.99,0.01,0.99,0.99,0.99,0.01,0.99,0.99,0.99,0.01,0.99,0.99,x,0.99,x,x,x,0.01,0.99,0.01,x,x,0.99,0.99,x,x,0.01),
            ('Enterobacter sakazakii',0.99,0.01,0.99,0.01,0.18,0.99,0.99,0.01,0.99,0.99,0.01,x,0.18,0.83,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.01,0.99,0.99,x,0.99,x,x,x,0.01,0.99,0.51,x,x,0.99,0.01,x,x,0.01),
            ('Enterobacter taylorae',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.01,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,0.01,0.99,0.99,x,0.99,x,x,x,0.01,0.99,0.01,x,x,0.99,0.01,x,x,0.01),
            ('Erwinia amylovora ',0.99,0.01,0.99,0.01,0.01,0.99,0.01,x,0.99,0.51,0.01,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.51,x,0.99,0.01,x,x,x,x,x,x,x,0.01,x,x,x,0.99,x,x,0.01),
            ('Erwinia ananas',0.99,0.01,0.99,0.51,0.99,0.99,0.01,x,0.99,0.99,0.01,x,0.99,0.99,0.99,0.99,0.99,0.99,0.51,0.99,0.99,x,0.99,0.99,x,0.01,x,x,x,0.01,0.01,0.01,x,x,x,0.99,x,x,0.01),
            ('Erwinia cacticida',0.99,0.01,0.99,x,0.01,0.99,0.99,0.01,0.99,0.01,0.01,x,0.83,0.01,0.18,0.01,0.99,0.01,0.99,0.99,0.01,0.99,0.83,0.51,x,x,x,x,x,0.01,0.01,0.01,x,x,0.99,0.01,x,x,0.01),
            ('Erwinia carotovora',0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.51,0.51,0.99,0.51,0.99,0.99,0.99,0.99,0.99,x,0.99,0.99,x,x,x,x,x,x,x,0.01,x,x,x,0.99,x,x,0.01),
            ('Erwinia chrysanthemi',0.99,0.01,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.99,0.01,x,0.99,0.51,0.51,0.01,0.99,0.99,0.99,0.99,0.99,x,0.01,0.99,x,x,x,x,x,x,x,0.01,x,x,x,0.99,x,x,0.01),
            ('Erwinia cypripedii',0.99,0.01,0.99,0.99,0.01,x,0.99,0.01,0.99,0.99,0.01,x,0.51,0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.99,x,0.99,0.99,x,x,x,x,x,x,x,0.99,x,x,x,0.01,x,x,0.01),
            ('Erwinia mallotivora ',0.99,0.01,0.99,0.01,0.01,x,0.01,x,0.99,0.01,0.01,x,0.01,0.01,0.01,0.01,0.99,0.01,0.99,0.01,0.01,x,0.99,0.99,x,x,x,x,x,x,x,0.01,x,x,x,0.01,x,x,0.01),
            ('Erwinia nigrifluens',0.99,0.01,0.99,0.99,0.01,x,0.01,x,0.99,0.99,0.01,x,0.99,0.99,0.01,0.01,0.99,0.99,0.99,0.99,0.99,x,0.99,0.99,x,x,x,x,x,x,x,0.01,x,x,x,0.01,x,x,0.99),
            ('Erwinia persicinus',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.01,x,0.01,x,x,x,0.01,0.01,0.01,x,x,0.99,0.01,x,x,0.01),
            ('Erwinia psidii ',0.99,0.01,0.99,0.99,0.01,x,0.01,x,0.99,x,0.99,x,x,0.99,0.01,x,0.99,0.01,0.99,0.99,0.99,x,0.01,0.01,x,x,x,x,x,x,x,0.01,x,x,x,0.01,x,x,0.01),
            ('Erwinia quercina',0.99,0.01,0.99,0.99,0.01,x,0.01,x,0.99,0.01,0.01,x,0.99,0.01,0.01,0.01,0.99,0.01,0.01,0.99,0.99,x,0.01,0.01,x,x,x,x,x,x,x,0.01,x,x,x,0.01,x,x,0.01),
            ('Erwinia rhapontici',0.99,0.01,0.99,0.99,0.01,x,0.99,0.01,0.99,0.99,0.51,x,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,x,0.99,0.51,x,x,x,x,x,x,x,0.01,x,x,x,0.01,x,x,0.01),
            ('Erwinia rubrifaciens',0.99,0.01,0.99,0.99,0.01,x,0.01,x,0.99,0.99,0.01,x,0.51,0.01,0.01,0.01,0.99,0.01,0.01,0.01,0.99,x,0.01,0.01,x,x,x,x,x,x,x,0.01,x,x,x,0.01,x,x,0.01),
            ('Erwinia salicis',0.99,0.01,0.99,0.99,0.01,x,0.01,x,0.99,0.01,0.01,x,0.51,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,x,0.01,0.01,x,x,x,x,x,x,x,0.01,x,x,x,0.01,x,x,0.01),
            ('Erwinia stewartii',0.99,0.01,0.01,0.01,0.01,x,0.01,x,0.99,0.99,0.01,x,0.01,0.01,0.99,0.01,0.99,0.99,0.01,0.01,0.99,x,0.99,0.99,x,0.01,x,x,x,0.01,0.01,0.01,x,x,x,0.01,x,x,0.01),
            ('Erwinia tracheiphila',0.99,0.01,0.99,0.99,0.01,x,0.01,x,0.99,0.01,0.01,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,x,0.01,0.01,x,x,x,x,x,x,x,0.01,x,x,x,0.01,x,x,0.01),
            ('Erwinia uredovora',0.99,0.01,0.99,0.01,0.99,x,0.99,x,0.99,0.99,0.01,x,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.51,0.99,x,0.99,0.99,x,0.01,x,x,x,0.01,0.01,0.01,x,x,x,0.99,x,x,0.01),
            ('Escherichia blattae',0.99,0.01,0.01,0.01,0.01,0.51,0.99,0.01,0.99,0.99,0.01,x,0.99,0.01,0.01,0.99,0.01,0.01,0.99,0.01,0.01,0.01,0.83,0.99,x,0.01,x,x,x,0.99,0.99,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Escherichia coli (inactive)',0.99,0.01,0.01,0.01,0.83,0.01,0.99,0.01,0.99,0.83,0.51,x,0.51,0.01,0.18,0.83,0.99,0.18,0.51,0.01,0.83,0.18,0.99,0.51,x,0.01,x,x,x,0.51,0.18,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Escherichia coli',0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.99,0.51,x,0.51,0.01,0.99,0.99,0.99,0.51,0.83,0.51,0.99,0.51,0.99,0.99,x,0.18,x,x,x,0.99,0.51,0.01,x,x,0.51,0.01,x,x,0.01),
            ('Escherichia fergusonii',0.99,0.01,0.99,0.01,0.99,0.18,0.99,0.01,0.99,0.99,0.51,x,0.18,0.01,0.01,0.99,0.99,0.01,0.99,0.51,0.01,0.01,0.99,0.99,x,0.01,x,x,x,0.99,0.99,0.01,x,x,0.51,0.01,x,x,0.01),
            ('Escherichia hermanii',0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.99,0.18,x,0.01,0.01,0.51,0.99,0.99,0.51,0.99,0.51,0.01,0.51,0.99,0.99,x,0.01,x,x,x,0.01,0.99,0.01,x,x,0.51,0.01,x,x,0.01),
            ('Escherichia vulneris',0.99,0.01,0.99,0.01,0.01,0.01,0.99,0.01,0.99,0.99,0.01,x,0.18,0.01,0.18,0.99,0.99,0.99,0.99,0.51,0.01,0.01,0.99,0.99,x,0.51,x,x,x,0.83,0.01,0.01,x,x,0.18,0.01,x,x,0.01),
            ('Hafnia alvei',0.99,0.01,0.83,0.01,0.01,0.01,0.99,0.01,0.99,0.99,0.01,x,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.18,0.01,0.01,0.99,0.99,x,0.01,x,x,x,0.99,0.99,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Klebsiella oxytoca',0.99,0.01,0.01,0.01,0.99,0.99,0.99,0.01,0.99,0.99,0.51,x,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,x,0.01,x,x,x,0.99,0.01,0.01,x,x,0.99,0.01,x,x,0.99),
            ('Klebsiella planticola',0.99,0.01,0.01,0.01,0.18,0.99,0.99,0.01,0.99,0.99,0.18,x,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,x,0.01,x,x,x,0.99,0.01,0.01,x,x,0.99,0.01,x,x,0.99),
            ('Klebsiella pneumoniae ozaenae',0.99,0.01,0.01,0.01,0.01,0.51,0.83,0.18,0.99,0.99,0.01,x,0.51,0.51,0.51,0.99,0.99,0.99,0.51,0.99,0.51,0.18,0.99,0.99,x,0.01,x,x,x,0.51,0.01,0.01,x,x,0.83,0.01,x,x,0.01),
            ('Klebsiella pneumoniae pneumoniae',0.99,0.01,0.01,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.51,x,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,x,0.01,x,x,x,0.99,0.01,0.01,x,x,0.99,0.01,x,x,0.99),
            ('Klebsiella pneumoniae rhinoscleromatis',0.99,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.99,0.99,0.01,x,0.51,0.99,0.01,0.99,0.99,0.99,0.99,0.99,0.99,0.83,0.99,0.99,x,0.01,x,x,x,0.01,0.01,0.01,x,x,0.51,0.01,x,x,0.01),
            ('Klebsiella terrigena',0.99,0.01,0.01,0.01,0.01,0.51,0.99,0.01,0.99,0.99,0.18,x,0.99,0.83,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,x,0.01,x,x,x,0.99,0.18,0.01,x,x,0.99,0.01,x,x,0.01),
            ('Kluyvera ascorbata',0.99,0.01,0.99,0.01,0.99,0.99,0.99,0.01,0.99,0.99,0.18,x,0.51,0.01,0.99,0.99,0.99,0.99,0.99,0.99,0.51,0.99,0.99,0.99,x,0.01,x,x,x,0.99,0.99,0.01,x,x,0.99,0.01,x,x,0.01),
            ('Kluyvera cryocrescens',0.99,0.01,0.99,0.01,0.99,0.83,0.99,0.01,0.99,0.99,0.01,x,0.01,0.01,0.99,0.99,0.99,0.99,0.99,0.99,0.51,0.83,0.99,0.99,x,0.01,x,x,x,0.18,0.99,0.01,x,x,0.99,0.01,x,x,0.01),
            ('Leclercia (Escherichia) adecarboxylata',0.99,0.01,0.83,0.01,0.99,0.01,0.99,0.01,0.99,0.99,0.83,x,0.01,0.01,0.99,0.99,0.99,0.51,0.99,0.99,0.01,0.51,0.99,0.99,x,0.01,x,x,x,0.01,0.01,0.01,x,x,0.99,0.01,x,x,0.18),
            ('Leminorella grimontii',0.99,0.01,0.01,0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.83,x,0.18,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.83,x,0.01,x,x,x,0.01,0.01,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Leminorella richardii',0.99,0.01,0.01,0.99,0.01,0.01,0.99,0.01,0.99,0.99,0.01,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.99,x,0.01,x,x,x,0.01,0.01,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Moellerella wisconsensis',0.99,0.01,0.01,0.01,0.01,0.83,0.99,0.01,0.99,0.01,0.01,x,0.01,0.01,0.99,0.51,0.51,0.99,0.01,0.01,0.01,0.99,0.01,0.01,x,0.01,x,x,x,0.01,0.01,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Morganella morganii',0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.01,0.01,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,x,0.01,x,x,x,0.01,0.99,0.99,x,x,0.01,0.01,x,x,0.99),
            ('Pantoea agglomerans',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.01,0.01,0.18,0.99,0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.99,x,0.01,x,x,x,0.01,0.51,0.83,x,x,0.99,0.01,x,x,0.01),
            ('Pantoea dispersa',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.51,0.01,x,0.18,0.51,0.01,0.99,0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.99,x,0.01,x,x,x,0.01,0.01,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Pragia fontium',0.99,0.01,0.99,0.99,0.01,0.83,0.99,0.01,0.99,0.01,0.01,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.83,0.01,0.01,0.01,0.01,x,0.01,x,x,x,0.01,0.01,0.18,x,x,0.83,0.01,x,x,0.01),
            ('Proteus mirabilis',0.99,0.01,0.99,0.99,0.01,0.51,0.99,0.01,0.99,0.01,0.01,x,0.51,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.18,0.99,0.99,x,0.01,x,x,x,0.01,0.99,0.99,x,x,0.01,0.99,x,x,0.99),
            ('Proteus myxofaciens',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.01,0.01,x,0.99,0.01,0.01,0.99,0.01,0.01,0.01,0.01,0.01,0.99,0.99,0.01,x,0.01,x,x,x,0.01,0.01,0.99,x,x,0.01,0.99,x,x,0.99),
            ('Proteus penneri',0.99,0.01,0.83,0.51,0.01,0.01,0.99,0.01,0.99,0.01,0.01,x,0.51,0.01,0.01,0.99,0.01,0.01,0.01,0.01,0.01,0.99,0.51,0.99,x,0.01,x,x,x,0.01,0.01,0.99,x,x,0.01,0.51,x,x,0.99),
            ('Proteus vulgaris',0.99,0.01,0.99,0.99,0.99,0.18,0.99,0.01,0.99,0.01,0.01,x,0.51,0.01,0.01,0.99,0.01,0.01,0.01,0.51,0.01,0.99,0.51,0.99,x,0.01,x,x,x,0.01,0.01,0.99,x,x,0.51,0.99,x,x,0.99),
            ('Salmonella bongori',0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.99,x,0.01,0.01,0.01,0.99,0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.99,x,0.51,x,x,x,0.99,0.99,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Salmonella choleraesuis arizonae',0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.01,0.01,0.18,0.99,0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.99,x,0.51,x,x,x,0.99,0.99,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Salmonella choleraesuis choleraesuis',0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.99,x,0.01,0.51,0.01,0.99,0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.99,x,0.51,x,x,x,0.99,0.99,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Salmonella choleraesuis diarizonae',0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.01,0.01,0.83,0.99,0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.99,x,0.51,x,x,x,0.99,0.99,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Salmonella choleraesuis houtenae',0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.01,0.01,0.01,0.99,0.99,0.01,0.99,0.51,0.99,0.01,0.99,0.99,x,0.51,x,x,x,0.99,0.99,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Salmonella choleraesuis indica',0.99,0.01,0.99,0.99,0.01,0.83,0.99,0.01,0.99,0.99,0.51,x,0.51,0.01,0.18,0.99,0.99,0.01,0.99,0.01,0.01,0.01,0.99,0.99,x,0.51,x,x,x,0.99,0.99,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Salmonella choleraesuis salamae',0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.01,0.99,0.99,0.99,x,0.18,0.01,0.01,0.99,0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.99,x,0.99,x,x,x,0.99,0.99,0.01,x,x,0.18,0.01,x,x,0.01),
            ('Serratia entomophila',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.01,0.01,x,0.01,0.01,0.01,0.99,0.99,0.01,0.01,0.99,0.01,0.99,0.99,0.51,x,0.01,x,x,x,0.01,0.01,0.01,x,x,0.99,0.99,x,x,0.01),
            ('Serratia ficaria',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.01,0.51,0.18,0.99,0.99,0.51,0.51,0.99,0.99,0.99,0.99,0.99,x,0.01,x,x,x,0.01,0.01,0.01,x,x,0.99,0.99,x,x,0.01),
            ('Serratia fonticola',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.99,x,0.83,0.51,0.99,0.99,0.99,0.99,0.83,0.99,0.99,0.18,0.99,0.83,x,0.01,x,x,x,0.99,0.99,0.01,x,x,0.99,0.01,x,x,0.18),
            ('Serratia grimesli',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.51,0.51,0.01,0.99,0.99,0.99,0.01,0.99,0.99,0.99,0.99,0.99,x,0.99,x,x,x,0.99,0.99,0.01,x,x,0.99,0.99,x,x,0.01),
            ('Serratia liquefaciens',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.99,0.51,0.01,0.99,0.99,0.83,0.18,0.99,0.99,0.99,0.99,0.99,x,0.01,x,x,x,0.99,0.99,0.01,x,x,0.99,0.99,x,x,0.01),
            ('Serratia marcescens',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.01,0.01,x,0.99,0.83,0.01,0.99,0.99,0.01,0.01,0.99,0.99,0.99,0.99,0.01,x,0.01,x,x,x,0.99,0.99,0.01,x,x,0.99,0.99,x,x,0.18),
            ('Serratia odorifera group 1',0.99,0.01,0.99,0.01,0.51,0.99,0.99,0.01,0.99,0.99,0.01,x,0.51,0.99,0.51,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,x,0.01,x,x,x,0.99,0.99,0.01,x,x,0.99,0.99,x,x,0.01),
            ('Serratia odorifera group 2',0.99,0.01,0.99,0.01,0.51,0.99,0.99,0.01,0.99,0.99,0.01,x,0.51,0.99,0.99,0.99,0.99,0.01,0.99,0.51,0.99,0.01,0.99,0.99,x,0.01,x,x,x,0.99,0.01,0.01,x,x,0.51,0.99,x,x,0.01),
            ('Serratia plymuthica',0.99,0.01,0.51,0.01,0.01,0.51,0.99,0.01,0.99,0.99,0.01,x,0.51,0.51,0.83,0.99,0.99,0.99,0.01,0.99,0.51,0.99,0.99,0.99,x,0.01,x,x,x,0.01,0.01,0.01,x,x,0.83,0.51,x,x,0.01),
            ('Serratia proteamaculans',0.99,0.01,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.51,0.51,0.01,0.99,0.99,0.99,0.51,0.51,0.83,0.99,0.99,0.99,x,0.01,x,x,x,0.99,0.99,0.01,x,x,0.51,0.99,x,x,0.01),
            ('Serratia rubidaea',0.99,0.01,0.83,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,0.18,0.18,0.99,0.99,0.99,0.99,0.01,0.99,0.01,0.99,0.99,0.99,x,0.01,x,x,x,0.51,0.01,0.01,x,x,0.99,0.99,x,x,0.01),
            ('Shigella boydii',0.99,0.01,0.01,0.01,0.51,0.01,0.99,0.01,0.99,0.51,0.01,x,0.01,0.01,0.01,0.51,0.99,0.51,0.01,0.01,0.51,0.01,0.83,0.01,x,0.01,x,x,x,0.01,0.01,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Shigella dysenteriae',0.99,0.01,0.01,0.01,0.51,0.01,0.99,0.01,0.99,0.51,0.01,x,0.01,0.01,0.01,0.51,0.99,0.51,0.01,0.01,0.51,0.01,0.83,0.01,x,0.01,x,x,x,0.01,0.01,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Shigella flexneri',0.99,0.01,0.01,0.01,0.51,0.01,0.99,0.01,0.99,0.51,0.01,x,0.01,0.01,0.01,0.51,0.99,0.51,0.01,0.01,0.51,0.01,0.83,0.01,x,0.01,x,x,x,0.01,0.01,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Shigella sonnei',0.99,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.99,0.99,0.01,x,0.18,0.01,0.01,0.99,0.99,0.01,0.83,0.01,0.01,0.01,0.99,0.01,x,0.01,x,x,x,0.01,0.99,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Yersinia aldovae',0.99,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.99,0.51,0.01,x,0.01,0.01,0.01,0.01,0.83,0.01,0.01,0.01,0.51,0.18,0.83,0.51,x,0.01,x,x,x,0.01,0.51,0.01,x,x,0.01,0.01,x,x,0.83),
            ('Yersinia bercovieri',0.99,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.99,0.99,0.01,x,0.01,0.01,0.18,0.99,0.99,0.01,0.01,0.18,0.99,0.99,0.99,0.99,x,0.01,x,x,x,0.01,0.83,0.01,x,x,0.18,0.01,x,x,0.51),
            ('Yersinia enterocolitica',0.99,0.01,0.01,0.01,0.51,0.01,0.99,0.01,0.99,0.99,0.01,x,0.99,0.51,0.01,0.83,0.99,0.01,0.01,0.18,0.99,0.99,0.99,0.51,x,0.01,x,x,x,0.01,0.99,0.01,x,x,0.18,0.01,x,x,0.83),
            ('Yersinia frederiksenii' ,0.99,0.01,0.01,0.01,0.99,0.18,0.99,0.01,0.99,0.99,0.01,x,0.83,0.18,0.51,0.99,0.99,0.51,0.99,0.99,0.99,0.99,0.99,0.99,x,0.01,x,x,x,0.01,0.99,0.01,x,x,0.83,0.01,x,x,0.83),
            ('Yersinia intermedia',0.99,0.01,0.01,0.01,0.99,0.01,0.99,0.01,0.99,0.99,0.01,x,0.51,0.18,0.51,0.99,0.99,0.51,0.99,0.99,0.99,0.99,0.99,0.99,x,0.01,x,x,x,0.01,0.99,0.01,x,x,0.99,0.01,x,x,0.83),
            ('Yersinia kristensenii',0.99,0.01,0.01,0.01,0.51,0.01,0.99,0.01,0.99,0.83,0.01,x,0.51,0.18,0.01,0.99,0.99,0.01,0.01,0.18,0.99,0.01,0.99,0.83,x,0.01,x,x,x,0.01,0.99,0.01,x,x,0.01,0.01,x,x,0.83),
            ('Yersinia mollaretii',0.99,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.99,0.99,0.01,x,0.18,0.01,0.51,0.51,0.99,0.01,0.01,0.18,0.99,0.99,0.99,0.51,x,0.01,x,x,x,0.01,0.83,0.01,x,x,0.01,0.01,x,x,0.18),
            ('Yersinia pestis',0.99,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.99,0.99,0.01,x,0.51,0.01,0.01,0.83,0.99,0.01,0.01,0.51,0.51,0.01,0.99,0.99,x,0.01,x,x,x,0.01,0.01,0.01,x,x,0.51,0.01,x,x,0.01),
            ('Yersinia pseudotuberculosis',0.99,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.99,0.51,0.01,x,0.51,0.01,0.01,0.99,0.99,0.18,0.51,0.18,0.01,0.01,0.99,0.99,x,0.01,x,x,x,0.01,0.01,0.01,x,x,0.99,0.01,x,x,0.99),
            ('Yersinia rohdei',0.99,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.99,0.99,0.01,x,0.51,0.01,0.01,0.01,0.99,0.51,0.01,0.01,0.99,0.99,0.99,0.51,x,0.01,x,x,x,0.01,0.18,0.01,x,x,0.01,0.01,x,x,0.51),
            ('Yersinia ruckeri',0.99,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.99,0.01,0.01,x,0.51,0.01,0.01,0.99,0.99,0.01,0.01,0.01,0.51,0.01,0.99,0.01,x,0.01,x,x,x,0.51,0.99,0.01,x,x,0.01,0.51,x,x,0.01)]

        if (self.gram_option.get()=="--" and
        self.shape_option.get()=="bacillus" and
        self.meta_option.get()=="fac anaerobe" and
        self.endo_option.get()=="--" and
        self.cat_option.get()=="+" and
        self.oxi_option.get()=="+"):
            Label(self.id_frame, text = "Gram Negative \n Facultative Anaerobe Bacillus \n", background = "white").pack(side=TOP, anchor = N)
            bac=[('Aeromonas allosaccharophila',0.99,0.99,0.99,0.01,0.99,0.51,0.99,0.01,0.99,0.51,x,x,0.99,x,0.01,x,0.99,0.51,0.51,0.01,0.01,0.99,x,x,x,0.51,x,x,x,0.99,0.51,x,x,x,0.51,x,x,x,0.01),
            ('Aeromonas bestiarum',0.99,0.99,0.99,0.99,0.99,0.51,0.99,0.01,0.99,0.99,x,x,0.99,x,0.18,x,0.99,0.01,0.83,0.99,0.18,0.99,x,x,x,0.83,x,x,x,0.83,0.01,x,x,x,0.99,x,x,x,0.01),
            ('Aeromonas caviae',0.99,0.99,0.99,0.01,0.99,0.83,0.99,0.01,0.99,0.99,0.01,x,0.51,0.01,0.51,0.99,0.99,0.01,0.01,0.99,0.01,0.99,0.99,0.01,x,0.99,x,x,x,0.01,0.01,0.01,x,x,0.99,0.99,x,x,0.01),
            ('Aeromonas encheleia',0.99,0.99,0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.01,x,x,0.83,x,0.01,x,0.83,0.01,0.83,0.99,0.01,0.83,x,x,x,0.99,x,x,x,0.01,0.01,x,x,x,0.99,x,x,x,0.01),
            ('Aeromonas eucrenophila',0.99,0.99,0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.83,0.01,x,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.99,0.01,0.83,0.99,0.01,x,0.99,x,x,x,0.01,0.01,0.51,x,x,0.99,0.99,x,x,0.01),
            ('Aeromonas hydrophila',0.99,0.99,0.99,0.83,0.99,0.51,0.99,0.01,0.99,0.83,0.01,x,0.99,0.01,0.18,0.99,0.99,0.01,0.18,0.83,0.01,0.99,0.99,0.01,x,0.99,x,x,x,0.99,0.01,0.01,x,x,0.99,0.99,x,x,0.01),
            ('Aeromonas jandaei',0.99,0.99,0.99,0.83,0.99,0.83,0.99,0.01,0.99,0.18,x,x,0.99,x,0.01,x,0.99,0.01,0.01,0.01,0.01,0.01,x,x,x,0.99,x,x,x,0.99,0.01,x,x,x,0.01,x,x,x,0.01),
            ('Aeromonas media',0.99,0.99,0.51,0.01,0.51,0.51,0.99,0.01,0.99,0.99,0.01,x,0.99,0.01,0.99,0.99,0.99,0.01,0.01,0.99,0.18,0.99,0.99,0.01,x,0.99,x,x,x,0.01,0.01,0.51,x,x,0.51,0.99,x,x,0.01),
            ('Aeromonas popoffii',0.99,0.99,0.99,0.51,0.51,0.51,0.99,0.01,0.99,0.51,x,x,0.99,x,0.01,x,0.99,0.01,0.01,0.01,0.01,0.01,x,x,x,0.99,x,x,x,0.01,0.01,x,x,x,0.01,x,x,x,0.01),
            ('Aeromonas salmonicida achromogenes',0.99,0.99,0.01,0.01,0.99,0.01,0.99,0.01,0.99,0.01,0.01,x,0.51,0.01,0.01,0.99,0.01,0.01,0.01,0.51,0.01,0.99,0.99,0.01,x,0.99,x,x,x,0.51,0.01,0.01,x,x,0.01,0.99,x,x,0.01),
            ('Aeromonas salmonicida masoucida',0.99,0.99,0.01,0.99,0.99,0.01,0.99,0.01,0.99,0.99,0.01,x,0.51,0.01,0.01,0.99,0.99,0.01,0.01,0.51,0.01,0.99,0.99,0.01,x,0.99,x,x,x,0.51,0.01,0.01,x,x,0.99,0.99,x,x,0.01),
            ('Aeromonas salmonicida salmonicida',0.99,0.99,0.01,0.01,0.01,0.01,0.99,0.01,0.99,0.99,0.01,x,0.51,0.01,0.01,0.99,0.99,0.01,0.01,0.51,0.01,0.01,0.99,0.01,x,0.99,x,x,x,0.51,0.01,0.01,x,x,0.99,0.99,x,x,0.01),
            ('Aeromonas salmonicida smithia',0.99,0.99,0.01,0.99,0.01,0.01,0.99,0.01,0.83,0.51,0.01,x,0.18,0.01,0.01,0.01,0.01,0.01,0.01,0.51,0.18,0.51,0.01,0.01,x,0.18,x,x,x,0.01,0.01,0.01,x,x,0.01,0.99,x,x,0.01),
            ('Aeromonas schubertii',0.99,0.99,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.01,0.01,x,0.51,0.01,0.01,0.99,0.01,0.01,0.01,0.01,0.01,0.01,0.99,0.01,x,0.99,x,x,x,0.83,0.01,0.51,x,x,0.01,0.99,x,x,0.01),
            ('Aeromonas sobria',0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.01,0.99,0.18,0.01,x,0.99,0.01,0.18,0.99,0.99,0.01,0.01,0.18,0.01,0.99,0.51,0.01,x,0.99,x,x,x,0.99,0.01,0.99,x,x,0.01,0.99,x,x,0.01),
            ('Aeromonas trota',0.99,0.99,0.99,0.51,0.99,0.99,0.99,0.01,0.99,0.01,x,x,0.51,x,0.51,x,0.83,0.01,0.01,0.01,0.01,0.18,x,x,x,0.99,x,x,x,0.99,0.01,x,x,x,0.01,x,x,x,0.01),
            ('Aeromonas veronii bv sobria',0.99,0.99,0.99,0.99,0.99,0.51,0.99,0.01,0.99,0.18,x,x,0.51,x,0.18,x,0.99,0.01,0.01,0.18,0.01,0.99,x,x,x,0.99,x,x,x,0.99,0.01,x,x,x,0.18,x,x,x,0.01),
            ('Aeromonas veronii bv veronii',0.99,0.99,0.99,0.51,0.99,0.99,0.99,0.01,0.99,0.01,0.01,x,0.99,0.01,0.18,0.99,0.99,0.01,0.01,0.99,0.01,0.99,0.99,0.01,x,0.01,x,x,x,0.99,0.99,0.83,x,x,0.99,0.83,x,x,0.01),
            ('Chromobacterium fluviatile',0.99,0.99,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.01,0.01,x,0.18,0.01,0.01,0.99,0.01,x,0.01,0.01,0.01,0.18,0.99,0.01,x,0.01,x,x,x,0.01,0.01,0.01,x,x,0.01,0.99,x,x,0.01),
            ('Chromobacterium violaceum',0.99,0.99,0.99,0.18,0.01,0.99,0.99,0.01,0.99,0.01,0.01,x,0.01,0.01,0.01,0.51,0.01,x,0.01,0.01,0.51,0.18,0.99,0.01,x,0.51,x,x,x,0.01,0.01,0.01,x,x,0.01,0.99,x,x,0.01),
            ('Plesiomonas shigelloides',0.99,0.99,0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.01,0.01,x,0.51,0.99,0.99,0.99,0.01,0.01,0.01,0.01,0.01,0.01,0.99,0.01,x,0.99,x,x,x,0.99,0.99,0.01,x,x,0.01,0.01,x,x,0.01),
            ('Vibrio cholerae',0.99,0.99,0.99,0.01,0.99,0.99,0.99,0.01,0.99,0.01,0.01,x,0.51,0.01,0.01,0.99,0.99,0.01,0.01,0.01,0.01,0.99,0.99,0.01,x,0.01,x,x,x,0.99,0.99,0.01,x,x,0.01,0.99,x,x,0.01),
            ('Vibrio fluvialis',0.99,0.99,0.51,0.01,0.18,0.99,0.99,0.01,0.99,0.99,0.01,x,0.01,0.01,0.01,0.99,0.99,0.01,0.01,0.01,0.01,0.99,0.99,0.01,x,0.99,x,x,x,0.01,0.01,0.01,x,x,0.01,0.83,x,x,0.01),
            ('Vibrio harveyi',0.99,0.99,0.01,0.01,0.99,0.01,0.99,0.01,0.51,0.01,0.01,x,0.01,0.01,0.01,0.99,0.51,0.01,0.01,0.01,0.01,0.51,0.51,0.01,x,0.01,x,x,x,0.99,0.01,0.51,x,x,0.01,0.01,x,x,0.01),
            ('Vibrio metschnokovii',0.99,0.99,0.51,0.01,0.18,0.51,0.01,0.01,0.99,0.01,0.01,x,0.99,0.51,0.51,0.99,0.99,0.01,0.01,0.01,0.51,0.99,0.99,0.01,x,0.51,x,x,x,0.51,0.01,0.01,x,x,0.01,0.51,x,x,0.01),
            ('Vibrio mimicus',0.99,0.99,0.99,0.01,0.99,0.99,0.99,0.01,0.99,0.01,0.01,x,0.18,0.01,0.18,0.99,0.99,0.01,0.01,0.01,0.01,0.01,0.99,0.01,x,0.01,x,x,x,0.99,0.99,0.01,x,x,0.51,0.51,x,x,0.01),
            ('Vibrio parahaemolyticus',0.99,0.99,0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.83,0.01,x,0.51,0.01,0.01,0.99,0.99,0.01,0.01,0.01,0.01,0.01,0.99,0.01,x,0.01,x,x,x,0.99,0.01,0.01,x,x,0.01,0.99,x,x,0.18),
            ('Vibrio vulnificus',0.99,0.99,0.99,0.01,0.99,0.51,0.99,0.01,0.99,0.01,0.01,x,0.01,0.01,0.83,0.99,0.51,0.01,0.01,0.99,0.01,0.18,0.99,0.01,x,0.01,x,x,x,0.99,0.51,0.51,x,x,0.51,0.51,x,x,0.01)]

        if (self.gram_option.get()=="+" and
        self.shape_option.get()=="bacillus" and
        self.meta_option.get()=="aerobe" and
        self.endo_option.get()=="--" and
        self.cat_option.get()=="+"):
            Label(self.id_frame, text = "Gram Positive \n Aerobe Bacillus \n", background = "white").pack(side=TOP, anchor = N)
            bac=[('Arthobacter',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Caryophanon',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Curtobacterium',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Kurthia',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Microbacterium',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Myobacterium',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Pimelobacterium',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Terrabacter',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)]

        if (self.gram_option.get()=="+" and
        self.shape_option.get()=="bacillus" and
        self.meta_option.get()=="fac anaerobe" and
        self.endo_option.get()=="--" and
        self.cat_option.get()=="+"):
            Label(self.id_frame, text = "Gram Positive \n Facultative Anaerobe Bacillus \n", background = "white").pack(side=TOP, anchor = N)
            bac=[('Brocothrix',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Cellumonas',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Erysiphelothrix',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Listeria',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)]

        if (self.gram_option.get()=="+" and
        self.shape_option.get()=="bacillus" and
        self.meta_option.get()!="?" and
        self.endo_option.get()=="+" and
        self.cat_option.get()=="+"):
            Label(self.id_frame, text = "Gram Positive \n Spore-forming Bacillus \n", background = "white").pack(side=TOP, anchor = N)
            bac=[('Bacillus',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)]

        if (self.gram_option.get()=="+" and
        self.shape_option.get()=="bacillus" and
        self.meta_option.get()!="?" and
        self.endo_option.get()=="+" and
        self.cat_option.get()=="--"):
            Label(self.id_frame, text = "Gram Positive \n Spore-forming Bacillus \n", background = "white").pack(side=TOP, anchor = N)
            bac=[('Amphibacillus',0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Sporolactobacillus',0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)]

        if (self.gram_option.get()=="+" and
        self.shape_option.get()=="coccus" and
        self.meta_option.get()=="aerobe" and
        self.endo_option.get()=="--" and
        self.cat_option.get()=="+"):
            Label(self.id_frame, text = "Gram Positive \n Aerobe Coccus \n", background = "white").pack(side=TOP, anchor = N)
            bac=[('Deinococcus',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Dermabacter',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Micrococcus',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Planococcus',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)]

        if (self.gram_option.get()=="+" and
        self.shape_option.get()=="coccus" and
        self.meta_option.get()=="fac anaerobe" and
        self.endo_option.get()=="--" and
        self.cat_option.get()=="+"):
            Label(self.id_frame, text = "Gram Positive \n Facultative Anaerobe Coccus \n", background = "white").pack(side=TOP, anchor = N)
            bac=[('Enterococcus',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Lactococcus',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Leuconostoc',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Pedicoccus',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Trichoccus',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
            ('Vagococcus',0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)]

        if (self.gram_option.get()=="+" and
        self.shape_option.get()=="coccus" and
        self.meta_option.get()=="aerobe" and
        self.endo_option.get()=="+" and
        self.cat_option.get()=="+" and
        self.oxi_option.get()=="+"):
            Label(self.id_frame, text = "Gram Positive \n Spore-forming Coccus \n", background = "white").pack(side=TOP, anchor = N)
            bac=[('Sporocarcina',0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)]

        def plus(matrix, i):
            return [row[i] for row in matrix]
        
        def minus(matrix, i):
            return [1.00-row[i] for row in matrix]


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

        if self.motil_option.get()=="+":
            bact2.append(plus(bac,3))
            bact3.append(plus(bac,3))
        if self.motil_option.get()=="--":
            bact2.append(minus(bac,3))
            bact3.append(plus(bac,3))

        if self.h2s_option.get()=="+":
            bact2.append(plus(bac,4))
            bact3.append(plus(bac,4))
        if self.h2s_option.get()=="--":
            bact2.append(minus(bac,4))
            bact3.append(plus(bac,4))

        if self.ind_option.get()=="+":
            bact2.append(plus(bac,5))
            bact3.append(plus(bac,5))
        if self.ind_option.get()=="--":
            bact2.append(minus(bac,5))
            bact3.append(plus(bac,5))

        if self.cit_option.get()=="+":
            bact2.append(plus(bac,6))
            bact3.append(plus(bac,6))
        if self.cit_option.get()=="--":
            bact2.append(minus(bac,6))
            bact3.append(plus(bac,6))

        if self.nit1_option.get()=="+":
            bact2.append(plus(bac,7))
            bact3.append(plus(bac,7))
        if self.nit1_option.get()=="--":
            bact2.append(minus(bac,7))
            bact3.append(plus(bac,7))

        if self.nit2_option.get()=="+":
            bact2.append(plus(bac,8))
            bact3.append(plus(bac,8))
        if self.nit2_option.get()=="--":
            bact2.append(minus(bac,8))
            bact3.append(plus(bac,8))

        if self.glu_option.get()=="+":
            bact2.append(plus(bac,9))
            bact3.append(plus(bac,9))
        if self.glu_option.get()=="--":
            bact2.append(minus(bac,9))
            bact3.append(plus(bac,9))

        if self.arab_option.get()=="+":
            bact2.append(plus(bac,10))
            bact3.append(plus(bac,10))
        if self.arab_option.get()=="--":
            bact2.append(minus(bac,10))
            bact3.append(plus(bac,10))

        if self.dul_option.get()=="+":
            bact2.append(plus(bac,11))
            bact3.append(plus(bac,11))
        if self.dul_option.get()=="--":
            bact2.append(minus(bac,11))
            bact3.append(plus(bac,11))

        if self.fru_option.get()=="+":
            bact2.append(plus(bac,12))
            bact3.append(plus(bac,12))
        if self.fru_option.get()=="--":
            bact2.append(minus(bac,12))
            bact3.append(plus(bac,12))

        if self.glyc_option.get()=="+":
            bact2.append(plus(bac,13))
            bact3.append(plus(bac,13))
        if self.glyc_option.get()=="--":
            bact2.append(minus(bac,13))
            bact3.append(plus(bac,13))

        if self.ino_option.get()=="+":
            bact2.append(plus(bac,14))
            bact3.append(plus(bac,14))
        if self.ino_option.get()=="--":
            bact2.append(minus(bac,14))
            bact3.append(plus(bac,14))

        if self.lac_option.get()=="+":
            bact2.append(plus(bac,15))
            bact3.append(plus(bac,15))
        if self.lac_option.get()=="--":
            bact2.append(minus(bac,15))
            bact3.append(plus(bac,15))

        if self.mal_option.get()=="+":
            bact2.append(plus(bac,16))
            bact3.append(plus(bac,16))
        if self.mal_option.get()=="--":
            bact2.append(minus(bac,16))
            bact3.append(plus(bac,16))

        if self.man_option.get()=="+":
            bact2.append(plus(bac,17))
            bact3.append(plus(bac,17))
        if self.man_option.get()=="--":
            bact2.append(minus(bac,17))
            bact3.append(plus(bac,17))

        if self.raf_option.get()=="+":
            bact2.append(plus(bac,18))
            bact3.append(plus(bac,18))
        if self.raf_option.get()=="--":
            bact2.append(minus(bac,18))
            bact3.append(plus(bac,18))

        if self.rham_option.get()=="+":
            bact2.append(plus(bac,19))
            bact3.append(plus(bac,19))
        if self.rham_option.get()=="--":
            bact2.append(minus(bac,19))
            bact3.append(plus(bac,19))

        if self.sal_option.get()=="+":
            bact2.append(plus(bac,20))
            bact3.append(plus(bac,20))
        if self.sal_option.get()=="--":
            bact2.append(minus(bac,20))
            bact3.append(plus(bac,20))

        if self.sorb_option.get()=="+":
            bact2.append(plus(bac,21))
            bact3.append(plus(bac,21))
        if self.sorb_option.get()=="--":
            bact2.append(minus(bac,21))
            bact3.append(plus(bac,21))

        if self.suc_option.get()=="+":
            bact2.append(plus(bac,22))
            bact3.append(plus(bac,22))
        if self.suc_option.get()=="--":
            bact2.append(minus(bac,22))
            bact3.append(plus(bac,22))

        if self.tre_option.get()=="+":
            bact2.append(plus(bac,23))
            bact3.append(plus(bac,23))
        if self.tre_option.get()=="--":
            bact2.append(minus(bac,23))
            bact3.append(plus(bac,23))

        if self.xyl_option.get()=="+":
            bact2.append(plus(bac,24))
            bact3.append(plus(bac,24))
        if self.xyl_option.get()=="--":
            bact2.append(minus(bac,24))
            bact3.append(plus(bac,24))

        if self.ala_option.get()=="+":
            bact2.append(plus(bac,25))
            bact3.append(plus(bac,25))
        if self.ala_option.get()=="--":
            bact2.append(minus(bac,25))
            bact3.append(plus(bac,25))

        if self.arg_option.get()=="+":
            bact2.append(plus(bac,26))
            bact3.append(plus(bac,26))
        if self.arg_option.get()=="--":
            bact2.append(minus(bac,26))
            bact3.append(plus(bac,26))

        if self.asp_option.get()=="+":
            bact2.append(plus(bac,27))
            bact3.append(plus(bac,27))
        if self.asp_option.get()=="--":
            bact2.append(minus(bac,27))
            bact3.append(plus(bac,27))

        if self.glut_option.get()=="+":
            bact2.append(plus(bac,28))
            bact3.append(plus(bac,28))
        if self.glut_option.get()=="--":
            bact2.append(minus(bac,28))
            bact3.append(plus(bac,28))

        if self.hist_option.get()=="+":
            bact2.append(plus(bac,29))
            bact3.append(plus(bac,29))
        if self.hist_option.get()=="--":
            bact2.append(minus(bac,29))
            bact3.append(plus(bac,29))

        if self.lys_option.get()=="+":
            bact2.append(plus(bac,30))
            bact3.append(plus(bac,30))
        if self.lys_option.get()=="--":
            bact2.append(minus(bac,30))
            bact3.append(plus(bac,30))

        if self.orn_option.get()=="+":
            bact2.append(plus(bac,31))
            bact3.append(plus(bac,31))
        if self.orn_option.get()=="--":
            bact2.append(minus(bac,31))
            bact3.append(plus(bac,31))

        if self.phen_option.get()=="+":
            bact2.append(plus(bac,32))
            bact3.append(plus(bac,32))
        if self.phen_option.get()=="--":
            bact2.append(minus(bac,32))
            bact3.append(plus(bac,32))

        if self.val_option.get()=="+":
            bact2.append(plus(bac,33))
            bact3.append(plus(bac,33))
        if self.val_option.get()=="--":
            bact2.append(minus(bac,33))
            bact3.append(plus(bac,33))

        if self.cas_option.get()=="+":
            bact2.append(plus(bac,34))
            bact3.append(plus(bac,34))
        if self.cas_option.get()=="--":
            bact2.append(minus(bac,34))
            bact3.append(plus(bac,34))

        if self.esc_option.get()=="+":
            bact2.append(plus(bac,35))
            bact3.append(plus(bac,35))
        if self.esc_option.get()=="--":
            bact2.append(minus(bac,35))
            bact3.append(plus(bac,35))

        if self.gel_option.get()=="+":
            bact2.append(plus(bac,36))
            bact3.append(plus(bac,36))
        if self.gel_option.get()=="--":
            bact2.append(minus(bac,36))
            bact3.append(plus(bac,36))

        if self.hip_option.get()=="+":
            bact2.append(plus(bac,37))
            bact3.append(plus(bac,37))
        if self.hip_option.get()=="--":
            bact2.append(minus(bac,37))
            bact3.append(plus(bac,37))

        if self.starch_option.get()=="+":
            bact2.append(plus(bac,38))
            bact3.append(plus(bac,38))
        if self.starch_option.get()=="--":
            bact2.append(minus(bac,38))
            bact3.append(plus(bac,38))

        if self.urea_option.get()=="+":
            bact2.append(plus(bac,39))
            bact3.append(plus(bac,39))
        if self.urea_option.get()=="--":
            bact2.append(minus(bac,39))
            bact3.append(plus(bac,39))

        bac2=zip(*bact2)
        bac3=zip(*bact3)

        #Algorithms
        bac4={}

        if self.algo_option.get()=="Additive Probability":
            bac4 = [(bac2[0],"%.2f"% reduce(mul,bac2[1:])) for bac2 in bac2]

        if self.algo_option.get()=="Geometric Mean":
            bac4 = [(bac2[0], "%.2f"% reduce(mul,bac2[1:])**(1.0/len(bac2[1:]))) for bac2 in bac2]

        if self.algo_option.get()=="Bayes Theorem":
           sigma = float(sum(reduce(mul,bac2[1:]) for bac2 in bac2))
           bac4 = [(bac2[0], "%.2f" % (reduce(mul,bac2[1:])/sigma)) for bac2 in bac2] 
                    
        if self.algo_option.get()=="Correlation":
            Label(self.id_frame, text = "Unwritten Code", background = "white").pack(side=TOP, anchor = W)


        bac5 = tuple(sorted(bac4, key=lambda item: item[1], reverse=True))

        if bac5[0][1]>=self.CI_option.get():
             Label(self.id_frame, text = bac5[0], background = "white").pack(side=TOP, anchor = W)
        if bac5[0][1]<self.CI_option.get():
            Label(self.id_frame, text = "Error: need more data \n", background = "white").pack(side=TOP, anchor = N)


        Label(self.id_frame, text = bac5[0], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = bac5[1], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = bac5[2], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = bac5[3], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = bac5[4], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = bac5[5], background = "white").pack(side=TOP, anchor = W)
        
root = Tk()
root.title("Freshwater Bacteria Compilation")
myapp = MyApp(root)
#root.withdraw()
root.mainloop()
