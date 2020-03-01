from Tkinter import (N, S, E, W, BOTH, BOTTOM, END, FLAT, HORIZONTAL, INSERT, LEFT, NO, RAISED, RIGHT, TOP, YES,
Button, Entry, Frame, Grid, Label, Menu, Pack, Radiobutton, Scale, StringVar, Text, Toplevel, Tk)

from operator import mul

root = Tk()
root.title("B. L. I. M. P. Bacteria Lot Identification Matrix Program")

class AutocompleteEntry(Entry):
        
    def set_completion_list(self, completion_list):
        self._completion_list = completion_list
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)               
        
    def autocomplete(self, delta=0):
        if delta:
            self.delete(self.position,END)
        else:
            self.position = len(self.get())
        _hits = []
        for element in self._completion_list:
            if element.startswith(self.get()):
                _hits.append(element)
                if _hits != self._hits:
                        self._hit_index = 0
                        self._hits=_hits
        if _hits == self._hits and self._hits:
                self._hit_index = (self._hit_index + delta) % len(self._hits)
        if self._hits:
                self.delete(0,END)
                self.insert(0,self._hits[self._hit_index])
                self.select_range(self.position,END)
                        
    def handle_keyrelease(self, event):
        if event.keysym == "BackSpace":
            self.delete(self.index(INSERT),END) 
            self.position = self.index(END)
        if event.keysym == "Down":
                self.autocomplete(1) # cycle to next hit
        if event.keysym == "Up":
                self.autocomplete(-1) # cycle to previous hit
        if len(event.keysym)== 1:
            self.autocomplete()

class Bacteria:
    def __init__(self, parent):

        # variables
        self.adon_option = StringVar()  #adonitol fermentation/growth
        self.ala_option = StringVar()   #alanine growth
        self.algo_option = StringVar()  #algorithm
        self.amp_option = StringVar()   #ampicillin resistance
        self.amy_option = StringVar()   #amylin hydrolysis
        self.amyg_option = StringVar()  #amygdalin hydrolysis
        self.arab_option = StringVar()  #arabinose fermentation/growth
        self.arg_option = StringVar()   #arginine dihydrolase
        self.asp_option = StringVar()   #asparagine growth
        self.cas_option = StringVar()   #casein hydrolysis
        self.cat_option = StringVar()   #catalase
        self.cell_option = StringVar()  #cellobiose fermentation/growth
        self.ceph_option = StringVar()  #cephalothin resistance
        self.chi_option = StringVar()   #chitin hydrolysis
        self.chlor_option = StringVar() #chloramphenicol resistance
        self.cit_option = StringVar()   #citrate
        self.coag_option = StringVar()  #coagulase
        self.dna_option = StringVar()   #deoxyribonuclease
        self.dul_option = StringVar()   #dulcitol fermentation/growth
        self.endo_option = StringVar()  #endospore formation
        self.endo_b_option = StringVar()#endospores bulging
        self.endo_c_option = StringVar()#endospores centrally located
        self.endo_o_option = StringVar()#endospores oval-shaped
        self.esc_option = StringVar()   #esculin hydrolysis
        self.ethan_option = StringVar() #ethanol fermentation/growth
        self.fast_option = StringVar()  #fastidious culture requirements
        self.fru_option = StringVar()   #fructose fermentation/growth
        self.galac_option = StringVar() #galactose fermentation/growth
        self.gel_option = StringVar()   #gelatin hydrolysis
        self.glu_option = StringVar()   #glucose fermentation
        self.glug_option = StringVar()  #glucose gas
        self.glux_option = StringVar()  #glucose oxidation
        self.glut_option = StringVar()  #glutamic acid growth
        self.glyc_option = StringVar()  #glycerol fermentation/growth
        self.gram_option = StringVar()  #gram stain
        self.group_option = StringVar() #bacteria group
        self.h2s_option = StringVar()   #hydrogen suldife
        self.hem_option = StringVar()   #hemolysis
        self.hip_option = StringVar()   #hippurate hydrolysis
        self.hist_option = StringVar()  #histidine growth
        self.ind_option = StringVar()   #indole
        self.ino_option = StringVar()   #inositol fermentation/growth
        self.lac_option = StringVar()   #lactose fermentation/growth
        self.lys_option = StringVar()   #lysine decarboxylase
        self.mal_option = StringVar()   #maltose fermentation/growth
        self.man_option = StringVar()   #mannitol fermentation/growth
        self.mann_option = StringVar()  #mannose fermentation/growth
        self.meli_option = StringVar()  #melibiose fermentation/growth
        self.meta_option = StringVar()  #metabolism
        self.motil_option = StringVar() #motility
        self.nal_option = StringVar()   #nalidixic acid resistance
        self.nit1_option = StringVar()  #nitrate -> nitrite reduction
        self.nit2_option = StringVar()  #nitrite -> nitrogen gas reduction        
        self.nit3_option = StringVar()  #nitrogen gas -> nitrite -> nitrate oxidation
        self.onpg_option = StringVar()  #o-nitrophenyl-beta-d-galactopyranoside
        self.orn_option = StringVar()   #ornithine decarboxylase
        self.oxi_option = StringVar()   #oxidase
        self.phen_option = StringVar()  #phenylalanine deaminase
        self.phos_option = StringVar()  #phosphatase
        self.poly_option = StringVar()  #polymyxin resistance
        self.raf_option = StringVar()   #raffinose fermentation/growth
        self.rham_option = StringVar()  #rhamnose fermentation/growth
        self.sal_option = StringVar()   #salicin fermentation/growth
        self.salt_option = StringVar()  #salinity
        self.shape_option  = StringVar()#bacteria shape
        self.sorb_option = StringVar()  #sorbitol fermentation/growth
        self.starch_option = StringVar()#starch hydrolysis
        self.strep_option = StringVar() #streptomycin resistance
        self.suc_option = StringVar()   #sucrose fermentation/growth
        self.temp_option = StringVar()  #temperature, incubator
        self.tre_option = StringVar()   #trehalose fermentation/growth
        self.trypto_option = StringVar()#tryptophan deaminase
        self.tw20_option = StringVar()  #tween20 hydrolysis
        self.tw80_option = StringVar()  #tween80 hydrolysis
        self.tyro_option = StringVar()  #tyrosine hydrolysis
        self.urea_option = StringVar()  #urea hydrolysis
        self.val_option = StringVar()   #valine growth
        self.vp_option = StringVar()    #voges-proskauer test
        self.xyl_option = StringVar()   #xylose fermentation/growth

        # top-level menu (and menu-selection definitions)
        def donothing():
            filewin = Toplevel(background="red")
            button = Button(filewin, text="Do nothing button")
            button.pack(side=LEFT, expand=NO, padx=10, pady=5, ipadx=5, ipady=5)
            filewin.title("Nothing")
    
        def intronothing():
            filewin = Toplevel(background="yellow")
            Label(filewin, text=". . .\n \
            Welcome to the wonderful world of water bacteria identification without 16S rRNA samples. \n\n \
            This database includes over 300 common taxa likely found in lotic or lentic environments. \n \
            Any temperate inland habitat with dirt, oxygen, and water. \n \n \
            This compilation does not include protozoa, plankton, obligate anaerobes, or bacteria which cannot be lab cultured. \n \
            Bacteria strains are variable, fickle, and constantly changing their morphology: individual test results may not provide an exact match. \n\
            Taxonomists are variable, fickle, and constantly changing their minds: old genera are parenthetically noted \n\n\
            First, select the group to which your bacteria belongs, select an analytical test, confidence interval, and click 'Submit'. \n\
            Enter the phenotypic test results for your unidentified bacteria colony. \n \
            Click 'Identify' to display bacteria which best match your current results and 'Reset' to clear the slate. \n \
            Click 'Search' to to display the expected test results for a known bacterium after entering its name in the text window. \n\n\
            Instructions on how to run and interpret the biochemical tests are available in the top menu. \n \
            All tests performed on 48 hour old colony cultures except gram stains (24hr) and endospore tests (1 week)\n \
            For each 'Search' command, any test with > 85% positive result scores + , < 15% scores --, and those in between or unknown are unscored. \n \n \
            This program is freeware published and distributed under the GNU public license.  Suggestions for updates welcome.  \n\
            Please credit author. \n \n \
            - Jeff Bardwell, 2012 \n \
              (mudnwater@yahoo.com)\n\n\n", justify=LEFT, font=10, background="yellow", foreground="dark green").pack()
            filewin.title("water Bacteria ID v 2.0")

        def generanothing():
            filewin = Toplevel(background="white")

            Label(filewin, text=". . .\n \
        1a)Gram Negative Facultative Anaerobe Bacillus (catalase +, oxidase - )\n\
            Brennaria, Budvicia, Buttiauxella, Citrobacter, Edwardsiella, Enterobacter, Erwinia, Escherichia, Hafnia \n\
            Klebsiella, Kluyvera, Lecleria, Leminorella, Moellerella, Morganella, Pantoea, Pectobacterium \n\
            Pragia, Proteus, Rahnella, Salmonella, Serratia, Shigella, Trabulsiella, Vibrio, Xenorhabdus, Yersinia \n\
        1b)Gram Negative Facultative Anaerobe Bacillus (catalase +, oxidase + )\n\
            Aeromonas, Chromobacterium, Plesiomonas, Vibrio \n\
        1c)Gram Negative Facultative Anaerobe Bacillus (catalase -, oxidase - ) \n\
            Xenorhabdus \n\n\
        2a)Gram Negative Aerobe Bacillus (catalase +, oxidase - ) \n\
            Acidiphilium, Acinetobacter, Agrobacterium, Azomonas, Azotobacter, Flavimonas, Deinobacter, Gluconobacter, Flavimonas \n\
        2b)Gram Negative Aerobe Bacillus (catalase +, oxidase + ) \n\
            Achromobacter, Acidophilium, Acidovorax, Agrobacterium, Agromonas, Alcaligenes, Aquaspirillum, Azomonas, Azotobacter, Comamonas, \n\
            Cupriavidis, Ensifer, Flavobacterium, Hydrogenophila, Janthinobacterium, Legionella, Pseudomonas, Rhizobacter, Roseomonas, \n\
            Serpens, Shingobacterium, Veriovorax, Xanthobacter, Zooglea \n\n\
        2c)Gram Negative Aerobe Bacillus (catalase - ) \n\
            Derxia \n\n\
        3)Gram Positive Facultative Anaerobe Bacillus \n\
            Brocothrix, Cellulomonas, Corynebacterium, Erysiphelothrix, Listeria \n\
        4)Gram Positive Aerobe Bacillus \n\
            Caryophanon, Curtobacterium, Kurthia, Microbacterium, Mycobacterium, Pimelobacterium, Rhodococcus, Terrabacter \n\n\
        5)Gram Positive Facultative Anaerobe Coccus \n\
            Enterococcus, Lactococcus, Leuconostoc, Pedicoccus, Trichoccus, Vagococcus \n\
        6)Gram Positive Aerobe Coccus \n\
            Arthrobacter, Deinococcus, Dermabacter, Micrococus, Planococus \n\
        7)Spore Forming Bacillus and Coccus \n\
            Amphibacillus, Aneurinibacillus, Bacillus, Brevibacillus, Paenibacillus, Sporosarcina, Sporolactobacillus, Virgibacillus \n",
            justify=LEFT, background="white", foreground="black", wraplength=1000).pack()
            filewin.title("Bacteria Groups")

        def referencenothing():
            filewin = Toplevel(background="white")

            mytext = "insert references here, code error if you insert too many citations: non ASCII, # -*- coding: cp1252 -*-"
            scrbar = Scrollbar(filewin, orient=VERTICAL)
            scrbar.pack(side=RIGHT,fill=Y)
            text = Text(filewin, width=100, height=20, state=NORMAL, background="white", foreground="black")
            text.insert(INSERT, mytext)
            text['state'] = DISABLED
            text.pack()
            text['yscrollcommand'] = scrbar.set
            scrbar['command'] = text.yview  

            filewin.title("Matrix References")
        
        menubar = Menu(root)

        intromenu = Menu(menubar, tearoff=0)
        intromenu.add_command(label="Read Me", command=intronothing)
        intromenu.add_command(label="Credits", command=donothing)        
        menubar.add_cascade(label="Instructions", menu=intromenu)

        datamenu = Menu(menubar, tearoff=0)
        datamenu.add_command(label="Groups", command=generanothing)
        datamenu.add_command(label="References", command=referencenothing)
        menubar.add_cascade(label="Database", menu=datamenu)

        labmenu = Menu(menubar, tearoff=0)
        labmenu.add_command(label="Lab Safety", command=donothing)
        labmenu.add_separator()
        labmenu.add_command(label="Making Plates", command=donothing)
        labmenu.add_command(label="Colony Counts", command=donothing)
        labmenu.add_separator()
        labmenu.add_command(label="MAC", command=donothing)
        labmenu.add_command(label="MSA", command=donothing)
        labmenu.add_command(label="SS", command=donothing)
        labmenu.add_command(label="TSA", command=donothing)
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
        menubar.add_cascade(label="Procedure", menu=labmenu)

        analysismenu = Menu(menubar, tearoff=0)
        analysismenu.add_command(label="Statistics", command=donothing)
        analysismenu.add_separator()
        analysismenu.add_command(label="Bayes Theorem", command=donothing)
        analysismenu.add_command(label="Geometric Mean", command=donothing)
        analysismenu.add_command(label="Correlation", command=donothing)
        menubar.add_cascade(label="Analysis", menu=analysismenu)

        root.config(menu=menubar)

        # button options
        algo_options = ["Geometric Mean", "Bayes Theorem", "Phi Coefficient"]
        fast_options = ["None", "Salt", "Blood", "Yeast"]
        group_options = ["Gram Negative Facultative Anaerobe Bacillus", "Gram Negative Aerobe Bacillus", "Gram Negative Aerobe Coccus",
        "Gram Positive Facultative Anaerobe Bacillus", "Gram Positive Aerobe Bacillus",
        "Gram Positive Facultative Anaerobe Coccus", "Gram Positive Aerobe Coccus",
        "Spore Forming Bacillus and Coccus"]

        # button defaults
        self.group_option.set("Gram Negative Facultative Anaerobe Bacillus")
        self.algo_option.set("Bayes Theorem")
        self.fast_option.set("None")
    
        # layout
        self.myParent = parent

        self.myContainer1 = Frame(parent, background="light blue")
        self.myContainer1.pack(expand=YES, fill=BOTH)

        # main left frame
        self.main_left_frame = Frame(self.myContainer1, background="light blue")
        self.main_left_frame.pack(side=LEFT, expand=YES, padx=5, pady=5, ipadx=5, ipady=5)
        
        # main right frame
        self.main_right_frame = Frame(self.myContainer1, background="white") 
        self.main_right_frame.pack(side=RIGHT, expand=YES, fill=BOTH)

        # bacteria group frame
        self.bac_frame = Frame(self.main_right_frame, borderwidth=5, background="light gray")
        self.bac_frame.pack(expand=NO, fill=BOTH)

        # submit frame
        self.submit_frame = Frame(self.bac_frame, borderwidth=5, background="light gray")
        self.submit_frame.pack(side=BOTTOM, expand=NO)
        
        Label(self.bac_frame, text="BACTERIA GROUP", font=8, background="light gray").pack(side=TOP,anchor=N)
        for option in group_options:
            button = Radiobutton(self.bac_frame, text=str(option), indicatoron=1,
            value=option, padx=5, variable=self.group_option, background="light gray", command=self.main_left_frame.destroy())
            button.pack(side=TOP, anchor=W)

        Label(self.bac_frame, text="GROWTH FACTORS", font=8, background="light gray").pack(side=TOP,anchor=N)
        for option in fast_options:
            button = Radiobutton(self.bac_frame, text=str(option), indicatoron=1,
            value=option, padx=5, variable=self.fast_option, background="light gray")
            button.pack(side=LEFT, anchor=W)

        # submit button
        self.submitbutton = Button(self.submit_frame,text="Submit", background="black", foreground="white",
        width=6, padx="2m", pady="1m")

        self.submitbutton.pack()
        
        self.submitbutton.bind("<Button-1>", self.submitbuttonclick)
        self.submitbutton.bind("<Return>", self.submitbuttonclick)

        # algorithm frame
        self.algo_frame = Frame(self.main_right_frame, borderwidth=5, background="white")
        self.algo_frame.pack(expand=NO, fill=BOTH)
        Label(self.algo_frame, text="SAMPLE ANALYSIS", font=8, background="white").pack(side=TOP,anchor=N)

        self.algo_left_frame = Frame(self.algo_frame, background="white")
        self.algo_left_frame.pack(side=LEFT, anchor=E, expand=NO, fill=BOTH)
        for option in algo_options:
            button = Radiobutton(self.algo_left_frame, text=str(option), indicatoron=1,
            value=option, padx=5, variable=self.algo_option, background="white")
            button.pack(side=TOP, anchor=W)

        self.algo_center_frame = Frame(self.algo_frame, background="white")
        self.algo_center_frame.pack(side=LEFT, anchor=N, expand=NO, fill=BOTH)

        self.marine = Scale(self.algo_center_frame, from_=0.01, to=1.00, orient=HORIZONTAL, bd=0, label="Marine",
        background="white", troughcolor="dodgerblue4", length=65, width=10, sliderlength=10, resolution=0.01)
        self.marine.pack()
        self.marine.set(1.00)

        self.water = Scale(self.algo_center_frame, from_=0.01, to=1.00, orient=HORIZONTAL, bd=0, label="Freshwater",
        background="white", troughcolor="cyan", length=65, width=10, sliderlength=10, resolution=0.01)
        self.water.pack()
        self.water.set(1.00)

        self.soil = Scale(self.algo_center_frame, from_=0.01, to=1.00, orient=HORIZONTAL, bd=0, label="Soil",
        background="white", troughcolor="saddle brown", length=65, width=10, sliderlength=10, resolution=0.01)
        self.soil.pack()
        self.soil.set(1.00)

        self.algo_right_frame = Frame(self.algo_frame, background="white")
        self.algo_right_frame.pack(side=RIGHT, anchor=N, expand=NO, fill=BOTH)

        self.plant = Scale(self.algo_right_frame, from_=0.01, to=1.00, orient=HORIZONTAL, bd=0, label="Vegetation",
        background="white", troughcolor="green", length=65, width=10, sliderlength=10, resolution=0.01)
        self.plant.pack()
        self.plant.set(1.00)

        self.animal = Scale(self.algo_right_frame, from_=0.01, to=1.00, orient=HORIZONTAL, bd=0, label="Clinical",
        background="white", troughcolor="red", length=65, width=10, sliderlength=10, resolution=0.01)
        self.animal.pack()
        self.animal.set(1.00)

        self.fecal = Scale(self.algo_right_frame, from_=0.01, to=1.00, orient=HORIZONTAL, bd=0, label="Fecal",
        background="white", troughcolor="dark olive green", length=65, width=10, sliderlength=10, resolution=0.01)
        self.fecal.pack()
        self.fecal.set(1.00)

        # search frame
        self.search_frame = Frame(self.main_right_frame, borderwidth=5, background="light gray")
        self.search_frame.pack(expand=NO)

        self.bac_list=(
        'Aeromonas allosaccharophila','Aeromonas bestiarum','Aeromonas caviae','Aeromonas encheleia','Aeromonas eucrenophila','Aeromonas hydrophila','Aeromonas jandaei','Aeromonas media','Aeromonas popoffii','Aeromonas salmonicida achromogenes','Aeromonas salmonicida masoucida','Aeromonas salmonicida salmonicida','Aeromonas salmonicida smithia','Aeromonas schubertii','Aeromonas sobria','Aeromonas trota','Aeromonas veronii bv sobria','Aeromonas veronii bv veronii',
        'Aneurinibacillus aneurinilyticus',
        'Bacillius alcalophilus','Bacillus aminovorans','Bacillus amyloliquefaciens','Bacillus anthracis','Bacillus asahii','Bacillus atrophaeus','Bacillus badius','Bacillus barbaricus','Bacillus bataviensis','Bacillus carboniphilus','Bacillus carotarum','Bacillus cascainensis','Bacillus cereus','Bacillus circulans','Bacillus clausii','Bacillus coagulans','Bacillus cohnii','Bacillus decolorationis','Bacillus drentensis','Bacillus endophyticus','Bacillus farraginis','Bacillus fastidiosus','Bacillus firmus','Bacillus flexus','Bacillus fordii','Bacillus freudenreichii','Bacillus fumarioli','Bacillus funiculus','Bacillus galactosidilyticus','Bacillus gelatini','Bacillus gibsonii','Bacillus insolitus','Bacillus kaustophilus','Bacillus lentus','Bacillus licheniformis','Bacillus macroides','Bacillus megaterium','Bacillus mycoides','Bacillus psychrophilus','Bacillus psychrosaccharolyticus','Bacillus pumilis','Bacillus simplex','Bacillus smithii','Bacillus sphaericus','Bacillus stearothermophilus','Bacillus subtilis','Bacillus Taxon 18','Bacillus Taxon 21','Bacillus Taxon 24','Bacillus Taxon 26','Bacillus Taxon 27','Bacillus Taxon 28','Bacillus Taxon 29','Bacillus Taxon 33','Bacillus Taxon 4','Bacillus Taxon 41','Bacillus thuringiensis',
        'Brennaria (Erwinia) nigrifluens','Brennaria (Erwinia) quercina','Brennaria (Erwinia) rubrifaciens','Brennaria (Erwinia) salicis',
        'Brevibacillus brevis','Brevibacillus laterosporus',
        'Budvicia aquatica',
        'Buttiauxella agrestis',
        'Cedecea davisae','Cedecea lapagei','Cedecea neteri','Cedecea species 3','Cedecea species 5',
        'Chromobacterium fluviatile','Chromobacterium violaceum',
        'Citrobacter (diversus) koseri','Citrobacter amalonaticus','Citrobacter braakii','Citrobacter farmeri','Citrobacter freundii','Citrobacter gillenii','Citrobacter murliniae','Citrobacter rodentium','Citrobacter sedlakii','Citrobacter werkmanii','Citrobacter youngae',
        'Colwellia psychrerythraea','Colwellia demingiae','Colwellia rossensis','Colwellia hornerae','Colwellia psychroptropica',
        'Edwardsiella hoshinae','Edwardsiella ictaluri','Edwardsiella tarda',
        'Enterobacter (Erwinia) dissolvens','Enterobacter (Erwinia) nimipressuralis','Enterobacter aerogenes','Enterobacter amnigenus biogroup 1','Enterobacter amnigenus biogroup 2','Enterobacter asburiae','Enterobacter cancerogenus','Enterobacter cloacae','Enterobacter gergoviae','Enterobacter hormaechei','Enterobacter intermedius','Enterobacter sakazakii','Enterobacter taylorae',
        'Erwinia amylovora ','Erwinia ananas','Erwinia billingiae','Erwinia mallotivora ','Erwinia persicinus','Erwinia psidii ','Erwinia rhapontici','Erwinia tracheiphila','Erwinia uredovora',
        'Escherichia blattae','Escherichia coli','Escherichia coli (inactive)','Escherichia fergusonii','Escherichia hermanii','Escherichia vulneris',
        'Ewingella americana',
        'Geobacillus stearothermophilus',
        'Hafnia alvei',
        'Klebsiella ornithinolytica','Klebsiella oxytoca','Klebsiella planticola','Klebsiella pneumoniae aerogenes','Klebsiella pneumoniae ozaenae','Klebsiella pneumoniae pneumoniae','Klebsiella pneumoniae rhinoscleromatis','Klebsiella terrigena',
        'Kluyvera ascorbata','Kluyvera cryocrescens',
        'Leclercia (Escherichia) adecarboxylata',
        'Leminorella grimontii','Leminorella richardii',
        'Listonella anguillarum','Listonella pelagia biovar I','Listonella pelagia biovar II',
        'Lysinibacillus fusiformis','Lysinibacillus sphaericus',
        'Moellerella wisconsensis',
        'Morganella morganii',
        'Obesumbacterium proteus biogroup 1','Obesumbacterium proteus biogroup 2 ',
        'Paenibacillus alvei','Paenibacillus amylolyticus','Paenibacillus apiarius','Paenibacillus larvae pulvifaciens','Paenibacillus macerans','Paenibacillus pabuli','Paenibacillus polymyxa','Paenibacillus thiaminolyticus',
        'Pantoea (Enterobacter) agglomerans','Pantoea (Erwinia) stewartii','Pantoea dispersa',
        'Pectobacterium (Erwinia) cacticida','Pectobacterium (Erwinia) carotovora','Pectobacterium (Erwinia) chrysanthemi','Pectobacterium (Erwinia) cypripedii','Pectobacterium atrosepticum','Pectobacterium betavasculorum','Pectobacterium wasabiae',
        'Photobacterium angustum','Photobacterium damselae damselae','Photobacterium damselae piscicida','Photobacterium frigidiphilum','Photobacterium ganghwense','Photobacterium iliopiscarium','Photobacterium indicum','Photobacterium leiognathi','Photobacterium  lipolyticum','Photobacterium phosphoreum','Photobacterium profundum','Photobacterium rosenbergii',
        'Photorhabdus (Xenorhabdus) luminescens',
        'Plesiomonas shigelloides',
        'Pragia fontium',
        'Proteus mirabilis','Proteus myxofaciens','Proteus penneri','Proteus vulgaris Biogroup 2','Proteus vulgaris Biogroup 3',
        'Providencia alcalifaciens','Providencia heimbachae','Providencia rettgeri','Providencia rustigianii','Providencia stuartii',
        'Rahnella aquatilis',
        'Salmonella bongori','Salmonella enterica arizonae','Salmonella enterica diarizonae','Salmonella enterica enterica','Salmonella enterica houtenae','Salmonella enterica indica','Salmonella enterica salamae',
        'Serratia entomophila','Serratia ficaria','Serratia fonticola','Serratia grimesli','Serratia liquefaciens','Serratia marcescens','Serratia odorifera group 1','Serratia odorifera group 2','Serratia plymuthica','Serratia proteamaculans','Serratia rubidaea',
        'Shewanella xiamenensis','Shewanella oneidensis','Shewanella putrefaciens','Shewanella profunda','Shewanella decolorationis','Shewanella baltica','Shewanella hafniensis','Shewanella morhuae','Shewanella glacialipisicola',
        'Shigella boydii','Shigella dysenteriae','Shigella flexneri','Shigella sonnei',
        'Tatumella ptyseos',
        'Trabulsiella guamensis',
        'Vibrio aerogenes','Vibrio aestuarinus','Vibrio agarivorans','Vibrio alginolyticus','Vibrio anguillarum','Vibrio brasiliensis','Vibrio calvienensis','Vibrio campbellii','Vibrio chagasii','Vibrio cholerae','Vibrio cincinnatiensis','Vibrio comitans','Vibrio coralliilyticus','Vibrio crassostreae','Vibrio cyclotrophicus','Vibrio diabolicus','Vibrio diazothrophicus','Vibrio ezurae','Vibrio fischeri','Vibrio fluvialis','Vibrio fortis','Vibrio furnisii','Vibrio gallicus','Vibrio gazogenes','Vibrio gigantis','Vibrio halioticoli','Vibrio harveyi','Vibrio hepatarius','Vibrio hispanicus','Vibrio ichthyoenteri','Vibrio inusitatus','Vibrio kanaloae','Vibrio lentus','Vibrio litoralis','Vibrio logei','Vibrio mediterranei','Vibrio metschnokovii','Vibrio mimicus','Vibrio mytili','Vibrio natriegens','Vibrio navarrensis','Vibrio neonatus','Vibrio neptunis','Vibrio nereis','Vibrio nigrapulchritudo','Vibrio ordalii','Vibrio orientalis','Vibrio pacinii','Vibrio parahaemolyticus','Vibrio pectenicida','Vibrio pelagius I','Vibrio pelagius II','Vibrio penaeicida','Vibrio pomeroyi','Vibrio ponticus','Vibrio proteolyticus','Vibrio rarus','Vibrio rhizosphaerae','Vibrio rotiferianus','Vibrio ruber','Vibrio rumoiensis','Vibrio salmonicida','Vibrio scophthalmi','Vibrio splendidus I','Vibrio splendidus II','Vibrio superstes','Vibrio tapetis','Vibrio tasmaniensis','Vibrio tubiashi','Vibrio vulnificus B1','Vibrio vulnificus B2','Vibrio vulnificus B3','Vibrio wodanis','Vibrio xuii',
        'Virgibacillus pantothenticus',
        'Xenorhabdus beddingii','Xenorhabdus bovienii','Xenorhabdus budapestensis','Xenorhabdus cabanillasii','Xenorhabdus doucetiae','Xenorhabdus ehlersii','Xenorhabdus griffiniae','Xenorhabdus hominickii','Xenorhabdus indica','Xenorhabdus innexi','Xenorhabdus japonica','Xenorhabdus koppenhoeferi','Xenorhabdus kozodoii','Xenorhabdus mauleonii','Xenorhabdus miraniensis','Xenorhabdus nematophila','Xenorhabdus poinarii','Xenorhabdus romanii','Xenorhabdus species 3','Xenorhabdus species 9','Xenorhabdus stockiae','Xenorhabdus szentirmaii',
        'Yersinia aldovae','Yersinia bercovieri','Yersinia enterocolitica','Yersinia frederiksenii' ,'Yersinia intermedia','Yersinia kristensenii','Yersinia mollaretii','Yersinia pestis','Yersinia pseudotuberculosis','Yersinia rohdei','Yersinia ruckeri','Yokenella regensburgei'
        )

        self.enter = AutocompleteEntry(self.search_frame, width=27)

        self.enter.set_completion_list(self.bac_list)
        self.enter.pack(side=LEFT, expand=NO, padx=5, pady=5, ipadx=5, ipady=5)

        self.searchbutton = Button(self.search_frame, text="Search", foreground="white", background="blue",
        width=6, padx="2m", pady="1m")
        self.searchbutton.pack(side=LEFT, pady=5)
        self.searchbutton.bind("<Button-1>", self.searchbuttonclick)
        self.searchbutton.bind("<Return>", self.searchbuttonclick)

        # heading frame
        self.heading_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.heading_frame.pack(expand=NO)
        Label(self.heading_frame, text="IDENTIFICATION SCORE", font=8, background="white").pack(side=TOP,anchor=N)
        
        # id frame
        self.id_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.id_frame.pack(expand=YES, fill=BOTH)

        # button settings
        self.adon_options = ["+", "--", "?"] 
        self.ala_options = ["+", "--", "?"]
        self.amp_options = ["+", "--", "?"]
        self.amy_options = ["+", "--", "?"]
        self.amyg_options = ["+", "--", "?"]
        self.arab_options = ["+", "--", "?"]
        self.arg_options = ["+", "--", "?"]
        self.asp_options = ["+", "--", "?"]
        self.cas_options = ["+", "--", "?"]
        self.cat_options = ["+", "--", "?"]
        self.cell_options = ["+", "--", "?"]
        self.ceph_options = ["+", "--", "?"]
        self.chi_options = ["+", "--", "?"]
        self.chlor_options = ["+", "--", "?"]
        self.cit_options = ["+", "--", "?"]
        self.coag_options = ["+", "--", "?"]
        self.dna_options = ["+", "--", "?"] 
        self.dul_options = ["+", "--", "?"]
        self.endo_options = ["+", "--", "?"]
        self.endo_b_options = ["+", "--", "?"]
        self.endo_c_options = ["+", "--", "?"]
        self.endo_o_options = ["+", "--", "?"]
        self.esc_options = ["+", "--", "?"]
        self.ethan_options = ["+", "--", "?"]
        self.fru_options = ["+", "--", "?"]
        self.galac_options = ["+", "--", "?"]
        self.gel_options = ["+", "--", "?"]
        self.glu_options = ["+", "--", "?"]
        self.glug_options = ["+", "--", "?"]
        self.glut_options = ["+", "--", "?"]
        self.glux_options = ["+", "--", "?"]
        self.glyc_options = ["+", "--", "?"]
        self.gram_options = ["+", "--", "?"]
        self.h2s_options = ["+", "--", "?"]
        self.hem_options = ["+", "--", "?"]
        self.hip_options = ["+", "--", "?"]
        self.hist_options = ["+", "--", "?"]
        self.ind_options = ["+", "--", "?"]
        self.ino_options = ["+", "--", "?"]
        self.lac_options = ["+", "--", "?"]
        self.lys_options = ["+", "--", "?"]
        self.mal_options = ["+", "--", "?"]
        self.man_options = ["+", "--", "?"]
        self.mann_options = ["+", "--", "?"]
        self.meli_options = ["+", "--", "?"]
        self.meta_options = ["aerobe", "fac anaerobe", "?"]
        self.motil_options = ["+", "--", "?"]
        self.nal_options = ["+", "--", "?"]
        self.nit1_options = ["+", "--", "?"]
        self.nit2_options = ["+", "--", "?"]        
        self.nit3_options = ["+", "--", "?"]
        self.onpg_options = ["+", "--", "?"]
        self.orn_options = ["+", "--", "?"]
        self.oxi_options = ["+", "--", "?"]
        self.phen_options = ["+", "--", "?"]
        self.phos_options = ["+", "--", "?"]
        self.poly_options = ["+", "--", "?"]
        self.raf_options = ["+", "--", "?"]
        self.rham_options = ["+", "--", "?"]
        self.sal_options = ["+", "--", "?"]
        self.salt_options = ["<6%", ">6%", "?"]
        self.shape_options = ["bacillus", "coccus", "spirillus", "?"]
        self.sorb_options = ["+", "--", "?"]
        self.starch_options = ["+", "--", "?"]
        self.strep_options = ["+", "--", "?"]
        self.suc_options = ["+", "--", "?"]
        self.temp_options = ["25C", "35C", "45C", "?"] 
        self.trypto_options = ["+", "--", "?"]
        self.tw20_options = ["+", "--", "?"]
        self.tw80_options = ["+", "--", "?"]
        self.tyro_options = ["+", "--", "?"]
        self.tre_options = ["+", "--", "?"]
        self.urea_options = ["+", "--", "?"]
        self.val_options = ["+", "--", "?"]
        self.vp_options = ["+", "--", "?"]
        self.xyl_options = ["+", "--", "?"]

    def resetbuttonclick(self, event):
        self.adon_option.set("?")
        self.ala_option.set("?")
        self.amp_option.set("?")
        self.amy_option.set("?")
        self.amyg_option.set("?")
        self.arab_option.set("?")
        self.arg_option.set("?")
        self.asp_option.set("?")
        self.cas_option.set("?")
        self.cat_option.set("?")
        self.cell_option.set("?")
        self.ceph_option.set("?")
        self.chi_option.set("?")
        self.chlor_option.set("?")
        self.cit_option.set("?")
        self.coag_option.set("?")
        self.dna_option.set("?")
        self.dul_option.set("?")
        self.endo_b_option.set("?")
        self.endo_c_option.set("?")
        self.endo_o_option.set("?")
        self.esc_option.set("?")
        self.ethan_option.set("?")
        self.fru_option.set("?")        
        self.galac_option.set("?")
        self.gel_option.set("?")
        self.glug_option.set("?")
        self.glu_option.set("?")
        self.glut_option.set("?")
        self.glux_option.set("?")
        self.glyc_option.set("?")
        self.h2s_option.set("?")
        self.hem_option.set("?")
        self.hip_option.set("?")
        self.hist_option.set("?")
        self.ind_option.set("?")
        self.ino_option.set("?")
        self.lac_option.set("?")
        self.lys_option.set("?")
        self.mal_option.set("?")
        self.man_option.set("?")
        self.mann_option.set("?")
        self.meli_option.set("?")
        self.motil_option.set("?")
        self.nal_option.set("?")
        self.nit1_option.set("?")
        self.nit2_option.set("?")
        self.nit3_option.set("?")
        self.onpg_option.set("?")
        self.orn_option.set("?")
        self.oxi_option.set("?")
        self.phen_option.set("?")
        self.phos_option.set("?")
        self.poly_option.set("?")
        self.raf_option.set("?")
        self.rham_option.set("?")
        self.sal_option.set("?")
        self.salt_option.set("?")
        self.sorb_option.set("?")
        self.starch_option.set("?")
        self.strep_option.set("?")
        self.suc_option.set("?")
        self.temp_option.set("?")
        self.tre_option.set("?")
        self.trypto_option.set("?")
        self.tw20_option.set("?")
        self.tw80_option.set("?")
        self.tyro_option.set("?")
        self.urea_option.set("?")
        self.val_option.set("?")
        self.vp_option.set("?")
        self.xyl_option.set("?")       

        self.id_frame.destroy()
        self.id_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.id_frame.pack(side=TOP, fill=BOTH)

        self.enter.delete(0,END)
        self.water.set(1.00)
        self.soil.set(1.00)
        self.plant.set(1.00)
        self.animal.set(1.00)
            
    def submitbuttonclick(self, event):
        self.id_frame.destroy()
        self.id_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.id_frame.pack(side=TOP, fill=BOTH)

        self.main_left_frame.destroy()

        # main left frame
        self.main_left_frame = Frame(self.myContainer1, background="light blue")
        self.main_left_frame.pack(side=LEFT, expand=YES, padx=5, pady=5, ipadx=5, ipady=5)

        # bottom frame
        self.bottom_frame = Frame(self.main_left_frame, background="light blue")
        self.bottom_frame.pack(side=BOTTOM, expand=YES, ipadx=5, ipady=5)

        # bottom_left_frame
        self.bottom_left_frame = Frame(self.bottom_frame, background="light blue")
        self.bottom_left_frame.pack(side=LEFT, expand=YES, ipadx=1, ipady=1)

        # bottom_right_frame
        self.bottom_right_frame = Frame(self.bottom_frame, background="light blue")
        self.bottom_right_frame.pack(side=LEFT, expand=YES, ipadx=1, ipady=1)

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
        self.control_right_frame.pack(side=LEFT, anchor=N, expand=YES, padx=2, pady=2, ipadx=2, ipady=2)

        # button defaults
        self.adon_option.set("?")
        self.ala_option.set("?")
        self.amp_option.set("?")
        self.amy_option.set("?")
        self.amyg_option.set("?")
        self.arab_option.set("?")
        self.arg_option.set("?")
        self.asp_option.set("?")
        self.cas_option.set("?")
        self.cat_option.set("?")
        self.cell_option.set("?")
        self.ceph_option.set("?")
        self.chi_option.set("?")
        self.chlor_option.set("?")
        self.cit_option.set("?")
        self.coag_option.set("?")
        self.dna_option.set("?")
        self.dul_option.set("?")
        self.endo_b_option.set("?")
        self.endo_c_option.set("?")
        self.endo_o_option.set("?")
        self.esc_option.set("?")
        self.ethan_option.set("?")
        self.fru_option.set("?")        
        self.galac_option.set("?")
        self.gel_option.set("?")
        self.glug_option.set("?")
        self.glu_option.set("?")
        self.glut_option.set("?")
        self.glux_option.set("?")
        self.glyc_option.set("?")
        self.h2s_option.set("?")
        self.hem_option.set("?")
        self.hip_option.set("?")
        self.hist_option.set("?")
        self.ind_option.set("?")
        self.ino_option.set("?")
        self.lac_option.set("?")
        self.lys_option.set("?")
        self.mal_option.set("?")
        self.man_option.set("?")
        self.mann_option.set("?")
        self.meli_option.set("?")
        self.motil_option.set("?")
        self.nal_option.set("?")
        self.nit1_option.set("?")
        self.nit2_option.set("?")
        self.nit3_option.set("?")
        self.onpg_option.set("?")
        self.orn_option.set("?")
        self.oxi_option.set("?")
        self.phen_option.set("?")
        self.phos_option.set("?")
        self.poly_option.set("?")
        self.raf_option.set("?")
        self.rham_option.set("?")
        self.sal_option.set("?")
        self.salt_option.set("?")
        self.sorb_option.set("?")
        self.starch_option.set("?")
        self.strep_option.set("?")
        self.suc_option.set("?")
        self.temp_option.set("?")
        self.tre_option.set("?")
        self.trypto_option.set("?")
        self.tw20_option.set("?")
        self.tw80_option.set("?")
        self.tyro_option.set("?")
        self.urea_option.set("?")
        self.val_option.set("?")
        self.vp_option.set("?")
        self.xyl_option.set("?")

        # layout
        if (self.group_option.get()=="Gram Negative Facultative Anaerobe Bacillus" or
        self.group_option.get()=="Gram Positive Facultative Anaerobe Bacillus" or
        self.group_option.get()=="Gram Positive Facultative Anaerobe Coccus" or
        self.group_option.get()=="Spore Forming Bacillus and Coccus"):
            adon_label = "ADONITOL FERM:"
            arab_label = "L-ARABINOSE FERM:"
            cell_label = "CELLOBIOSE FERM:"
            dul_label = "DULCITOL FERM:"
            ethan_label ="ETHANOL FERM:"
            fru_label = "FRUCTOSE FERM:"
            galac_label = "GALACTOSE FERM:"
            glyc_label = "GLYCEROL FERM:"
            ino_label = "MYO-INOSITOL FERM:"
            lac_label = "LACTOSE FERM:"
            mal_label = "MALTOSE FERM:"
            man_label = "D-MANNITOL FERM:"
            mann_label = "D-MANNOSE FERM:"
            meli_label = "MELIBIOSE FERM:"
            raf_label = "RAFFINOSE FERM:"
            rham_label = "L-RHAMNOSE FERM:"
            sal_label = "SALICIN FERM:"
            sorb_label = "D-SORBITOL FERM:"
            suc_label = "SUCROSE FERM:"
            tre_label = "TREHALOSE FERM:"
            xyl_label = "D-XYLOSE FERM:"

        if (self.group_option.get()=="Gram Negative Aerobe Bacillus" or
        self.group_option.get()=="Gram Negative Aerobe Coccus" or
        self.group_option.get()=="Gram Positive Aerobe Bacillus" or
        self.group_option.get()=="Gram Positive Aerobe Coccus"):
            adon_label = "ADONITOL GROWTH:"
            arab_label = "L-ARABINOSE GROWTH:"
            cell_label = "CELLOBIOSE GROWTH:"
            dul_label = "DULCITOL GROWTH"
            ethan_label ="ETHANOL GROWTH:"
            fru_label = "FRUCTOSE GROWTH:"
            galac_label = "GALACTOSE GROWTH:"
            glyc_label = "GLYCEROL GROWTH:"
            ino_label = "MYO-INOSITOL GROWTH:"
            lac_label = "LACTOSE GROWTH:"
            mal_label = "MALTOSE GROWTH:"
            man_label = "D-MANNITOL GROWTH:"
            mann_label = "D-MANNOSE GROWTH:"
            meli_label = "MELIBIOSE GROWTH:"
            raf_label = "RAFFINOSE GROWTH:"
            rham_label = "L-RHAMNOSE GROWTH:"
            sal_label = "SALICIN GROWTH:"
            sorb_label = "D-SORBITOL GROWTH:"
            suc_label = "SUCROSE GROWTH:"
            tre_label = "TREHALOSE GROWTH:"
            xyl_label = "D-XYLOSE GROWTH:"
            
        self.gram_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.gram_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.gram_options_frame, text="GRAM STAIN:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.gram_options:
            button = Radiobutton(self.gram_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.gram_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
           
        self.shape_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.shape_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.shape_options_frame, text="SHAPE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.shape_options:
            button = Radiobutton(self.shape_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.shape_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.meta_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.meta_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.meta_options_frame, text="METABOLISM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.meta_options:
            button = Radiobutton(self.meta_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.meta_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
        
        self.endo_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.endo_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.endo_options_frame, text="ENDOSPORE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.endo_options:
            button = Radiobutton(self.endo_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.endo_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.endo_b_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.endo_b_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.endo_b_options_frame, text="BULGING SPORES:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.endo_b_options:
            button = Radiobutton(self.endo_b_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.endo_b_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.endo_c_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.endo_c_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.endo_c_options_frame, text="CENTRAL SPORES:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.endo_c_options:
            button = Radiobutton(self.endo_c_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.endo_c_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.endo_o_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.endo_o_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.endo_o_options_frame, text="OVAL SPORES:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.endo_o_options:
            button = Radiobutton(self.endo_o_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.endo_o_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
        
        self.cat_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.cat_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.cat_options_frame, text="CATALASE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.cat_options:
            button = Radiobutton(self.cat_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.cat_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
        
        self.oxi_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.oxi_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.oxi_options_frame, text="OXIDASE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.oxi_options:
            button = Radiobutton(self.oxi_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.oxi_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.salt_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.salt_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.salt_options_frame, text="SALINITY RANGE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.salt_options:
            button = Radiobutton(self.salt_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.salt_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.temp_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.temp_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.temp_options_frame, text="TEMP RANGE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.temp_options:
            button = Radiobutton(self.temp_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.temp_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.motil_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.motil_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.motil_options_frame, text="MOTILITY:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.motil_options:
            button = Radiobutton(self.motil_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.motil_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.h2s_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.h2s_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.h2s_options_frame, text="HYDROGEN SULFIDE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.h2s_options:
            button = Radiobutton(self.h2s_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.h2s_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.ind_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.ind_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.ind_options_frame, text="INDOLE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.ind_options:
            button = Radiobutton(self.ind_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.ind_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
        
        self.cit_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.cit_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.cit_options_frame, text="CITRATE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.cit_options:
            button = Radiobutton(self.cit_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.cit_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
        
        self.nit1_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.nit1_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.nit1_options_frame, text="NO3->NO2:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.nit1_options:
            button = Radiobutton(self.nit1_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.nit1_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.nit2_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.nit2_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.nit2_options_frame, text="NO3->NO2->N2:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.nit2_options:
            button = Radiobutton(self.nit2_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.nit2_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.nit3_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.nit3_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.nit3_options_frame, text="N2->NO2->NO3:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.nit3_options:
            button = Radiobutton(self.nit3_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.nit3_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.glux_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.glux_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.glux_options_frame, text="GLUCOSE OXI:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.glux_options:
            button = Radiobutton(self.glux_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.glux_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.glu_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.glu_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.glu_options_frame, text="GLUCOSE FERM:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.glu_options:
            button = Radiobutton(self.glu_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.glu_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.glug_options_frame = Frame(self.control_left_frame, borderwidth=3, background="light blue")
        self.glug_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.glug_options_frame, text="GLUCOSE GAS:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.glug_options:
            button = Radiobutton(self.glug_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.glug_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.adon_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.adon_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.adon_options_frame, text=adon_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.adon_options:
            button = Radiobutton(self.adon_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.adon_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
                
        self.arab_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.arab_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.arab_options_frame, text=arab_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.arab_options:
            button = Radiobutton(self.arab_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.arab_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.cell_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.cell_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.cell_options_frame, text=cell_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.cell_options:
            button = Radiobutton(self.cell_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.cell_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.dul_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.dul_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.dul_options_frame, text=dul_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.dul_options:
             button = Radiobutton(self.dul_options_frame, text=str(option), indicatoron=0,
             value=option, padx=5, variable=self.dul_option, background="light blue")
             button.pack(side=LEFT, anchor=E)

        self.ethan_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.ethan_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.ethan_options_frame, text=ethan_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.ethan_options:
            button = Radiobutton(self.ethan_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.ethan_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.fru_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.fru_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.fru_options_frame, text=fru_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.fru_options:
            button = Radiobutton(self.fru_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.fru_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.galac_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.galac_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.galac_options_frame, text=galac_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.galac_options:
            button = Radiobutton(self.galac_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.galac_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.glyc_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.glyc_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.glyc_options_frame, text=glyc_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.glyc_options:
            button = Radiobutton(self.glyc_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.glyc_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.ino_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.ino_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.ino_options_frame, text=ino_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.ino_options:
            button = Radiobutton(self.ino_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.ino_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.lac_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.lac_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.lac_options_frame, text=lac_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.lac_options:
            button = Radiobutton(self.lac_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.lac_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.mal_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.mal_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.mal_options_frame, text=mal_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.mal_options:
            button = Radiobutton(self.mal_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.mal_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.man_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.man_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.man_options_frame, text=man_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.man_options:
            button = Radiobutton(self.man_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.man_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.mann_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.mann_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.mann_options_frame, text=mann_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.mann_options:
            button = Radiobutton(self.mann_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.mann_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.meli_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.meli_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.meli_options_frame, text=meli_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.meli_options:
            button = Radiobutton(self.meli_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.meli_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.raf_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.raf_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.raf_options_frame, text=raf_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.raf_options:
            button = Radiobutton(self.raf_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.raf_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.rham_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.rham_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.rham_options_frame, text=rham_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.rham_options:
            button = Radiobutton(self.rham_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.rham_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.sal_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.sal_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.sal_options_frame, text=sal_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.sal_options:
            button = Radiobutton(self.sal_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.sal_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.sorb_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.sorb_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.sorb_options_frame, text=sorb_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.sorb_options:
            button = Radiobutton(self.sorb_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.sorb_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.suc_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.suc_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.suc_options_frame, text=suc_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.suc_options:
            button = Radiobutton(self.suc_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.suc_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.tre_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.tre_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.tre_options_frame, text=tre_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.tre_options:
            button = Radiobutton(self.tre_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.tre_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.xyl_options_frame = Frame(self.control_center_frame, borderwidth=3, background="light blue")
        self.xyl_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.xyl_options_frame, text=xyl_label, relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.xyl_options:
            button = Radiobutton(self.xyl_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.xyl_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.arg_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.arg_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.arg_options_frame, text="ARGININE DIHYDROLASE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.arg_options:
            button = Radiobutton(self.arg_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.arg_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.lys_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.lys_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.lys_options_frame, text="LYSINE DECARBOXYLASE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.lys_options:
            button = Radiobutton(self.lys_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.lys_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
        
        self.orn_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.orn_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.orn_options_frame, text="ORNITHINE DECARBOXYLASE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.orn_options:
            button = Radiobutton(self.orn_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.orn_option, background="light blue")
            button.pack(side=LEFT, anchor=E) 
        
        self.phen_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.phen_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.phen_options_frame, text="PHENYLALANINE DEAMINASE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.phen_options:
            button = Radiobutton(self.phen_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.phen_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.trypto_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.trypto_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.trypto_options_frame, text="TRYPTOPHAN DEAMINASE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.trypto_options:
            button = Radiobutton(self.trypto_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.trypto_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.amp_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.amp_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.amp_options_frame, text="AMPICILLIN RESISTANCE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.amp_options:
            button = Radiobutton(self.amp_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.amp_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.ceph_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.ceph_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.ceph_options_frame, text="CEPHALOTHIN RESISTANCE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.ceph_options:
            button = Radiobutton(self.ceph_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.ceph_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.chlor_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.chlor_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.chlor_options_frame, text="CHLORAMPHENICOL RESISTANCE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.chlor_options:
            button = Radiobutton(self.chlor_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.chlor_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.nal_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.nal_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.nal_options_frame, text="NALIDIXIC ACID RESISTANCE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.nal_options:
            button = Radiobutton(self.nal_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.nal_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.poly_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.poly_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.poly_options_frame, text="POLYMYXIN RESISTANCE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.poly_options:
            button = Radiobutton(self.poly_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.poly_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.strep_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.strep_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.strep_options_frame, text="STREPTOMYCIN RESISTANCE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.strep_options:
            button = Radiobutton(self.strep_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.strep_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.amy_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.amy_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.amy_options_frame, text="AMYLIN HYDROLYSIS:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.amy_options:
            button = Radiobutton(self.amy_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.amy_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.amyg_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.amyg_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.amyg_options_frame, text="AMYGDALIN HYDROLYSIS:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.amyg_options:
            button = Radiobutton(self.amyg_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.amyg_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.cas_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.cas_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.cas_options_frame, text="CASEIN HYDROLYSIS:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.cas_options:
            button = Radiobutton(self.cas_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.cas_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.chi_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.chi_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.chi_options_frame, text="CHITIN HYDROLYSIS:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.chi_options:
            button = Radiobutton(self.chi_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.chi_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.esc_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.esc_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.esc_options_frame, text="ESCULIN HYDROLYSIS:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.esc_options:
            button = Radiobutton(self.esc_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.esc_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.gel_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.gel_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.gel_options_frame, text="GELATIN HYDROLYSIS:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.gel_options:
            button = Radiobutton(self.gel_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.gel_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.hip_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.hip_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.hip_options_frame, text="HIPPURATE HYDROLYSIS:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.hip_options:
            button = Radiobutton(self.hip_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.hip_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
                
        self.starch_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.starch_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.starch_options_frame, text="STARCH HYDROLYSIS:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.starch_options:
            button = Radiobutton(self.starch_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.starch_option, background="light blue")
            button.pack(side=LEFT, anchor=E)
                
        self.tw20_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.tw20_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.tw20_options_frame, text="TWEEN 20 HYDROLYSIS:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.tw20_options:
            button = Radiobutton(self.tw20_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.tw20_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.tw80_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.tw80_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.tw80_options_frame, text="TWEEN 80 HYDROLYSIS:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.tw80_options:
            button = Radiobutton(self.tw80_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.tw80_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.tyro_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.tyro_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.tyro_options_frame, text="TYROSINE HYDROLYSIS:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.tyro_options:
            button = Radiobutton(self.tyro_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.tyro_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.urea_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.urea_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.urea_options_frame, text="UREA HYDROLYSIS:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.urea_options:
            button = Radiobutton(self.urea_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.urea_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.coag_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.coag_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.coag_options_frame, text="COAGULASE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.coag_options:
            button = Radiobutton(self.coag_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.coag_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.dna_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.dna_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.dna_options_frame, text="DEOXYRIBONUCLEASE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.dna_options:
            button = Radiobutton(self.dna_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.dna_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.phos_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.phos_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.phos_options_frame, text="PHOSPHATASE:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.phos_options:
            button = Radiobutton(self.phos_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.phos_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.hem_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.hem_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.hem_options_frame, text="HEMOLYSIS:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.hem_options:
            button = Radiobutton(self.hem_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.hem_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.onpg_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.onpg_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.onpg_options_frame, text="ONPG:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.onpg_options:
            button = Radiobutton(self.onpg_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.onpg_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        self.vp_options_frame = Frame(self.control_right_frame, borderwidth=3, background="light blue")
        self.vp_options_frame.pack(side=TOP, expand=YES, anchor=W)
        Label(self.vp_options_frame, text="VOGES-PROSKAUER:", relief=FLAT, font="bold", background="light blue").pack(side=LEFT,anchor=W)
        for option in self.vp_options:
            button = Radiobutton(self.vp_options_frame, text=str(option), indicatoron=0,
            value=option, padx=5, variable=self.vp_option, background="light blue")
            button.pack(side=LEFT, anchor=E)

        # identify button
        self.idbutton = Button(self.bottom_left_frame,text="Identify", background="dark green", foreground="white", width=6, padx="2m", pady="1m")
        self.idbutton.pack(side=LEFT)
        self.idbutton.bind("<Button-1>", self.idbuttonclick)
        self.idbutton.bind("<Return>", self.idbuttonclick)

        # reset button
        self.resetbutton = Button(self.bottom_right_frame,text="Reset", background="red", foreground="white", width=6, padx="2m", pady="1m")
        self.resetbutton.pack(side=RIGHT)
        self.resetbutton.bind("<Button-1>", self.resetbuttonclick)
        self.resetbutton.bind("<Return>", self.resetbuttonclick)

        # button frame defaults
        if (self.group_option.get()=="Gram Negative Facultative Anaerobe Bacillus" and
            self.fast_option.get()=="None" or self.fast_option.get()=="Salt" or self.fast_option.get()=="Yeast"):
            self.nit2_options_frame.destroy(), self.nit3_options_frame.destroy(),
            self.adon_options_frame.destroy(),self.cell_options_frame.destroy(),self.glux_options_frame.destroy(),
            self.ethan_options_frame.destroy(),self.fru_options_frame.destroy(),self.galac_options_frame.destroy(),
            self.amp_options_frame.destroy(), self.ceph_options_frame.destroy(), self.chlor_options_frame.destroy(), self.nal_options_frame.destroy(), self.poly_options_frame.destroy(), self.strep_options_frame.destroy(),
            self.trypto_options_frame.destroy(),self.amy_options_frame.destroy(),self.amyg_options_frame.destroy(), self.cas_options_frame.destroy(), self.chi_options_frame.destroy(),
            self.hip_options_frame.destroy(),self.starch_options_frame.destroy(),self.tw20_options_frame.destroy(),
            self.tw80_options_frame.destroy(),self.tyro_options_frame.destroy(),self.endo_b_options_frame.destroy(),
            self.endo_c_options_frame.destroy(),self.endo_o_options_frame.destroy(),self.coag_options_frame.destroy(),
            self.dna_options_frame.destroy(),self.phos_options_frame.destroy(),self.hem_options_frame.destroy()

            self.gram_option.set("--")
            self.shape_option.set("bacillus")
            self.meta_option.set("fac anaerobe")
            self.endo_option.set("--")

        if (self.group_option.get()=="Gram Negative Aerobe Bacillus"):
            self.adon_options_frame.destroy(),self.cell_options_frame.destroy(),self.glug_options_frame.destroy(),
            self.ethan_options_frame.destroy(),self.fru_options_frame.destroy(),self.galac_options_frame.destroy(),
            self.trypto_options_frame.destroy(),self.cas_options_frame.destroy(),
            self.hip_options_frame.destroy(),self.starch_options_frame.destroy(),self.tw20_options_frame.destroy(),
            self.tw80_options_frame.destroy(),self.tyro_options_frame.destroy(),self.endo_b_options_frame.destroy(),
            self.endo_c_options_frame.destroy(),self.endo_o_options_frame.destroy(),self.coag_options_frame.destroy(),
            self.dna_options_frame.destroy(),self.phos_options_frame.destroy(),self.hem_options_frame.destroy()

            self.gram_option.set("--")
            self.shape_option.set("bacillus")
            self.meta_option.set("aerobe")
            self.endo_option.set("--")

        if (self.group_option.get()=="Gram Negative Aerobe Coccus"):
            self.main_left_frame.destroy()

            self.gram_option.set("--")
            self.shape_option.set("coccus")
            self.meta_option.set("aerobe")
            self.endo_option.set("--")
            
        if (self.group_option.get()=="Gram Positive Facultative Anaerobe Bacillus"):
            self.main_left_frame.destroy()

            self.gram_option.set("+")
            self.shape_option.set("bacillus")
            self.meta_option.set("fac anaerobe")
            self.endo_option.set("--")
            
        if (self.group_option.get()=="Gram Positive Aerobe Bacillus"):
            self.main_left_frame.destroy()

            self.gram_option.set("+")
            self.shape_option.set("bacillus")
            self.meta_option.set("aerobe")
            self.endo_option.set("--")

        if (self.group_option.get()=="Gram Positive Facultative Anaerobe Coccus"):
            self.main_left_frame.destroy()

            self.gram_option.set("+")
            self.shape_option.set("coccus")
            self.meta_option.set("fac anaerobe")
            self.endo_option.set("--")

        if (self.group_option.get()=="Gram Positive Aerobe Coccus"):
            self.main_left_frame.destroy()

            self.gram_option.set("+")
            self.shape_option.set("coccus")
            self.meta_option.set("aerobe")
            self.endo_option.set("--")
            
        if (self.group_option.get()=="Spore Forming Bacillus and Coccus"):
            self.h2s_options_frame.destroy(),self.nit2_options_frame.destroy(), self.nit3_options_frame.destroy(),
            self.adon_options_frame.destroy(), self.glug_options_frame.destroy(),
            self.ethan_options_frame.destroy(), self.dul_options_frame.destroy(), self.rham_options_frame.destroy(),
            self.trypto_options_frame.destroy(), self.glux_options_frame.destroy(),
            self.sorb_options_frame.destroy(), self.suc_options_frame.destroy(), self.tre_options_frame.destroy(),
            self.coag_options_frame.destroy(), self.glyc_options_frame.destroy(), self.ino_options_frame.destroy(),
            self.mal_options_frame.destroy(),self.meli_options_frame.destroy(),
            self.amp_options_frame.destroy(), self.ceph_options_frame.destroy(),
            self.amy_options_frame.destroy(), self.amyg_options_frame.destroy(), self.chi_options_frame.destroy(), self.tw20_options_frame.destroy(), self.tw80_options_frame.destroy(), self.tyro_options_frame.destroy(),
            self.dna_options_frame.destroy(),self.phos_options_frame.destroy(),self.hem_options_frame.destroy()

            self.endo_option.set("+")
            self.gram_option.set("+")
            self.meta_option.set("?")
            self.shape_option.set("?")

        # id matrix
        a=self.animal.get
        af=lambda:1-(1-self.animal.get())*(1-self.fecal.get())
        afw=lambda:1-(1-self.animal.get())*(1-self.fecal.get())*(1-self.water.get()) 
        afs=lambda:1-(1-self.animal.get())*(1-self.fecal.get())*(1-self.soil.get())
        afsw=lambda:1-(1-self.animal.get())*(1-self.fecal.get())*(1-self.soil.get())*(1-self.water.get())
        afmpsw=lambda:1-(1-self.animal.get())*(1-self.fecal.get())*(1-self.marine.get())*(1-self.plant.get())*(1-self.soil.get())*(1-self.water.get())
        afpsw=lambda:1-(1-self.animal.get())*(1-self.fecal.get())*(1-self.plant.get())*(1-self.soil.get())*(1-self.water.get())
        apsw=lambda:1-(1-self.animal.get())*(1-self.plant.get())*(1-self.soil.get())*(1-self.water.get())
        apw=lambda:1-(1-self.animal.get())*(1-self.plant.get())*(1-self.water.get())
        am=lambda:1-(1-self.animal.get())*(1-self.marine.get())
        amw=lambda:1-(1-self.animal.get())*(1-self.marine.get())*(1-self.water.get())
        asw=lambda:1-(1-self.animal.get())*(1-self.soil.get())*(1-self.water.get())
        aw=lambda:1-(1-self.animal.get())*(1-self.water.get())
        f=self.fecal.get
        fms=lambda:1-(1-self.fecal.get())*(1-self.marine.get())*(1-self.soil.get())
        fpw=lambda:1-(1-self.fecal.get())*(1-self.plant.get())*(1-self.water.get())
        fs=lambda:1-(1-self.fecal.get())*(1-self.soil.get())
        fsw=lambda:1-(1-self.fecal.get())*(1-self.soil.get())*(1-self.water.get())
        fw=lambda:1-(1-self.fecal.get())*(1-self.water.get())
        m=self.marine.get
        ms=lambda:1-(1-self.marine.get())*(1-self.soil.get())
        mw=lambda:1-(1-self.marine.get())*(1-self.water.get())
        p=self.plant.get
        psw=lambda:1-(1-self.plant.get())*(1-self.soil.get())*(1-self.water.get())
        s=self.soil.get
        sw=lambda:1-(1-self.soil.get())*(1-self.water.get())
        w=self.water.get

        # bacteria,trait,sample,cat,oxi,motil,h2s,ind,cit,nit1,nit2,nit3,glux,glu,glug,adon,arab,cell,dul,ethan,fru,galac,glyc,ino,lac,mal,man,mann,meli,raf,rham,sal,sorb,suc,tre,xyl,arg,lys,orn,phen,trypto,amp,ceph,chlor,nal,poly,strep,amy,amyg,cas,chi,esc,gel,hip,starch,tw20,tw80,tyro,urea,endo_b,endo_c,endo_o,coag,dna,phos,hem,onpg,vp
        x=0.50
        
        # negfacbac cat- oxi- endo- nit1- glu+ (nonfastidious)
        self.A = [
        ('Xenorhabdus beddingii','Colony: --- \n Type Strain: Q58',w,0.01,0.01,x,0.01,0.01,0.99,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.01,x,0.99,x,x,x,x,x,x,0.01,x,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,0.01,0.01),
        ('Xenorhabdus bovienii','Colony: --- \n Type Strain: ---',w,0.01,0.01,x,0.01,0.01,0.15,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.15,x,0.85,x,x,x,x,x,x,0.01,x,0.15,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,0.01,0.01),
        ('Xenorhabdus species 3','Colony: --- \n Type Strain: TB20',w,0.01,0.01,x,0.01,0.01,0.99,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.01,x,0.01,x,x,x,x,x,x,0.01,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,0.01,0.01),
        ('Xenorhabdus budapestensis','Colony: --- \n Type Strain: ---',w,0.01,0.01,x,0.01,0.01,0.01,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.99,x,0.01,x,x,x,x,x,x,0.01,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.5,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,0.01,0.01),
        ('Xenorhabdus ehlersii','Colony: --- \n Type Strain: ---',w,0.01,0.01,x,0.01,0.01,0.15,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.01,x,0.85,x,x,x,x,x,x,0.01,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.85,x,x,x,x,x,x,0.01,x,x,x,x,0.15,x,x,0.01,0.01),
        ('Xenorhabdus indica','Colony: --- \n Type Strain: ---',w,0.01,0.01,x,0.01,0.01,0.01,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.99,x,0.01,x,x,x,x,x,x,0.01,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.5,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,0.01,0.01),
        ('Xenorhabdus innexi','Colony: --- \n Type Strain: ---',w,0.01,0.01,x,0.01,0.01,0.5,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.5,x,0.01,x,x,x,x,x,x,0.01,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,0.01,0.01),
        ('Xenorhabdus japonica','Colony: --- \n Type Strain: DSM 16522',w,0.01,0.01,x,0.01,0.01,0.01,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.01,x,0.99,x,x,x,x,x,x,0.01,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,0.01,0.01),
        ('Xenorhabdus species 9','Colony: --- \n Type Strain: VN01',w,0.01,0.01,x,0.01,0.01,0.01,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.01,x,0.99,x,x,x,x,x,x,0.01,x,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,0.01,0.01),
        ('Xenorhabdus nematophila','Colony: --- \n Type Strain: ---',w,0.01,0.01,x,0.01,0.01,0.15,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.15,x,0.85,x,x,x,x,x,x,0.01,x,0.85,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,0.01,0.01),
        ('Xenorhabdus poinarii','Colony: --- \n Type Strain: ---',w,0.01,0.01,x,0.01,0.01,0.15,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.01,x,0.99,x,x,x,x,x,x,0.01,x,0.85,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.15,x,x,x,x,x,x,0.01,x,x,x,x,0.01,x,x,0.01,0.01),
        ('Xenorhabdus szentirmaii','Colony: --- \n Type Strain: ---',w,0.01,0.01,x,0.01,0.01,0.85,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.85,x,0.99,x,x,x,x,x,x,0.85,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,0.01,0.01),
        ('Xenorhabdus cabanillasii','Colony: --- \n Type Strain: USTX62',w,0.01,0.01,x,0.01,0.01,0.01,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.5,x,0.5,x,x,x,x,x,x,0.01,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,0.01,0.01),
        ('Xenorhabdus doucetiae','Colony: --- \n Type Strain: FRM16',w,0.01,0.01,x,0.01,0.01,0.01,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.5,x,0.5,x,x,x,x,x,x,0.01,x,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.5,x,x,x,x,x,x,0.01,x,x,x,x,0.5,x,x,0.01,0.01),
        ('Xenorhabdus griffiniae','Colony: --- \n Type Strain: ID10',w,0.01,0.01,x,0.01,0.01,0.99,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.01,x,0.01,x,x,x,x,x,x,0.01,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,0.01,0.01),
        ('Xenorhabdus hominickii','Colony: --- \n Type Strain: DSM 17903',w,0.01,0.01,x,0.01,0.99,0.01,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.01,x,0.85,x,x,x,x,x,x,0.01,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,0.01,0.01),
        ('Xenorhabdus koppenhoeferi','Colony: Yellow \n Type Strain: USNJ01',w,0.01,0.01,x,0.01,0.01,0.01,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.01,x,0.99,x,x,x,x,x,x,0.01,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,0.01,0.01),
        ('Xenorhabdus kozodoii','Colony: --- \n Type Strain: DSM 17907',w,0.01,0.01,x,0.01,0.01,0.15,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.01,x,0.99,x,x,x,x,x,x,0.01,x,0.85,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.15,x,x,x,x,x,x,0.01,x,x,x,x,0.01,x,x,0.01,0.01),
        ('Xenorhabdus mauleonii','Colony: Yellow \n Type Strain: VC01',w,0.01,0.01,x,0.01,0.01,0.99,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.99,x,0.99,x,x,x,x,x,x,0.01,x,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,0.01,0.01),
        ('Xenorhabdus miraniensis','Colony: --- \n Type Strain: Q1',w,0.01,0.01,x,0.01,0.01,0.99,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.01,x,0.99,x,x,x,x,x,x,0.01,x,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,x,0.01,x,x,x,x,0.01,x,x,0.01,0.01),
        ('Xenorhabdus romanii','Colony: Yellow \n Type Strain: PR06-A',w,0.01,0.01,x,0.01,0.01,0.01,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.85,x,0.99,x,x,x,x,x,x,0.01,x,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,0.01,x,x,x,x,0.01,x,x,0.01,0.01),
        ('Xenorhabdus stockiae','Colony: --- \n Type Strain: TH01',w,0.01,0.01,x,0.01,0.01,0.01,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.99,x,0.99,x,x,x,x,x,x,0.01,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,0.01,0.01)]

        # negfacbac cat+ oxi- endo- nit1- glu+ (nonfastidious)
        self.B = [
        ('Brennaria (Erwinia) nigrifluens','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.99,0.99,0.01,x,0.01,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.99,0.99,0.01,0.01,0.99,0.99,0.99,0.99,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,0.99,x,x,x,x,x,x,x,x,0.99),
        ('Brennaria (Erwinia) quercina','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.99,0.99,0.01,x,0.01,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.99,0.01,0.01,0.01,0.99,0.99,0.01,0.01,0.01,0.99,0.99,x,0.01,0.01,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.99),
        ('Brennaria (Erwinia) rubrifaciens','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.99,0.99,0.01,x,0.01,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.51,0.01,0.01,0.01,0.99,0.99,0.01,0.01,0.01,0.01,0.99,x,0.01,0.01,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.01),
        ('Brennaria (Erwinia) salicis','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.99,0.99,0.01,x,0.01,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.51,0.99,0.01,0.01,0.99,0.99,0.99,0.99,0.01,0.99,0.99,x,0.01,0.01,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.99),
        ('Erwinia amylovora','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.99,0.01,0.01,0.99,0.01,x,x,x,0.99,0.01,x,0.51,x,0.01,x,x,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.51,x,0.99,0.01,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.99),
        ('Erwinia ananas','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.99,0.51,0.99,0.99,0.01,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.51,0.99,0.99,x,0.99,0.99,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.99),
        ('Erwinia mallotivora ','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.99,0.01,0.01,x,0.01,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.01,0.01,0.01,0.01,0.99,0.99,0.01,0.01,0.99,0.01,0.01,x,0.99,0.99,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.99),
        ('Erwinia psidii ','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.99,0.99,0.01,x,0.01,x,x,x,0.99,0.01,x,x,x,0.99,x,x,x,x,0.99,0.01,x,0.99,0.99,x,0.01,0.99,0.99,0.99,x,0.01,0.01,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.99),
        ('Erwinia tracheiphila','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.99,0.99,0.01,x,0.01,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,x,0.01,0.01,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.5),
        ('Pantoea dispersa','Colony: --- \n Type Strain: ---',apsw,0.99,0.01,0.99,0.01,0.01,0.99,0.5,x,x,x,0.99,0.01,x,0.5,x,0.01,x,x,x,0.85,0.5,0.01,0.99,0.99,0.99,0.01,0.01,0.99,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.99),
        ('Pantoea (Erwinia) stewartii','Colony: --- \n Type Strain: ---',apsw,0.99,0.01,0.01,0.01,0.01,x,0.01,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.01,0.01,0.99,0.01,0.99,0.99,0.99,0.99,0.01,0.01,0.99,x,0.99,0.99,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.01),
        ('Photorhabdus (Xenorhabdus) luminescens','Colony: --- \n Type Strain: ---',aw,0.99,0.01,0.99,0.01,0.5,0.5,0.01,x,x,x,0.85,0.01,x,0.01,x,0.01,x,x,x,0.01,0.01,0.01,0.15,0.01,x,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.5,x,x,x,x,x,0.15,x,x,x,x,x,x,x,x,x),
        ('Vibrio metschnokovii','Colony: --- \n Type Strain: ---',amw,0.99,0.01,0.51,0.01,0.15,0.51,0.01,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.99,0.51,0.51,0.99,0.99,0.99,0.01,0.01,0.01,0.01,0.51,0.99,0.99,0.01,0.51,0.51,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.51,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.5,0.99)]

        # negfacbac cat+ oxi- endo- nit1+ glu+ (nonfastidious)
        self.C = [
        ('Budvicia aquatica','Colony: --- \n Type Strain: ---',w,0.99,0.01,0.51,0.85,0.01,0.01,0.99,x,x,x,0.99,0.01,x,0.85,x,0.01,x,x,x,0.01,0.01,0.85,0.01,0.51,0.01,0.01,0.01,0.99,0.01,0.01,0.01,0.01,0.99,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.51,x,x,x,x,x,x,x,0.99,0.01),
        ('Buttiauxella agrestis','Colony: --- \n Type Strain: ---',w,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.51,0.01,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.01,0.99,0.99,0.01,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Cedecea davisae','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.99,0.01,0.01,0.01,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.67,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.01,0.99,0.01,0.99,0.99,0.99,0.99,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Cedecea lapagei','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.01,x,0.01,x,x,x,0.33,0.01,0.67,0.99,0.99,0.99,0.01,0.01,0.01,0.99,0.01,0.01,0.99,0.01,0.99,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.99),
        ('Cedecea neteri','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.01,x,0.01,x,x,x,0.99,0.01,0.99,0.99,0.99,0.99,0.01,0.01,0.01,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.67),
        ('Cedecea species 3','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.33,x,0.01,x,0.01,x,x,x,0.67,0.01,0.67,0.99,0.99,x,x,0.33,0.01,0.99,0.01,0.5,0.99,0.99,0.99,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Cedecea species 5','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.99,0.01,0.01,0.01,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.01,0.01,0.01,0.99,0.99,x,x,0.99,0.01,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Citrobacter (diversus) koseri','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.01,0.99,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.51,x,x,x,0.99,0.01,0.51,0.99,0.99,0.99,0.01,0.01,0.99,0.01,0.99,0.51,0.99,0.99,0.99,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.51,x,x,x,x,x,x,x,0.99,0.01),
        ('Citrobacter amalonaticus','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.85,0.15,0.99,0.99,0.99,x,x,x,0.99,0.85,x,0.99,x,0.01,x,x,x,0.51,0.01,0.51,0.99,0.99,0.99,0.01,0.01,0.99,0.15,0.99,0.01,0.99,0.99,0.85,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.85,x,x,x,x,x,x,x,0.99,0.01),
        ('Citrobacter braakii','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.85,0.51,0.15,0.85,0.99,x,x,x,0.99,0.91,x,0.99,x,0.51,x,x,x,0.99,0.01,0.85,0.99,0.99,x,x,0.15,0.99,0.01,0.99,0.15,0.99,0.99,0.51,0.01,0.9,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.51,x,x,x,x,x,x,x,0.8,0.01),
        ('Citrobacter farmeri','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.01,0.99,0.01,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.85,0.01,0.01,0.99,0.99,x,x,0.99,0.99,0.01,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.51,x,x,x,x,x,x,x,0.99,0.01),
        ('Citrobacter freundii','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.85,0.85,0.15,0.85,0.99,x,x,x,0.99,0.91,x,0.99,x,0.15,x,x,x,0.99,0.01,0.85,0.99,0.99,0.99,0.5,0.85,0.99,0.01,0.99,0.5,0.99,0.99,0.51,0.01,0.15,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.51,x,x,x,x,x,x,x,0.99,0.01),
        ('Citrobacter gillenii','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.85,0.85,0.01,0.51,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.51,0.01,0.51,0.99,0.99,x,x,0.15,0.99,0.15,0.99,0.15,0.99,0.99,0.15,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Citrobacter murliniae','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.51,0.99,0.85,0.99,x,x,x,0.99,0.99,x,0.99,x,0.99,x,x,x,0.99,0.01,0.51,0.99,0.99,x,x,0.15,0.99,0.15,0.99,0.15,0.99,0.99,0.51,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.51,x,x,x,x,x,x,x,0.99,0.01),
        ('Citrobacter rodentium','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.01,0.01,0.01,0.01,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.01,0.01,0.99,0.99,0.99,x,x,0.01,0.99,0.01,0.99,0.01,0.99,0.99,0.01,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.85,x,x,x,x,x,x,x,0.99,0.01),
        ('Citrobacter sedlakii','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.01,0.99,0.85,0.99,x,x,x,0.99,0.99,x,0.99,x,0.99,x,x,x,0.85,0.01,0.99,0.99,0.99,x,x,0.01,0.99,0.15,0.99,0.01,0.99,0.99,0.99,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.15,0.01,x,x,x,x,x,0.99,x,x,x,x,x,x,x,0.99,0.01),
        ('Citrobacter werkmanii','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.99,0.01,0.99,0.99,x,x,x,0.99,0.95,x,0.99,x,0.01,x,x,x,0.99,0.01,0.15,0.99,0.99,x,x,0.01,0.99,0.01,0.99,0.01,0.99,0.99,0.85,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.99,x,x,x,x,x,x,x,0.99,0.01),
        ('Citrobacter youngae','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.85,0.01,0.85,0.99,x,x,x,0.99,0.82,x,0.99,x,0.85,x,x,x,0.99,0.01,0.15,0.99,0.99,x,x,0.01,0.99,0.01,0.99,0.15,0.99,0.99,0.51,0.01,0.03,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.51,x,x,x,x,x,x,x,0.99,0.01),
        ('Edwardsiella hoshinae','Colony: --- \n Type Strain: ---',afw,0.99,0.01,0.99,0.01,0.15,0.01,0.99,x,x,x,0.99,0.99,x,0.15,x,0.01,x,x,x,0.51,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.01,0.51,0.01,0.99,0.99,0.01,0.01,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Edwardsiella ictaluri','Colony: --- \n Type Strain: ---',afw,0.99,0.01,0.01,0.01,0.01,0.01,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.01,0.01,0.01,0.99,0.01,0.99,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.99,0.51,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Edwardsiella tarda','Colony: --- \n Type Strain: ---',afw,0.99,0.01,0.99,0.99,0.99,0.01,0.99,x,x,x,0.99,0.99,x,0.01,x,0.01,x,x,x,0.51,0.01,0.01,0.99,0.01,0.99,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Enterobacter (Erwinia) dissolvens','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.01,0.51,0.51,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.99,x,x,x,x,x,x,x,0.99,0.99),
        ('Enterobacter (Erwinia) nimipressuralis','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.99,0.01,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.99,0.99,0.01,0.99,0.99,0.99,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.99),
        ('Enterobacter aerogenes','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.77),
        ('Enterobacter amnigenus biogroup 1','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.01,0.01,0.51,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.01,0.01,0.51,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.99,0.99,0.01,0.01,0.51,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.99),
        ('Enterobacter amnigenus biogroup 2','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.01,0.01,0.51,0.99,0.99,0.99,0.99,0.01,0.99,0.99,0.99,0.01,0.99,0.99,0.51,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.99),
        ('Enterobacter asburiae','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.01,0.01,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.15,0.01,0.85,0.99,0.99,0.99,0.01,0.51,0.01,0.99,0.99,0.99,0.99,0.99,0.15,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.51,x,x,x,x,x,x,x,0.99,0.01),
        ('Enterobacter cancerogenus','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.01,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.99,0.99,0.01,0.01,0.99,0.99,0.99,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.99),
        ('Enterobacter cloacae','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.94,x,0.99,x,0.15,x,x,x,0.51,0.15,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.85,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.51,0.01,x,x,x,x,x,0.51,x,x,x,x,x,x,x,0.99,0.85),
        ('Enterobacter gergoviae','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.99,0.01,0.51,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.99,0.99,0.01,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.99,x,x,x,x,x,x,x,0.99,0.25),
        ('Enterobacter hormaechei','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.51,0.01,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.85,x,x,x,0.01,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.99,0.51,0.01,0.99,0.99,0.99,0.85,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.85,x,x,x,x,x,x,x,0.99,x),
        ('Enterobacter intermedius','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.01,0.01,0.51,0.99,x,x,x,0.99,0.99,x,0.99,x,0.99,x,x,x,0.99,0.01,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.51,0.99,0.99,0.01,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.55),
        ('Enterobacter sakazakii','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.01,0.15,0.99,0.99,x,x,x,0.99,0.95,x,0.99,x,0.01,x,x,x,0.15,0.85,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.01,0.99,0.99,0.99,0.01,0.99,0.51,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.3),
        ('Enterobacter taylorae','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.01,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.99,0.99,0.01,0.01,0.99,0.99,0.99,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.2),
        ('Erwinia billingiae','Colony: --- \n Type Strain: ---',psw,0.99,0.01,x,0.01,0.01,0.01,0.99,x,x,x,0.99,0.01,x,x,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x),
        ('Erwinia persicinus','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.99),
        ('Erwinia rhapontici','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.99,0.99,0.01,x,0.99,x,x,x,0.99,0.01,x,0.99,x,0.51,x,x,x,0.99,0.99,0.99,0.99,0.99,x,x,0.99,0.99,0.99,0.99,x,0.99,0.51,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.99),
        ('Erwinia uredovora','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.99,0.01,0.99,x,0.99,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.51,0.99,x,0.99,0.99,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.99),
        ('Escherichia blattae','Colony: --- \n Type Strain: ---',fw,0.99,0.01,0.01,0.01,0.01,0.51,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.99,0.01,0.01,0.99,0.01,0.99,0.01,0.01,0.99,0.01,0.01,0.01,0.85,0.99,0.01,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Escherichia coli','Colony: --- \n Type Strain: ---',fw,0.99,0.01,0.99,0.01,0.99,0.01,0.99,x,x,x,0.99,0.99,x,0.99,x,0.51,x,x,x,0.51,0.01,0.99,0.99,0.99,0.99,0.85,0.51,0.85,0.51,0.99,0.51,0.99,0.99,0.15,0.99,0.51,0.01,x,x,x,x,x,x,x,x,x,x,x,0.51,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.81,0.01),
        ('Escherichia coli (inactive)','Colony: --- \n Type Strain: ---',fw,0.99,0.01,0.01,0.01,0.85,0.01,0.99,x,x,x,0.99,0.01,x,0.85,x,0.51,x,x,x,0.51,0.01,0.15,0.85,0.99,0.99,0.5,0.15,0.51,0.01,0.85,0.15,0.99,0.51,0.01,0.51,0.15,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.45,0.01),
        ('Escherichia fergusonii','Colony: --- \n Type Strain: ---',fw,0.99,0.01,0.99,0.01,0.99,0.15,0.99,x,x,x,0.99,0.99,x,0.99,x,0.51,x,x,x,0.15,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.99,0.51,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.51,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Escherichia hermanii','Colony: --- \n Type Strain: ---',fw,0.99,0.01,0.99,0.01,0.99,0.01,0.99,x,x,x,0.99,0.99,x,0.99,x,0.15,x,x,x,0.01,0.01,0.51,0.99,0.99,0.99,0.01,0.51,0.99,0.51,0.01,0.51,0.99,0.99,0.01,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.51,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Escherichia vulneris','Colony: --- \n Type Strain: ---',fw,0.99,0.01,0.99,0.01,0.01,0.01,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.15,0.01,0.15,0.99,0.99,0.99,0.99,0.99,0.99,0.51,0.01,0.01,0.99,0.99,0.51,0.85,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.15,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Ewingella americana','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.9,0.01,0.01,0.9,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.15,0.01,0.7,0.01,0.99,0.99,0.01,0.01,0.1,0.9,0.01,0.01,0.99,0.1,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.99),
        ('Hafnia alvei','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.85,0.01,0.01,0.01,0.99,x,x,x,0.99,0.94,x,0.99,x,0.01,x,x,x,0.99,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.99,0.15,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.91,0.88),
        ('Klebsiella (Calymmatobacterium) granulomatis','Colony: --- \n Type Strain: ---',af,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Klebsiella oxytoca','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.01,0.01,0.99,0.99,0.99,x,x,x,0.99,0.94,x,0.99,x,0.51,x,x,x,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.99,x,x,x,x,x,x,x,0.99,0.99),
        ('Klebsiella pneumoniae aerogenes','Colony: --- \n Type Strain: ---',af,0.99,0.01,x,x,x,x,x,x,x,x,0.99,0.9,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,0.57),
        ('Klebsiella pneumoniae ozaenae','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.01,0.01,0.01,0.51,0.85,x,x,x,0.99,0.61,x,0.99,x,0.01,x,x,x,0.51,0.51,0.51,0.99,0.99,0.99,0.99,0.99,0.51,0.99,0.51,0.15,0.99,0.99,0.01,0.51,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.85,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.98,0.01),
        ('Klebsiella pneumoniae pneumoniae','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.01,0.01,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.51,x,x,x,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.99,x,x,x,x,x,x,x,0.99,0.01),
        ('Klebsiella pneumoniae rhinoscleromatis','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.01,0.01,0.01,0.01,0.99,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.51,0.99,0.01,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.85,0.99,0.99,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.51,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Kluyvera ascorbata','Colony: --- \n Type Strain: ---',afs,0.99,0.01,0.99,0.01,0.99,0.99,0.99,x,x,x,0.99,0.91,x,0.99,x,0.15,x,x,x,0.51,0.01,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.51,0.99,0.99,0.99,0.01,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Kluyvera cryocrescens','Colony: --- \n Type Strain: ---',afs,0.99,0.01,0.99,0.01,0.99,0.85,0.99,x,x,x,0.99,0.91,x,0.99,x,0.01,x,x,x,0.01,0.01,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.51,0.85,0.99,0.99,0.01,0.15,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Leclercia (Escherichia) adecarboxylata','Colony: --- \n Type Strain: ---',aw,0.99,0.01,0.85,0.01,0.99,0.01,0.99,x,x,x,0.99,0.99,x,0.99,x,0.85,x,x,x,0.01,0.01,0.99,0.99,0.99,0.99,0.99,0.51,0.99,0.99,0.01,0.51,0.99,0.99,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.15,x,x,x,x,x,x,x,0.99,0.01),
        ('Leminorella grimontii','Colony: --- \n Type Strain: ---',f,0.99,0.01,0.01,0.99,0.01,0.99,0.99,x,x,x,0.99,0.5,x,0.99,x,0.85,x,x,x,0.15,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.85,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Leminorella richardii','Colony: --- \n Type Strain: ---',f,0.99,0.01,0.01,0.99,0.01,0.01,0.99,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Moellerella wisconsensis','Colony: --- \n Type Strain: ---',fw,0.99,0.01,0.01,0.01,0.01,0.85,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.01,0.01,0.99,0.51,0.51,0.99,0.99,0.99,0.01,0.01,0.01,0.99,0.01,0.01,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Morganella morganii','Colony: --- \n Type Strain: ---',fw,0.99,0.01,0.99,0.01,0.99,0.01,0.99,x,x,x,0.99,0.99,x,0.01,x,0.01,x,x,x,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.5,0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.99,x,x,x,x,x,x,x,0.01,0.01),
        ('Pantoea (Enterobacter) agglomerans','Colony: --- \n Type Strain: ---',apsw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.01,0.01,0.15,0.99,0.99,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.99,0.01,0.01,0.01,0.15,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.99),
        ('Pantoea dispersa','Colony: --- \n Type Strain: ---',apsw,0.99,0.01,0.99,0.01,0.01,0.99,0.5,x,x,x,0.99,0.01,x,0.5,x,0.01,x,x,x,0.85,0.5,0.01,0.99,0.99,0.99,0.01,0.01,0.99,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.99),
        ('Pectobacterium (Erwinia) cacticida','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.99,x,0.01,0.99,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.85,0.01,0.15,0.01,0.99,0.99,0.01,0.01,0.99,0.99,0.01,0.99,0.85,0.51,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.99),
        ('Pectobacterium (Erwinia) carotovora','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.99,0.99,0.01,0.99,0.99,x,x,x,0.99,x,x,0.99,x,0.01,x,x,x,0.51,0.51,0.99,0.51,0.99,0.99,0.99,0.99,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.99),
        ('Pectobacterium (Erwinia) chrysanthemi','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.99,0.99,0.99,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.99,0.51,0.51,0.01,0.99,0.99,0.99,0.99,0.99,0.99,0.99,x,0.01,0.99,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.99),
        ('Pectobacterium (Erwinia) cypripedii','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.99,0.99,0.01,x,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.51,0.99,0.01,0.99,0.99,0.99,0.99,0.01,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.99,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.01),
        ('Pectobacterium atrosepticum','Colony: --- \n Type Strain: ---',psw,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Pectobacterium betavasculorum','Colony: --- \n Type Strain: ---',psw,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Pectobacterium wasabiae','Colony: --- \n Type Strain: ---',psw,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Pragia fontium','Colony: --- \n Type Strain: ---',fw,0.99,0.01,0.99,0.99,0.01,0.85,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.85,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.15,x,x,x,x,x,x,x,x,x,x,x,0.85,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Proteus mirabilis','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.99,0.01,0.51,0.99,x,x,x,0.99,0.99,x,0.01,x,0.01,x,x,x,0.7,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.15,0.99,0.99,0.01,0.01,0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,0.01,0.9,x,x,x,x,x,0.99,x,x,x,x,x,x,x,0.01,0.23),
        ('Proteus myxofaciens','Colony: --- \n Type Strain: ---',a,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.01,x,0.01,x,x,x,0.99,0.01,0.01,0.99,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.99,0.99,0.01,0.01,0.01,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,0.01,0.99,x,x,x,x,x,0.99,x,x,x,x,x,x,x,0.01,0.99),
        ('Proteus penneri','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.85,0.3,0.01,0.01,0.99,x,x,x,0.99,0.45,x,0.01,x,0.01,x,x,x,0.51,0.01,0.01,0.99,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.99,0.62,0.99,0.01,0.01,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,0.01,0.51,x,x,x,x,x,0.99,x,x,x,x,x,x,x,0.01,0.01),
        ('Proteus vulgaris Biogroup 2','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.57,0.99,0.29,0.99,x,x,x,0.99,0.86,x,0.01,x,0.01,x,x,x,0.4,0.01,0.01,0.99,0.01,x,x,0.01,0.01,0.51,0.01,0.99,0.01,0.99,0.01,0.01,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,0.99,0.57,x,x,x,x,x,0.86,x,x,x,x,x,x,x,x,x),
        ('Proteus vulgaris Biogroup 3','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.99,0.85,0.99,0.01,0.99,x,x,x,0.99,0.81,x,0.01,x,0.01,x,x,x,0.29,0.01,0.01,0.99,0.01,x,x,0.01,0.17,0.99,0.01,0.99,0.14,0.99,0.01,0.01,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,0.01,0.99,x,x,x,x,x,0.99,x,x,x,x,x,x,x,x,x),
        ('Providencia alcalifaciens','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.96,0.01,0.99,0.99,0.99,x,x,x,0.99,0.85,x,0.01,x,0.01,x,x,x,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.01,0.01,0.01,0.01,0.15,0.01,0.01,0.01,0.01,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Providencia heimbachae','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.46,0.01,0.01,0.01,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.01,0.46,0.01,0.54,0.01,0.99,0.01,0.01,0.99,0.01,0.01,0.01,0.01,0.08,0.01,0.01,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Providencia rettgeri','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.94,0.01,0.99,0.95,0.99,x,x,x,0.99,0.1,x,0.01,x,0.01,x,x,x,0.6,0.9,0.01,0.01,0.99,0.99,0.01,0.01,0.7,0.5,0.01,0.15,0.01,0.1,0.01,0.01,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,0.35,0.01,x,x,x,x,x,0.99,x,x,x,x,x,x,x,0.03,0.01),
        ('Providencia rustigianii','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.3,0.01,0.98,0.15,0.99,x,x,x,0.99,0.35,x,0.01,x,0.01,x,x,x,0.05,0.01,0.01,0.01,0.01,0.99,0.01,0.01,0.01,0.01,0.01,0.35,0.01,0.01,0.01,0.01,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Providencia stuartii','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.85,0.01,0.98,0.93,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.5,0.95,0.01,0.01,0.1,0.99,0.01,0.01,0.01,0.01,0.01,0.5,0.98,0.07,0.01,0.01,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.3,x,x,x,x,x,x,x,0.05,0.01),
        ('Rahnella aquatilis','Colony: --- \n Type Strain: ---',aw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.99,x,x,x,0.15,0.01,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.01,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Raoultella (Klebsiella) ornithinolytica','Colony: --- \n Type Strain: ---',psw,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01),
        ('Raoultella (Klebsiella) planticola','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.01,0.01,0.15,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.15,x,x,x,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.99,x,x,x,x,x,x,x,0.99,0.91),
        ('Raoultella (Klebsiella) terrigena','Colony: --- \n Type Strain: ---',psw,0.99,0.01,0.01,0.01,0.01,0.51,0.99,x,x,x,0.99,0.86,x,0.99,x,0.15,x,x,x,0.99,0.85,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.15,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.14),
        ('Salmonella bongori','Colony: --- \n Type Strain: ---',afw,0.99,0.01,0.99,0.99,0.01,0.99,0.99,x,x,x,0.99,0.85,x,0.99,x,0.99,x,x,x,0.01,0.01,0.01,0.99,0.99,0.99,0.85,0.01,0.99,0.01,0.99,0.01,0.99,0.99,0.51,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Salmonella enterica arizonae','Colony: --- \n Type Strain: ---',afw,0.99,0.01,0.99,0.99,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.01,0.01,0.15,0.99,0.99,0.99,0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.99,0.51,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Salmonella enterica diarizonae','Colony: --- \n Type Strain: ---',afw,0.99,0.01,0.99,0.99,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.01,0.01,0.85,0.99,0.99,0.99,0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.99,0.51,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Salmonella enterica enterica','Colony: --- \n Type Strain: ---',afw,0.99,0.01,0.99,0.99,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.99,x,x,x,0.01,0.51,0.01,0.99,0.99,0.99,0.99,0.01,0.99,0.01,0.99,0.01,0.99,0.99,0.51,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Salmonella enterica houtenae','Colony: --- \n Type Strain: ---',afw,0.99,0.01,0.99,0.99,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.01,0.01,0.01,0.99,0.99,0.99,0.99,0.01,0.99,0.51,0.99,0.01,0.99,0.99,0.51,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Salmonella enterica indica','Colony: --- \n Type Strain: ---',afw,0.99,0.01,0.99,0.99,0.01,0.85,0.99,x,x,x,0.99,0.99,x,0.99,x,0.51,x,x,x,0.51,0.01,0.15,0.99,0.99,0.99,0.85,0.01,0.99,0.01,0.01,0.01,0.99,0.99,0.51,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.5,0.01),
        ('Salmonella enterica salamae','Colony: --- \n Type Strain: ---',afw,0.99,0.01,0.99,0.99,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.99,x,x,x,0.15,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.99,0.01,0.99,0.01,0.99,0.99,0.99,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.15,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.15,0.01),
        ('Serratia entomophila','Colony: --- \n Type Strain: ---',afpsw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.01,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.01,0.99,0.01,0.99,0.99,0.51,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.99),
        ('Serratia ficaria','Colony: --- \n Type Strain: ---',afpsw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.01,0.51,0.15,0.99,0.99,0.99,0.5,0.51,0.51,0.99,0.99,0.99,0.99,0.99,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.2),
        ('Serratia fonticola','Colony: --- \n Type Strain: ---',afpsw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.85,x,0.99,x,0.99,x,x,x,0.85,0.51,0.99,0.99,0.99,0.99,0.99,0.99,0.85,0.99,0.99,0.15,0.99,0.85,0.01,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.15,x,x,x,x,x,x,x,0.99,0.01),
        ('Serratia grimesli','Colony: --- \n Type Strain: ---',afpsw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.51,0.51,0.01,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.5),
        ('Serratia liquefaciens','Colony: --- \n Type Strain: ---',afpsw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.85,x,0.99,x,0.01,x,x,x,0.99,0.51,0.01,0.99,0.99,0.99,0.85,0.85,0.15,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.97,0.74),
        ('Serratia marcescens','Colony: --- \n Type Strain: ---',afpsw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.5,x,0.01,x,0.01,x,x,x,0.99,0.85,0.01,0.99,0.99,0.99,0.01,0.01,0.01,0.99,0.99,0.99,0.99,0.01,0.01,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.99,x,x,x,x,x,0.15,x,x,x,x,x,x,x,0.96,0.96),
        ('Serratia odorifera group 1','Colony: --- \n Type Strain: ---',afpsw,0.99,0.01,0.99,0.01,0.51,0.99,0.99,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.51,0.99,0.51,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Serratia odorifera group 2','Colony: --- \n Type Strain: ---',afpsw,0.99,0.01,0.99,0.01,0.51,0.99,0.99,x,x,x,0.99,0.15,x,0.99,x,0.01,x,x,x,0.51,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.51,0.99,0.01,0.99,0.99,0.01,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.51,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Serratia plymuthica','Colony: --- \n Type Strain: ---',afpsw,0.99,0.01,0.51,0.01,0.01,0.51,0.99,x,x,x,0.99,0.5,x,0.99,x,0.01,x,x,x,0.51,0.51,0.85,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.51,0.99,0.99,0.99,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.85,0.51,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.99),
        ('Serratia proteamaculans','Colony: --- \n Type Strain: ---',afpsw,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.51,0.51,0.01,0.99,0.99,0.99,0.99,0.99,0.51,0.51,0.85,0.99,0.99,0.99,0.01,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.51,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x),
        ('Serratia rubidaea','Colony: --- \n Type Strain: ---',afpsw,0.99,0.01,0.85,0.01,0.01,0.99,0.99,x,x,x,0.99,0.5,x,0.99,x,0.01,x,x,x,0.15,0.15,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.99,0.01,0.99,0.99,0.99,0.01,0.51,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.77),
        ('Shigella boydii','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.01,0.01,0.51,0.01,0.99,x,x,x,0.99,0.01,x,0.51,x,0.01,x,x,x,0.01,0.01,0.01,0.51,0.99,0.99,0.5,0.51,0.01,0.01,0.51,0.01,0.85,0.01,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.13,0.01),
        ('Shigella dysenteriae','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.01,0.01,0.51,0.01,0.99,x,x,x,0.99,0.01,x,0.51,x,0.01,x,x,x,0.01,0.01,0.01,0.51,0.99,0.99,0.5,0.51,0.01,0.01,0.51,0.01,0.85,0.01,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.13,0.01),
        ('Shigella flexneri','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.01,0.01,0.51,0.01,0.99,x,x,x,0.99,0.01,x,0.51,x,0.01,x,x,x,0.01,0.01,0.01,0.51,0.99,0.99,0.5,0.51,0.01,0.01,0.51,0.01,0.85,0.01,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.13,0.01),
        ('Shigella sonnei','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.01,0.01,0.01,0.01,0.99,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.15,0.01,0.01,0.99,0.99,0.99,0.15,0.01,0.85,0.01,0.01,0.01,0.99,0.01,0.01,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.89,0.01),
        ('Tatumella ptyseos','Colony: --- \n Type Strain: ---',a,0.99,0.01,0.01,0.01,0.01,0.01,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.01,0.01,0.01,0.01,0.01,0.99,0.5,0.15,0.01,0.5,0.01,0.99,0.99,0.01,0.01,0.01,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Trabulsiella guamensis','Colony: --- \n Type Strain: ---',afw,0.99,0.01,0.99,0.99,0.01,0.99,0.99,x,x,x,0.99,x,x,0.99,x,0.01,x,x,x,0.01,0.01,0.01,0.99,0.99,x,x,0.01,0.99,0.01,0.99,0.01,0.99,0.99,0.5,0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Yersinia aldovae','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.01,0.01,0.01,0.01,0.99,x,x,x,0.99,0.01,x,0.51,x,0.01,x,x,x,0.01,0.01,0.01,0.01,0.85,0.99,0.01,0.01,0.01,0.01,0.51,0.15,0.85,0.51,0.01,0.01,0.51,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.85,x,x,x,x,x,x,x,0.01,0.01),
        ('Yersinia bercovieri','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.01,0.01,0.01,0.01,0.99,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.01,0.01,0.15,0.99,0.99,0.99,0.01,0.01,0.01,0.15,0.99,0.99,0.99,0.99,0.01,0.01,0.85,0.01,x,x,x,x,x,x,x,x,x,x,x,0.15,0.01,x,x,x,x,x,0.51,x,x,x,x,x,x,x,0.8,0.01),
        ('Yersinia enterocolitica','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.01,0.01,0.51,0.01,0.99,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.99,0.51,0.01,0.85,0.99,0.99,0.01,0.01,0.01,0.15,0.99,0.99,0.99,0.51,0.01,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.15,0.01,x,x,x,x,x,0.85,x,x,x,x,x,x,x,0.99,0.01),
        ('Yersinia frederiksenii' ,'Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.01,0.01,0.99,0.15,0.99,x,x,x,0.99,0.5,x,0.99,x,0.01,x,x,x,0.85,0.15,0.51,0.99,0.99,0.99,0.01,0.51,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.85,0.01,x,x,x,x,x,0.85,x,x,x,x,x,x,x,0.99,0.01),
        ('Yersinia intermedia','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.01,0.01,0.99,0.01,0.99,x,x,x,0.99,0.15,x,0.99,x,0.01,x,x,x,0.51,0.15,0.51,0.99,0.99,0.99,0.85,0.51,0.99,0.99,0.99,0.99,0.99,0.99,0.01,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.85,x,x,x,x,x,x,x,0.99,0.01),
        ('Yersinia kristensenii','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.01,0.01,0.51,0.01,0.99,x,x,x,0.99,0.15,x,0.85,x,0.01,x,x,x,0.51,0.15,0.01,0.99,0.99,0.99,0.01,0.01,0.01,0.15,0.99,0.01,0.99,0.85,0.01,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.85,x,x,x,x,x,x,x,0.99,0.01),
        ('Yersinia mollaretii','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.01,0.01,0.01,0.01,0.99,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.15,0.01,0.51,0.51,0.99,0.99,0.01,0.01,0.01,0.15,0.99,0.99,0.99,0.51,0.01,0.01,0.85,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.15,x,x,x,x,x,x,x,0.2,0.01),
        ('Yersinia pestis','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.01,0.01,0.01,0.01,0.85,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.51,0.01,0.01,0.85,0.99,0.99,0.15,0.01,0.01,0.51,0.51,0.01,0.99,0.99,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.51,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Yersinia pseudotuberculosis','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.01,0.01,0.01,0.01,0.99,x,x,x,0.99,0.01,x,0.51,x,0.01,x,x,x,0.51,0.01,0.01,0.99,0.99,0.99,0.5,0.15,0.51,0.15,0.01,0.01,0.99,0.99,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.99,x,x,x,x,x,x,x,0.99,0.01),
        ('Yersinia rohdei','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.01,0.01,0.01,0.01,0.85,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.51,0.01,0.01,0.01,0.99,0.99,0.5,0.51,0.01,0.01,0.99,0.99,0.99,0.51,0.01,0.01,0.15,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.51,x,x,x,x,x,x,x,0.5,0.01),
        ('Yersinia ruckeri','Colony: --- \n Type Strain: ---',afsw,0.99,0.01,0.01,0.01,0.01,0.01,0.85,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.51,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.01,0.01,0.51,0.01,0.99,0.01,0.01,0.51,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.51,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Yokenella regensburgei','Colony: --- \n Type Strain: ---',af,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.01,0.01,0.01,0.99,0.99,0.99,0.99,0.15,0.99,0.01,0.01,0.01,0.99,0.99,0.01,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.5,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01)]

        # negfacbac cat+ oxi+ endo- nit1+ glu+ (nonfastidious)
        self.D = [
        ('Aeromonas allosaccharophila','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.99,0.01,0.99,0.51,0.99,x,x,x,0.99,0.99,x,0.51,x,0.01,x,x,x,0.99,0.01,0.01,0.99,0.99,0.99,0.33,0.51,0.51,0.01,0.01,0.99,0.99,0.01,0.51,0.99,0.51,0.99,x,x,x,x,x,x,x,x,x,x,x,0.51,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Aeromonas bestiarum','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.99,0.99,0.99,0.51,0.99,x,x,x,0.99,0.75,x,0.99,x,0.01,x,x,x,0.99,0.01,0.18,0.99,0.99,0.99,0.01,0.01,0.83,0.99,0.18,0.99,0.99,0.01,0.83,0.83,0.01,0.25,x,x,x,x,x,x,x,x,x,x,x,0.99,0.75,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.63),
        ('Aeromonas caviae','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.99,0.01,0.99,0.83,0.99,x,x,x,0.99,0.05,x,0.99,x,0.01,x,x,x,0.51,0.01,0.51,0.99,0.99,0.99,0.04,0.01,0.01,0.99,0.01,0.99,0.99,0.01,0.99,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Aeromonas encheleia','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.99,0.01,0.99,0.01,0.99,x,x,x,0.99,0.95,x,0.01,x,0.01,x,x,x,0.83,0.01,0.01,0.99,0.83,0.99,0.01,0.01,0.83,0.99,0.01,0.83,0.99,0.01,0.99,0.01,0.01,0.51,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Aeromonas eucrenophila','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.99,0.01,0.99,0.01,0.99,x,x,x,0.99,0.89,x,0.83,x,0.01,x,x,x,0.01,0.01,0.99,0.99,0.99,0.99,0.01,0.01,0.01,0.99,0.01,0.83,0.99,0.01,0.99,0.01,0.01,0.51,x,x,x,x,x,x,x,x,x,x,x,0.99,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Aeromonas hydrophila','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.99,0.83,0.99,0.51,0.99,x,x,x,0.99,0.83,x,0.83,x,0.01,x,x,x,0.99,0.01,0.18,0.99,0.99,0.99,0.01,0.01,0.18,0.83,0.01,0.99,0.99,0.01,0.99,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.92),
        ('Aeromonas jandaei','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.99,0.83,0.99,0.83,0.99,x,x,x,0.99,0.99,x,0.18,x,0.01,x,x,x,0.99,0.01,0.01,0.99,0.99,0.99,0.47,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.99,0.99,0.01,0.93,x,x,x,x,x,x,x,x,x,x,x,0.01,0.93,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.87),
        ('Aeromonas media','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.51,0.01,0.51,0.51,0.99,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.99,0.01,0.99,0.99,0.99,0.99,0.01,0.01,0.01,0.99,0.18,0.99,0.99,0.01,0.99,0.01,0.01,0.51,x,x,x,x,x,x,x,x,x,x,x,0.51,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Aeromonas popoffii','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.99,0.51,0.51,0.51,0.99,x,x,x,0.99,0.99,x,0.51,x,0.01,x,x,x,0.99,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.99,0.01,0.01,0.86,x,x,x,x,x,x,x,x,x,x,x,0.01,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.57,0.86),
        ('Aeromonas salmonicida achromogenes','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.01,0.01,0.99,0.01,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.51,0.01,0.01,0.99,0.01,0.99,0.01,0.01,0.01,0.51,0.01,0.99,0.99,0.01,0.99,0.51,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.62),
        ('Aeromonas salmonicida masoucida','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.01,0.99,0.99,0.01,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.51,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.01,0.51,0.01,0.99,0.99,0.01,0.99,0.51,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.62),
        ('Aeromonas salmonicida salmonicida','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.01,0.01,0.01,0.01,0.99,x,x,x,0.99,0.99,x,0.99,x,0.01,x,x,x,0.51,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.01,0.51,0.01,0.01,0.99,0.01,0.99,0.51,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.62),
        ('Aeromonas salmonicida smithia','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.01,0.99,0.01,0.01,0.99,x,x,x,0.85,0.85,x,0.51,x,0.01,x,x,x,0.18,0.01,0.01,0.01,0.01,0.99,0.01,0.01,0.01,0.51,0.18,0.51,0.99,0.01,0.18,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Aeromonas schubertii','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.51,0.01,0.01,0.99,0.01,0.99,0.01,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.99,0.83,0.01,0.51,x,x,x,x,x,x,x,x,x,x,x,0.01,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.83,0.17),
        ('Aeromonas sobria','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.99,0.99,0.99,0.01,0.99,x,x,x,0.99,0.99,x,0.18,x,0.01,x,x,x,0.99,0.01,0.18,0.99,0.99,0.99,0.01,0.01,0.01,0.18,0.01,0.99,0.99,0.01,0.99,0.99,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,0.01,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Aeromonas trota','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.99,0.51,0.99,0.99,0.99,x,x,x,0.99,0.75,x,0.01,x,0.01,x,x,x,0.51,0.01,0.51,0.99,0.83,0.99,0.01,0.01,0.01,0.01,0.01,0.18,0.99,0.01,0.99,0.99,0.01,0.94,x,x,x,x,x,x,x,x,x,x,x,0.01,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Aeromonas veronii bv sobria','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.99,0.99,0.99,0.51,0.99,x,x,x,0.99,0.86,x,0.18,x,0.01,x,x,x,0.51,0.01,0.18,0.99,0.99,0.99,0.01,0.01,0.01,0.18,0.01,0.99,0.99,0.01,0.99,0.99,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,0.18,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.88),
        ('Aeromonas veronii bv veronii','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.99,0.51,0.99,0.99,0.99,x,x,x,0.99,0.8,x,0.01,x,0.01,x,x,x,0.99,0.01,0.18,0.99,0.99,0.99,0.01,0.01,0.01,0.99,0.01,0.99,0.99,0.01,0.01,0.99,0.99,0.83,x,x,x,x,x,x,x,x,x,x,x,0.99,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.88),
        ('Chromobacterium fluviatile','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.18,0.01,0.01,0.99,0.01,0.9,x,0.01,0.01,0.01,0.01,0.18,0.99,0.01,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.01),
        ('Chromobacterium violaceum','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.99,0.18,0.01,0.99,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.01,0.01,0.01,0.51,0.01,0.8,x,0.01,0.01,0.01,0.51,0.18,0.99,0.01,0.51,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.01),
        ('Plesiomonas shigelloides','Colony: --- \n Type Strain: ---',aw,0.99,0.99,0.99,0.01,0.99,0.01,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.51,0.99,0.99,0.99,0.01,0.15,0.01,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.99,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio cholerae','Colony: --- \n Type Strain: ---',amw,0.99,0.99,0.99,0.01,0.99,0.99,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.51,0.01,0.01,0.99,0.99,0.85,0.01,0.01,0.01,0.01,0.01,0.99,0.99,0.01,0.01,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.50),
        ('Vibrio fluvialis','Colony: --- \n Type Strain: ---',mw,0.99,0.99,0.51,0.01,0.18,0.99,0.99,x,x,x,0.99,0.01,x,0.99,x,0.01,x,x,x,0.01,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.01,0.01,0.01,0.99,0.99,0.01,0.99,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.83,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.5,0.01),
        ('Vibrio harveyi','Colony: --- \n Type Strain: ---',mw,0.99,0.99,0.01,0.01,0.99,0.01,0.99,x,x,x,0.51,0.01,x,0.01,x,0.01,x,x,x,0.01,0.01,0.01,0.99,0.51,0.5,0.01,0.01,0.01,0.01,0.01,0.51,0.51,0.01,0.01,0.99,0.01,0.51,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.50),
        ('Vibrio mimicus','Colony: --- \n Type Strain: ---',mw,0.99,0.99,0.99,0.01,0.99,0.99,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.18,0.01,0.18,0.99,0.99,0.99,0.01,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.01,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.51,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio parahaemolyticus','Colony: --- \n Type Strain: ---',amw,0.99,0.99,0.99,0.01,0.99,0.01,0.99,x,x,x,0.99,0.01,x,0.83,x,0.01,x,x,x,0.51,0.01,0.01,0.99,0.99,0.99,0.01,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.01,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.99,x,x,x,x,x,0.28,x,x,x,x,x,x,x,0.01,0.01),
        ('Vibrio vulnificus','Colony: --- \n Type Strain: ---',amw,0.99,0.99,0.99,0.01,0.99,0.51,0.99,x,x,x,0.99,0.01,x,0.01,x,0.01,x,x,x,0.01,0.01,0.83,0.99,0.51,0.99,0.5,0.01,0.01,0.99,0.01,0.18,0.99,0.01,0.01,0.99,0.51,0.51,x,x,x,x,x,x,x,x,x,x,x,0.01,0.51,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.5,0.01)]

        # negfacbac cat+ oxi+ endo- (salt)
        self.E = [
        ('Colwellia psychrerythraea','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,0.01,0.01,0.01,0.99,x,x,0.01,0.99,0.01,x,0.01,x,x,x,0.01,0.01,x,0.01,0.01,0.99,0.01,0.01,0.01,x,x,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,0.99,x,0.99,0.99,x,0.99,x,0.99,x,0.99,x,x,x,x,0.01,x,x,0.01,x),
        ('Colwellia demingiae','Colony: --- \n Type Strain: ACAM 459',m,0.99,0.99,0.99,0.01,0.01,0.99,0.99,x,x,x,0.01,0.01,x,0.01,0.01,x,x,0.01,0.01,x,0.01,0.01,0.01,0.01,0.01,0.01,x,x,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,x,0.01,x,x,x,x,x,x,x,x,0.99,x,0.99,0.01,x,0.99,x,0.01,0.01,0.01,x,x,x,x,0.01,x,x,0.01,x),
        ('Colwellia rossensis','Colony: --- \n Type Strain: ACAM 608',m,0.99,0.99,0.99,0.01,0.01,0.99,0.99,x,x,0.01,0.99,0.01,x,0.01,0.01,x,x,0.01,0.99,x,0.01,0.01,0.01,0.01,0.01,0.01,x,x,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,x,0.01,x,x,x,x,x,x,x,x,0.01,x,x,0.01,x,0.99,x,x,0.01,0.99,x,x,x,x,0.01,x,x,0.01,x),
        ('Colwellia hornerae','Colony: --- \n Type Strain: ACAM 607',m,0.99,0.99,0.99,0.01,0.01,0.99,0.99,x,x,x,0.01,0.01,x,0.01,0.01,x,x,0.01,0.01,x,0.01,0.01,0.01,0.01,0.01,0.01,x,x,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,x,0.01,x,x,x,x,x,x,x,x,0.99,x,0.99,0.01,x,0.99,x,0.99,0.01,0.01,x,x,x,x,0.01,x,x,0.01,x),
        ('Colwellia psychroptropica','Colony: --- \n Type Strain: ACAM 179',m,0.99,0.99,0.99,0.01,0.01,0.01,0.99,x,x,x,0.01,0.01,x,0.01,0.01,x,x,0.01,0.01,x,0.01,0.01,0.01,0.01,0.01,0.01,x,x,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,x,0.99,x,x,x,x,x,x,x,x,0.99,x,0.01,0.01,x,0.01,x,0.99,0.99,0.99,x,x,x,x,0.01,x,x,0.01,x),
        ('Listonella anguillarum','Colony: --- \n Type Strain: ---',m,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Listonella pelagia biovar I','Colony: --- \n Type Strain: ---',m,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Listonella pelagia biovar II','Colony: --- \n Type Strain: ---',m,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Photobacterium angustum','Colony: --- \n Type Strain: ATCC 25915',m,0.01,0.99,0.99,0.01,0.01,0.01,0.01,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,x,x,x,0.01,x,0.01,x,0.01,x,0.01,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Photobacterium damselae damselae','Colony: --- \n Type Strain: ATCC 33539',am,0.99,0.99,0.99,0.01,0.01,0.01,0.99,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,x,x,x,0.01,x,0.99,x,0.01,x,0.01,0.01,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Photobacterium damselae piscicida','Colony: --- \n Type Strain: NCIMB 2058',am,0.99,0.99,0.01,0.01,0.01,0.01,0.01,x,x,0.01,0.99,x,x,0.99,x,x,x,x,x,x,x,x,x,0.01,x,0.01,x,0.01,x,0.99,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Photobacterium frigidiphilum','Colony: --- \n Type Strain: SL13',m,0.99,0.99,0.99,x,0.99,0.01,0.99,x,x,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,x,0.99,x,x,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Photobacterium ganghwense','Colony: --- \n Type Strain: FR1311',m,0.99,0.99,0.99,0.01,0.99,0.99,0.99,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,x,x,x,0.99,x,0.01,x,0.99,x,0.01,0.01,x,x,0.99,0.01,0.01,x,0.01,x,x,x,x,x,x,x,x,x,x,0.01,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x),
        ('Photobacterium iliopiscarium','Colony: --- \n Type Strain: ATCC 51760',m,0.99,0.99,0.99,0.01,0.01,0.01,0.99,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,x,x,x,0.01,x,0.01,x,0.01,x,0.01,0.01,x,x,0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Photobacterium indicum','Colony: --- \n Type Strain: NBRC 14233',m,0.01,0.01,0.99,0.99,0.99,0.01,0.99,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Photobacterium leiognathi','Colony: --- \n Type Strain: ATCC 25521',am,0.01,0.99,0.99,0.01,0.01,0.01,0.99,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,x,x,x,0.01,x,0.01,x,0.01,x,0.01,0.01,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Photobacterium  lipolyticum','Colony: --- \n Type Strain: DSM 16190',m,0.99,0.99,0.99,0.01,0.99,0.01,0.99,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,x,x,x,0.01,x,0.01,x,0.01,x,0.01,0.99,x,x,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Photobacterium phosphoreum','Colony: --- \n Type Strain: ATCC 11040',am,0.99,0.99,0.99,0.01,0.01,0.01,0.99,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,x,x,x,0.01,x,0.01,x,0.01,x,0.01,0.01,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Photobacterium profundum','Colony: --- \n Type Strain: JCM 10084',m,0.99,0.99,0.99,0.01,0.99,0.01,0.99,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,x,x,x,0.99,x,0.01,x,0.01,x,0.01,0.01,x,x,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Photobacterium rosenbergii','Colony: --- \n Type Strain: LMG 22223',m,x,0.99,0.99,x,0.01,0.99,0.99,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,x,x,x,0.99,x,0.99,x,0.99,x,0.01,0.99,x,x,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Shewanella xiamenensis','Colony: --- \n Type Strain: S4T',m,0.99,0.99,x,x,x,0.01,0.99,x,x,x,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x),
        ('Shewanella oneidensis','Colony: --- \n Type Strain: ATCC 700550',m,0.99,0.99,x,x,x,0.01,0.99,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x),
        ('Shewanella putrefaciens','Colony: --- \n Type Strain: ATCC 8071',m,0.99,0.99,x,x,x,0.01,0.99,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x),
        ('Shewanella profunda','Colony: --- \n Type Strain: DSM 15900',m,0.99,0.99,x,x,x,0.99,0.99,x,x,x,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x),
        ('Shewanella decolorationis','Colony: --- \n Type Strain: JCM 21555',m,0.99,0.99,x,x,x,0.01,0.99,x,x,x,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x),
        ('Shewanella baltica','Colony: --- \n Type Strain: DSM 9439',m,0.99,0.99,x,x,x,0.99,0.99,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x),
        ('Shewanella hafniensis','Colony: --- \n Type Strain: NBRC 100975',m,0.99,0.99,x,x,x,0.99,0.99,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x),
        ('Shewanella morhuae','Colony: --- \n Type Strain: NBRC 100978',m,0.99,0.99,x,x,x,0.01,0.99,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x),
        ('Shewanella glacialipisicola','Colony: --- \n Type Strain: NBRC 102030',m,0.99,0.99,x,x,x,0.01,0.99,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x),
        ('Vibrio aerogenes','Colony: --- \n Type Strain: DSM 14438',m,0.99,0.01,0.99,x,0.99,0.99,x,x,x,0.01,0.99,0.99,x,0.01,x,x,x,x,x,x,0.99,x,x,0.99,0.99,0.01,x,x,x,0.01,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio aestuarinus','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,x,0.01,x,0.99,x,x,0.99,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio agarivorans','Colony: --- \n Type Strain: CECT 5085',m,0.99,0.99,0.99,x,0.01,0.01,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.01,0.99,x,0.01,0.01,0.01,0.01,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Vibrio alginolyticus','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.99,0.85,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,x,0.01,x,0.01,x,0.01,0.85,x,x,0.01,0.99,0.85,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.15,x,x,x,x,x,x,x,0.01,0.85),
        ('Vibrio anguillarum','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.85,0.99,x,x,x,0.01,0.99,0.01,x,0.85,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,0.01,0.01,0.85,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.99),
        ('Vibrio brasiliensis','Colony: --- \n Type Strain: DSM 17184',m,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,0.01,x,0.01,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.99),
        ('Vibrio calvienensis','Colony: --- \n Type Strain: DSM 14347',m,0.99,0.99,0.99,x,0.01,0.99,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,x,x,x,0.99,0.99,0.99,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio campbellii','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.99,x,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,x,x,0.01,x,0.01,x,0.01,0.01,x,x,0.01,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Vibrio chagasii','Colony: --- \n Type Strain: DSM 17138',m,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,x,0.01,x,0.01,x,x,0.01,x,x,x,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,x),
        ('Vibrio cholerae','Colony: --- \n Type Strain: ---',am,0.99,0.99,0.99,x,0.99,x,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,x,0.01,x,0.01,0.01,0.01,0.99,x,x,0.01,0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.99),
        ('Vibrio cincinnatiensis','Colony: --- \n Type Strain: ---',am,0.99,0.99,0.99,x,0.01,0.99,x,x,x,0.01,0.99,0.01,x,0.99,x,x,x,x,x,x,0.99,x,x,0.99,0.99,x,x,x,0.99,0.01,0.99,x,x,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio comitans','Colony: --- \n Type Strain: LMG 23416',m,0.99,0.99,0.99,x,0.01,x,x,x,x,0.01,0.99,0.01,x,x,x,x,x,x,x,x,0.01,x,x,0.99,0.01,0.01,x,0.01,x,0.01,0.01,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.85,x),
        ('Vibrio coralliilyticus','Colony: --- \n Type Strain: LMG 20984',m,0.99,0.99,0.99,x,0.99,0.85,x,x,x,0.01,0.99,x,x,x,x,x,x,x,x,x,0.99,x,x,0.85,0.99,0.01,x,x,x,x,0.99,x,x,x,x,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,x),
        ('Vibrio crassostreae','Colony: --- \n Type Strain: DSM 17220',m,0.99,0.99,0.99,x,0.99,x,x,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.99,x,0.01,0.01,0.01,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,x),
        ('Vibrio cyclotrophicus','Colony: --- \n Type Strain: LMG 21359',m,0.99,0.99,0.99,x,0.01,x,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.01,x,x,x,0.01,0.01,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Vibrio diabolicus','Colony: --- \n Type Strain: LMG 19805',m,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,x,0.01,0.01,0.99,x,x,0.01,0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.99),
        ('Vibrio diazothrophicus','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,0.01,x,0.99,x,x,x,x,x,x,0.01,x,x,0.99,0.01,0.01,x,x,0.99,0.01,0.99,x,x,0.85,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.15,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio ezurae','Colony: --- \n Type Strain: DSM 17533',m,0.99,0.99,0.99,x,0.99,0.01,x,x,x,0.01,0.99,0.01,x,x,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,0.01,x,0.01,0.01,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x),
        ('Vibrio fischeri','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.01,x,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.15,x,0.01,x,0.01,x,0.01,x,x,x,0.01,0.99,0.15,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,x,x,0.15,0.01),
        ('Vibrio fluvialis','Colony: --- \n Type Strain: ---',am,0.99,0.99,0.99,x,0.85,0.99,x,x,x,0.01,0.99,0.01,x,0.99,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,0.01,0.85,0.15,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio fortis','Colony: --- \n Type Strain: LMG 21557',m,0.99,0.99,0.99,x,0.99,x,x,x,x,0.01,0.99,x,x,x,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.99,x,0.01,x,0.01,x,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,x),
        ('Vibrio furnisii','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.15,0.99,x,x,x,0.01,0.99,0.99,x,0.99,x,x,x,x,x,x,0.01,x,x,0.99,x,0.01,x,0.01,0.01,0.01,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio gallicus','Colony: --- \n Type Strain: DSM 16639',am,0.99,0.99,0.99,x,x,0.01,x,x,x,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01,0.01,x,x,x,0.01,0.01,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x),
        ('Vibrio gazogenes','Colony: --- \n Type Strain: ---',m,0.99,0.01,0.99,x,0.01,0.99,x,x,x,0.01,0.99,0.99,x,0.99,x,x,x,x,x,x,0.01,x,x,0.99,0.99,x,x,0.01,0.99,x,0.99,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.01),
        ('Vibrio gigantis','Colony: --- \n Type Strain: DSM 18531',m,0.99,0.99,0.99,x,x,x,x,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.99,x,0.01,0.01,0.01,0.01,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,x),
        ('Vibrio halioticoli','Colony: --- \n Type Strain: LMG 18542',m,0.99,0.99,0.99,x,0.99,0.01,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,x,0.01,x,0.01,x,0.01,0.01,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio harveyi','Colony: --- \n Type Strain: ---',am,0.99,0.99,0.99,x,0.99,x,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,0.01,0.85,0.01,0.01,x,x,0.01,0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01),
        ('Vibrio hepatarius','Colony: --- \n Type Strain: LMG 20362',m,0.99,0.99,0.99,x,0.99,x,x,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,x,0.01,x,0.01,x,x,0.99,x,x,x,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,x),
        ('Vibrio hispanicus','Colony: --- \n Type Strain: DSM 16580',m,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.99,0.99,0.01,x,0.99,x,0.01,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Vibrio ichthyoenteri','Colony: --- \n Type Strain: LMG 19664',m,0.99,0.99,0.99,x,0.01,0.01,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.01,0.99,0.01,x,0.01,0.01,0.01,0.99,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01),
        ('Vibrio inusitatus','Colony: --- \n Type Strain: LMG 23434',m,0.99,0.99,0.99,x,0.01,0.01,x,x,x,0.01,0.99,0.01,x,x,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,0.01,x,0.01,0.01,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x),
        ('Vibrio kanaloae','Colony: --- \n Type Strain: DSM 17181',m,0.99,0.99,0.99,x,0.99,0.01,x,x,x,0.01,0.99,x,x,0.99,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,0.01,x,0.01,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.99),
        ('Vibrio lentus','Colony: --- \n Type Strain: CECT 5110',m,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,0.01,0.01,0.01,0.01,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x),
        ('Vibrio litoralis','Colony: --- \n Type Strain: DSM 17657',m,0.99,0.99,0.99,x,0.01,0.99,x,x,x,0.01,0.99,0.01,x,0.99,x,x,x,x,x,x,x,x,x,0.99,0.99,x,x,x,x,x,0.01,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,x,x,0.01,x),
        ('Vibrio logei','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.01,0.01,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.85,x,0.01,x,0.01,0.01,0.01,0.15,x,x,0.01,0.99,0.85,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01),
        ('Vibrio mediterranei','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.99,0.01,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.85,x,x,0.99,0.99,0.99,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.01),
        ('Vibrio metschnokovii','Colony: --- \n Type Strain: ---',am,0.99,0.01,0.99,x,0.15,x,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,x,0.01,x,0.01,x,x,0.99,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.85,0.85),
        ('Vibrio mimicus','Colony: --- \n Type Strain: ---',am,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.85,0.99,0.01,x,0.01,0.01,0.01,0.01,x,x,x,0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.15),
        ('Vibrio mytili','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.01,0.85,x,x,x,0.01,0.99,0.99,x,0.99,x,x,x,x,x,x,0.01,x,x,0.99,x,0.01,x,0.01,0.99,0.01,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.01),
        ('Vibrio natriegens','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.01,0.99,x,x,x,0.01,0.99,0.01,x,0.99,x,x,x,x,x,x,0.15,x,x,0.99,x,x,x,0.99,0.99,0.15,0.99,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01),
        ('Vibrio navarrensis','Colony: --- \n Type Strain: DSM 15800',m,0.99,0.99,0.99,x,0.99,0.85,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,x,0.01,x,0.01,x,0.01,0.99,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio neonatus','Colony: --- \n Type Strain: DSM 17531',m,0.99,0.99,0.99,x,0.99,0.01,x,x,x,0.01,0.99,0.01,x,x,x,x,x,x,x,x,0.01,x,x,0.99,0.01,0.01,x,0.01,x,0.01,0.01,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x),
        ('Vibrio neptunis','Colony: --- \n Type Strain: DSM 17183',m,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,0.01,x,x,0.01,0.99,0.01,x,0.01,x,0.01,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.99),
        ('Vibrio nereis','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.85,0.99,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.01,x,0.01,x,0.01,0.01,0.01,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Vibrio nigrapulchritudo','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.01,0.99,0.85,x,0.01,0.15,0.01,0.01,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio ordalii','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.01,0.99,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.15,0.01,0.01,x,0.01,0.15,0.01,0.99,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Vibrio orientalis','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.99,x,x,x,0.01,0.01,0.99,x,x,x,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01),
        ('Vibrio pacinii','Colony: --- \n Type Strain: LMG 19999',m,0.99,0.99,0.99,x,0.01,0.99,x,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,0.01,x,x,0.01,0.99,0.01,x,0.01,x,0.01,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.99),
        ('Vibrio parahaemolyticus','Colony: --- \n Type Strain: ---',am,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,0.01,x,0.85,x,x,x,x,x,x,0.01,x,x,0.99,x,0.01,x,0.01,0.01,0.01,0.01,x,x,0.01,0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01),
        ('Vibrio pectenicida','Colony: --- \n Type Strain: LMG 19642',m,0.99,0.99,0.99,x,0.01,x,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.01,0.01,0.01,x,0.99,x,0.01,0.01,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01),
        ('Vibrio pelagius I','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.01,0.99,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,x,0.01,x,0.01,0.01,0.01,0.99,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio pelagius II','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,0.01,0.01,0.01,x,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio penaeicida','Colony: --- \n Type Strain: DSM 14398',m,0.99,0.99,0.99,x,x,x,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,x,x,x,0.01,0.99,0.01,x,0.01,0.01,0.01,0.01,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio pomeroyi','Colony: --- \n Type Strain: DSM 17180',m,0.99,0.99,0.99,x,0.99,0.01,x,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,0.01,x,0.01,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,x),
        ('Vibrio ponticus','Colony: --- \n Type Strain: DSM 16217',m,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,0.85,0.85,0.01,x,0.01,0.01,0.01,0.85,x,x,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01),
        ('Vibrio proteolyticus','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,x,0.01,x,0.01,0.01,0.85,0.01,x,x,0.99,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,0.85),
        ('Vibrio rarus','Colony: --- \n Type Strain: LMG 23674',m,0.99,0.99,0.99,x,0.99,0.01,x,x,x,0.01,0.99,0.01,x,x,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,0.01,x,0.01,0.01,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x),
        ('Vibrio rhizosphaerae','Colony: --- \n Type Strain: DSM 18581',m,0.99,0.99,0.99,x,0.01,0.99,x,x,x,0.01,0.99,0.99,x,x,x,x,x,x,x,x,0.99,x,x,0.99,0.99,0.99,x,x,0.99,0.99,0.99,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99),
        ('Vibrio rotiferianus','Colony: --- \n Type Strain: DSM 17186',m,0.99,0.99,0.99,x,0.99,0.01,x,x,x,0.01,0.99,0.01,x,0.99,x,x,x,x,x,x,x,x,x,0.01,0.99,0.99,x,0.01,x,0.01,0.99,x,x,0.01,0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,x,x,0.01,0.01),
        ('Vibrio ruber','Colony: --- \n Type Strain: DSM 16370',m,0.99,0.01,0.99,x,0.01,0.99,x,x,x,0.01,0.99,0.99,x,0.99,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.99,x,x,0.99,x,0.99,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x),
        ('Vibrio rumoiensis','Colony: --- \n Type Strain: LMG 20038',m,0.99,0.99,0.99,x,0.01,0.99,x,x,x,0.01,0.99,x,x,0.99,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,0.01,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01),
        ('Vibrio salmonicida','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.01,0.01,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,x,0.01,x,0.01,0.01,0.01,0.01,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Vibrio scophthalmi','Colony: --- \n Type Strain: CECT 4638',m,0.99,0.99,0.99,x,0.01,0.01,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.01,x,0.01,x,0.01,x,0.01,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Vibrio splendidus I','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.99,x,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,0.01,0.01,0.01,0.85,x,x,0.85,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.85,0.01),
        ('Vibrio splendidus II','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,x,x,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.01,0.01,x,0.01,0.01,0.01,0.01,x,x,x,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.01),
        ('Vibrio superstes','Colony: --- \n Type Strain: DSM 16383',m,0.99,0.99,0.99,x,0.01,0.01,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.99,x,0.01,x,0.01,0.99,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x),
        ('Vibrio tapetis','Colony: --- \n Type Strain: CECT 4600',m,0.99,0.99,0.99,x,0.99,0.01,x,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,0.01,x,x,0.01,x,0.01,x,0.01,x,0.01,0.01,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio tasmaniensis','Colony: --- \n Type Strain: DSM 17182',m,0.99,0.99,0.99,x,0.99,x,x,x,x,0.01,0.99,x,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,0.01,x,0.01,0.01,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.99),
        ('Vibrio tubiashi','Colony: --- \n Type Strain: ---',m,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.85,x,0.01,0.15,0.01,0.99,x,x,0.85,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio vulnificus B1','Colony: --- \n Type Strain: ---',am,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,0.01,0.99,0.01,0.15,x,x,0.01,0.99,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio vulnificus B2','Colony: --- \n Type Strain: ---',am,0.99,0.99,0.99,x,0.01,0.99,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.01,0.99,0.01,x,0.01,0.01,0.01,0.15,x,x,0.01,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01),
        ('Vibrio vulnificus B3','Colony: --- \n Type Strain: ---',am,0.99,0.99,0.99,x,0.99,0.01,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,0.01,x,0.01,x,0.01,0.01,0.01,0.01,x,x,0.01,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01),
        ('Vibrio wodanis','Colony: --- \n Type Strain: LMG 21011',m,0.99,0.99,0.99,x,0.85,x,x,x,x,0.01,0.99,0.01,x,0.01,x,x,x,x,x,x,0.01,x,x,x,0.99,0.01,x,0.01,0.01,0.01,0.99,x,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.15,x,x,x,x,x,x,x,0.01,0.01),
        ('Vibrio xuii','Colony: --- \n Type Strain: DSM 17185',m,0.99,0.99,0.99,x,0.99,0.99,x,x,x,0.01,0.99,x,x,0.99,x,x,x,x,x,x,0.01,x,x,0.99,0.99,0.01,x,0.01,x,0.01,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.99)]
        
        # negfacbac cat+ oxi- endo- glu+ (yeast)

        # negfacbac cat- oxi- endo- glu+ (blood)

        # negfacbac cat- oxi+ endo- nit1+ glu- (blood)

        # negfacbac cat- oxi+ endo- nit1- glu+ (blood)

        # negfacbac cat+ oxi+ endo- nit1- glu+ (blood)

        # spore bacillus cat+
        self.Z = [
        ('Aneurinibacillus aneurinilyticus','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',f,0.99,0.6,0.99,x,0.01,0.01,0.99,x,x,x,0.01,x,x,0.01,0.01,x,x,0.01,0.01,x,x,0.01,x,x,0.01,x,0.01,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.99,0.99,0.99,x,x,0.01,x,0.01,x,0.01,0.01,x,x,0.99,0.01,0.8,0.8,0.99,x,x,x,x,x,0.01),
        ('Bacillus alcalophilus','Colony: circular smooth and shiny \n Color: white sometimes with dark center \n Margins: --- \n Location: --- \n Type Strain: ---',afmpsw,0.99,x,0.99,x,x,0.01,0.01,x,x,x,0.99,x,x,0.99,x,x,x,x,x,0.99,x,0.99,x,0.99,x,x,x,x,x,0.99,0.99,x,0.99,x,x,x,0.01,0.01,x,x,x,x,x,x,x,x,0.99,x,x,0.99,0.01,0.99,0.01,0.01,0.01,x,0.01,0.01,0.99,x,x,x,x,x,0.01),
        ('Bacillus aminovorans','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,x,0.99,x,0.01,0.01,0.5,x,x,x,0.99,x,x,0.01,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,0.01,0.99,0.01,0.99,0.01,x,x,x,x,x,0.01),
        ('Bacillus amyloliquefaciens','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',ms,0.99,0.99,0.99,0.5,0.01,0.22,0.78,x,x,x,0.99,x,x,x,0.99,x,x,0.99,0.99,x,x,0.99,x,x,0.89,x,0.99,x,0.99,x,x,x,0.11,0.01,0.01,0.01,0.01,0.01,x,x,0.11,0.01,0.99,0.11,x,x,0.99,x,0.99,0.99,0.11,0.99,0.5,x,0.01,0.01,0.01,0.99,0.95,x,x,x,x,x,0.99),
        ('Bacillus anthracis','Colony: 6-7 mm diameter \n Color: opaque nonpigmented \n Margins: --- \n Location: --- \n Type Strain: ---',asw,0.99,x,0.01,x,0.01,x,0.99,x,x,x,0.99,x,x,0.01,x,x,x,x,x,0.01,x,x,x,x,0.01,x,x,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,0.99,x,0.99,x,x,0.01,0.01,0.01,0.99,0.99,x,x,x,x,x,0.99),
        ('Bacillus asahii','Colony: --- \n Color: white circular \n Margins: --- \n Location: --- \n Type Strain: ---',fs,0.99,0.99,0.99,0.01,0.01,x,0.99,x,x,x,0.01,x,x,x,0.01,x,x,0.01,0.01,x,x,0.01,x,x,0.01,x,0.01,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,0.99,0.99,x,x,x,0.01,0.5,0.99,x,x,x,x,x,0.01),
        ('Bacillus atrophaeus','Colony: < 2 mm diameter \n Color: opaque smooth circular form brown/black pigment \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.01,0.99,x,x,0.99,0.99,x,x,x,0.99,x,x,0.99,x,x,x,0.99,0.5,x,x,0.01,x,x,0.5,x,x,x,0.99,x,x,x,0.99,0.01,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,0.99,x,x,0.99,x,0.99,x,0.01,0.01,0.01,0.01,0.99,0.99,x,x,x,x,x,0.99),
        ('Bacillus badius','Colony: smooth may have rhizoid-like structures \n Color: --- \n Margins: filamentous \n Location: --- \n Type Strain: ---',fms,0.99,0.01,0.99,x,0.01,0.01,0.01,x,x,x,0.01,x,x,x,0.01,x,x,0.01,0.01,x,x,0.01,x,x,0.01,x,0.01,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01,0.01,0.01,x,x,0.99,x,0.01,0.99,0.5,0.01,x,x,0.99,0.5,0.01,0.5,0.99,x,x,x,x,x,0.01),
        ('Bacillus barbaricus','Colony: 3-7 mm diameter circular flat \n Color: opaque brown \n Margins: --- \n Location: wall painting Vienna AUSTRIA \n Type Strain: ---',psw,0.99,0.01,0.01,0.01,0.01,0.01,0.01,x,x,x,0.99,x,x,x,0.01,x,x,0.5,0.5,x,x,0.5,x,x,x,x,0.01,x,0.01,x,0.5,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,0.99,x,0.01,0.01,0.01,0.01,0.99,0.01,0.99,x,x,x,x,x,x),
        ('Bacillus bataviensis','Colony: raised egg-shell texture  \n Color: cream with brown agar diffusion \n Margins: --- \n Location: agricultural fields NETHERLANDS \n Type Strain: ---',s,0.99,x,0.99,0.01,0.01,0.01,0.99,x,x,x,0.99,x,0.01,0.01,0.99,0.99,x,0.99,0.99,x,0.01,0.99,0.99,0.99,0.99,x,0.99,x,x,0.01,x,x,0.01,0.01,0.01,0.01,x,0.01,x,x,x,x,x,x,x,x,0.01,x,0.99,0.99,x,x,x,x,x,0.01,0.99,0.99,0.01,x,x,x,x,0.99,0.01),
        ('Bacillus carboniphilus','Colony: circular flat smooth \n Color: red-brown pigment \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.99,0.99,x,x,0.01,0.01,x,x,x,0.01,x,0.01,0.01,0.01,x,x,0.01,0.01,x,x,0.01,x,x,0.01,x,0.01,x,0.01,x,x,x,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,0.99,x,x,0.99,0.99,0.99,x,0.99,x,0.01,0.01,0.5,0.99,x,x,x,x,0.01,0.01),
        ('Bacillus carotarum','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.01,x,x,x,0.8,0.99,x,x,x,x,x,x,x,0.99,x,x,0.8,0.01,x,x,0.01,x,x,0.01,x,0.6,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,0.4,0.99,0.01,0.01,x,x,0.99,x,0.4,x,0.99,0.4,x,x,x,0.6,0.01,0.99,0.99,x,x,x,x,x,0.01),
        ('Bacillus cascainensis','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.01,x,x,x,0.01,0.01,x,x,x,x,x,x,x,0.99,x,x,0.99,0.99,x,x,0.99,x,x,0.99,x,0.99,x,0.99,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.99,0.01,0.01,x,x,0.99,x,0.99,x,0.86,0.01,x,x,x,0.01,0.01,0.57,0.57,x,x,x,x,x,0.01),
        ('Bacillus cereus','Colony: 2-7 mm diameter smooth moist \n Color: white-cream or pink/brown or yellow diffusion or yellow-green fluorescent \n Margins: --- \n Location: --- \n Type Strain: ---',asw,0.99,0.01,0.99,x,0.01,0.99,0.97,x,x,x,0.99,x,0.01,0.01,0.84,x,x,0.86,0.03,x,x,0.02,x,x,0.21,x,0.03,x,0.91,x,x,x,0.01,0.5,0.01,0.01,0.01,x,x,x,0.15,0.02,0.99,0.6,x,x,0.99,x,0.99,0.99,0.02,0.86,x,x,0.99,0.21,0.01,0.99,0.99,x,x,x,x,x,0.91),
        ('Bacillus circulans','Colony: 1-3 mm diameter convex egg-shell texture \n Color: opaque cream \n Margins: irregular \n Location: soil sewage food dead bees \n Type Strain: ---',asw,0.99,0.01,0.99,0.01,0.01,0.01,0.2,x,x,x,0.99,x,0.5,0.01,0.99,x,x,0.99,0.99,x,x,0.99,x,x,0.99,x,0.8,x,0.99,x,x,x,0.99,0.01,0.01,0.01,x,0.01,x,x,0.01,0.99,0.85,0.01,x,x,0.99,x,0.99,0.99,0.01,0.99,x,x,x,0.01,0.99,0.2,0.99,x,x,x,x,x,0.01),
        ('Bacillus clausii','Colony: --- \n Color: white \n Margins: filamentous \n Location: --- \n Type Strain: ---',s,0.99,x,x,x,x,x,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,0.99,0.01,0.99,0.01,0.01,x,x,0.99,0.99,0.99,x,x,x,x,x,x),
        ('Bacillus coagulans','Colony: 1-3 mm diameter convex \n Color: white \n Margins: smooth \n Location: --- \n Type Strain: ---',apw,0.99,0.01,0.99,0.01,0.01,0.01,0.99,x,x,x,0.99,x,0.01,0.01,0.2,x,x,0.99,0.5,x,x,0.01,x,x,0.99,x,0.01,x,0.01,x,x,x,0.2,0.5,0.01,0.01,x,0.01,x,x,0.01,0.99,0.15,0.01,x,x,0.01,x,0.99,0.5,0.99,0.99,x,x,0.01,0.01,0.5,0.8,0.99,x,x,x,x,x,0.60),
        ('Bacillus cohnii','Colony: 1-2 mm diameter \n Color: white \n Margins: --- \n Location: soil feces DENMARK GERMANY BRITAIN \n Type Strain: ---',fs,0.99,0.99,0.99,x,x,x,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,0.99,x,x,0.99,0.99,0.99,x,0.99,x,0.01,0.99,0.01,0.99,x,x,x,x,x,x),
        ('Bacillus decolorationis','Colony: convex glistening and rough texture \n Color: cream-beige \n Margins: smooth to irregular \n Location: mural paintings SPAIN AUSTRIA \n Type Strain: ---',s,0.99,0.99,0.99,0.01,0.01,0.01,0.99,x,x,x,0.99,x,x,0.01,0.99,0.01,x,0.99,x,x,x,x,0.99,x,x,0.01,0.01,x,0.99,0.01,0.99,0.99,0.01,0.01,0.01,0.01,x,0.01,x,x,x,x,x,x,x,x,0.99,x,0.99,0.99,x,x,x,x,x,0.01,0.99,0.99,0.01,x,x,x,x,0.01,0.01),
        ('Bacillus drentensis','Colony: eggshell texture \n Color: cream with brown agar diffusion \n Margins: regular or irregular \n Location: agricultural fields NETHERLANDS \n Type Strain: ---',s,0.99,x,0.99,0.01,0.01,0.01,0.99,x,x,x,0.99,x,0.01,0.01,0.01,0.01,x,0.99,x,0.01,0.01,0.99,0.99,0.01,x,0.99,x,0.01,0.99,0.01,x,x,0.01,0.01,0.01,0.01,x,0.01,x,x,x,x,x,x,x,x,0.01,x,0.99,0.01,x,x,x,x,x,x,0.99,0.99,0.99,x,x,x,x,x,x),
        ('Bacillus endophyticus','Colony: 1-3 mm diameter slimy rough \n Color: usually white sometimes pink or red \n Margins: --- \n Location: cotton plants TAJIKISTAN \n Type Strain: ---',p,0.99,0.99,0.99,x,0.01,0.99,0.01,x,x,x,0.99,x,0.01,0.99,0.01,x,x,x,0.01,0.01,0.99,0.01,x,0.99,0.99,0.99,x,0.99,x,x,0.99,0.01,x,0.01,x,x,0.01,x,x,x,x,x,x,x,x,x,0.01,x,x,0.01,x,0.01,x,x,x,0.01,0.01,0.01,0.99,x,x,x,x,0.99,0.01),
        ('Bacillus farraginis','Colony: 1 mm diameter raised granular texture \n Color: cream translucent \n Margins: irregular \n Location: cattle feed silage fodder \n Type Strain: ---',p,0.99,0.99,0.99,x,0.01,0.01,0.01,x,x,x,0.01,x,0.01,0.01,0.01,0.01,x,0.01,0.01,0.01,0.01,0.01,x,0.01,0.01,0.01,0.01,0.01,0.01,x,0.01,0.01,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,0.01,x,x,0.01,x,0.01,x,x,x,0.01,0.01,0.99,0.99,x,x,x,x,x,0.01),
        ('Bacillus fastidiosus','Colony: rhizoid \n Color: nonpigmented or yellow \n Margins: irregular \n Location: soil and chicken litter \n Type Strain: ---',fs,0.99,0.99,0.99,x,x,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,0.01,x,x,0.01,x,0.01,x,x,0.01,0.99,0.01,0.99,0.99,x,x,x,x,x,x),
        ('Bacillus firmus','Colony: 1-12 mm diameter eggshell glossy surface \n Color: creamy-yellow to orange-brown \n Margins: entire to rhizoid \n Location: --- \n Type Strain: ---',s,0.99,0.01,0.99,0.01,0.01,0.01,0.99,x,x,x,0.99,x,0.01,0.01,0.01,0.01,x,0.12,0.01,x,0.01,0.01,x,x,0.01,x,0.01,x,0.12,0.01,0.99,0.99,0.01,0.01,0.01,0.01,x,0.01,x,x,0.01,0.12,0.01,0.01,x,x,0.99,x,0.01,0.99,0.88,0.99,x,x,x,0.01,0.01,0.88,0.99,x,x,x,x,x,0.01),
        ('Bacillus flexus','Colony: smooth \n Color: opaque \n Margins: --- \n Location: poultry feces and soil \n Type Strain: ---',fs,0.99,0.01,0.99,x,0.01,0.99,0.01,x,x,x,0.99,x,0.01,0.01,0.01,0.01,x,0.99,0.99,0.99,x,0.99,0.99,0.99,0.01,x,0.99,0.01,x,0.01,0.99,0.99,0.01,x,x,x,0.01,x,x,x,0.01,0.01,0.01,0.01,x,x,0.99,x,0.01,0.99,0.01,0.99,0.99,x,0.01,0.99,0.01,0.99,0.99,x,x,x,x,0.99,0.01),
        ('Bacillus fordii','Colony: 2 mm diameter raised glossy smooth \n Color: cream translucent \n Margins: entire \n Location: cattle feed raw milk \n Type Strain: ---',apw,0.99,0.99,0.99,x,0.01,0.01,0.01,x,x,x,0.01,x,0.01,0.01,0.01,0.01,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,0.01,x,x,0.01,x,0.01,x,x,x,0.01,0.99,0.99,0.99,x,x,x,x,0.01,0.01),
        ('Bacillus freudenreichii','Colony: --- \n Color: --- \n Margins: --- \n Location: soil river water and sewage \n Type Strain: ---',fsw,0.99,x,0.99,x,0.01,0.01,0.01,x,x,x,0.01,x,0.01,0.01,0.01,0.01,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,0.01,x,x,0.99,x,0.01,0.99,0.99,x,x,x,x,x,0.01),
        ('Bacillus fumarioli','Colony: 3-10 mm diameter convex circular glossy \n Color: opaque creamy brown \n Margins: slightly irregular \n Location: soil or plant gelatin BELGIUM FRANCE USA \n Type Strain: ---',psw,0.99,x,0.99,x,0.01,0.01,0.01,x,x,x,0.99,x,x,0.01,0.01,0.01,x,0.99,x,x,0.01,x,x,0.99,0.99,x,x,0.01,0.01,0.01,0.99,0.99,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,0.01,x,0.01,0.99,x,x,x,x,x,0.01,0.01,0.99,0.99,x,x,x,x,0.01,0.99),
        ('Bacillus funiculus','Colony: --- \n Color: opaque off white \n Margins: --- \n Location: sewage sludge JAPAN \n Type Strain: ---',fw,0.99,0.01,0.99,x,0.01,0.01,0.99,x,x,x,0.99,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,0.99,0.01,x,0.99,x,0.01,x,0.99,0.01,0.99,0.99,x,x,x,x,x,0.99),
        ('Bacillus galactosidilyticus','Colony: 1 mm diameter smooth flat \n Color: cream-offwhite with opaque center \n Margins: irregular rhizoid projections \n Location: raw milk decomposed wheat grain infant bile \n Type Strain: ---',apw,0.99,x,0.99,0.01,0.01,0.01,0.99,x,x,x,0.99,x,0.01,x,x,0.01,x,0.99,x,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,0.01,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,0.99,x,0.99,0.01,x,x,x,x,x,x,0.99,0.99,0.99,x,x,x,x,0.99,0.01),
        ('Bacillus gelatini','Colony: 1-4 mm diameter smooth waxy eggshell texture \n Color: opaque cream with darker center \n Margins: irregular \n Location: plant gelatin \n Type Strain: ---',p,0.99,0.01,0.99,0.01,0.01,0.01,0.01,x,x,x,0.99,x,0.01,0.01,x,0.01,x,0.99,x,0.99,x,0.01,0.99,0.99,0.99,0.01,0.01,0.01,0.01,0.01,0.01,0.99,0.01,0.01,0.01,0.01,x,0.01,x,x,x,x,x,x,x,x,0.99,x,0.99,0.99,x,x,x,x,x,0.01,0.01,0.99,0.99,x,x,x,x,0.01,0.01),
        ('Bacillus gibsonii','Colony: circular smooth shiny \n Color: yellow \n Margins: --- \n Location: --- \n Type Strain: ---',s,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,0.99,0.01,0.01,0.01,0.01,x,x,0.01,0.99,0.99,x,x,x,x,x,x),
        ('Bacillus insolitus','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,x,0.99,x,0.01,0.01,0.01,x,x,x,0.01,x,0.01,0.01,0.01,0.01,x,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,x,0.01,x,0.01,0.01,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,0.01,x,x,0.01,0.01,0.01,0.99,0.01,x,x,x,x,x,0.01),
        ('Bacillus kaustophilus','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.01,x,x,x,0.99,0.99,x,x,x,x,x,x,x,0.99,x,x,0.99,0.2,x,x,0.01,x,x,0.99,x,0.2,x,0.4,x,x,x,0.99,x,x,x,x,x,x,x,0.01,0.99,0.01,0.01,x,x,0.2,x,0.99,x,0.99,0.99,x,x,x,0.01,0.99,0.01,0.99,x,x,x,x,x,0.01),
        ('Bacillus lentus','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.99,0.99,x,0.01,0.01,0.01,x,x,x,0.99,x,x,x,0.5,x,x,0.01,0.5,x,x,0.01,x,0.99,0.25,x,0.01,x,0.5,x,x,x,0.35,x,x,x,x,x,x,x,0.01,0.99,0.01,0.99,x,x,0.01,x,0.99,x,0.99,0.99,x,x,x,0.99,0.01,0.99,0.99,x,x,x,x,x,0.01),
        ('Bacillus licheniformis','Colony: dull rough surface hair-like outgrowths \n Color: opaque sometimes with red or brown pigmentation \n Margins: --- \n Location: --- \n Type Strain: ---',afsw,0.99,0.1,0.99,x,0.01,0.95,0.99,x,x,x,0.99,x,x,0.99,0.99,x,x,0.99,0.95,x,x,0.68,x,0.99,0.99,x,0.95,x,0.99,x,x,x,0.95,x,x,x,x,x,x,x,0.9,0.42,0.99,0.95,x,x,0.99,x,0.99,0.99,0.01,0.99,x,x,x,0.32,0.01,0.99,0.99,x,x,x,x,x,0.99),
        ('Bacillus macroides','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',fpw,0.99,x,0.99,x,0.01,0.01,0.01,x,x,x,0.01,x,x,0.01,0.01,x,x,0.01,0.01,x,x,0.01,x,x,0.01,x,0.01,x,0.01,x,x,x,0.01,x,x,x,0.99,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,0.01,x,x,x,x,x,0.01,0.99,x,x,x,x,x,0.01),
        ('Bacillus megaterium','Colony: glossy mucoid \n Color: yellow brown or black \n Margins: --- \n Location: --- \n Type Strain: ---',afs,0.99,0.01,0.99,x,0.01,0.99,0.01,x,x,x,0.99,x,x,x,0.99,x,x,0.99,0.99,x,x,0.27,x,x,0.45,x,0.01,x,0.99,x,x,x,0.99,x,x,x,x,x,x,x,0.09,0.01,0.01,0.01,x,x,0.99,x,0.99,0.99,0.09,0.99,x,x,x,0.82,0.01,0.99,0.99,x,x,x,x,x,0.01),
        ('Bacillus mycoides','Colony: rhizoid \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',asw,0.99,x,0.99,x,0.01,x,0.99,x,x,x,0.99,x,x,0.01,x,x,x,x,x,x,x,x,x,0.01,0.01,x,x,x,x,x,x,0.99,0.01,0.01,x,x,0.99,x,x,x,x,x,x,x,x,x,0.99,x,x,0.99,x,x,x,x,x,x,0.01,0.99,0.99,x,x,x,x,x,0.99),
        ('Bacillus psychrophilus','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.2,0.99,x,x,0.01,0.8,x,x,x,x,x,x,x,0.2,x,x,0.6,0.01,x,x,0.01,x,x,0.01,x,0.01,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01,0.01,0.01,x,x,0.99,x,0.2,x,0.99,0.01,x,x,x,0.99,0.99,0.99,0.01,x,x,x,x,x,0.01),
        ('Bacillus psychrosaccharolyticus','Colony: thick growth \n Color: opaque \n Margins: --- \n Location: --- \n Type Strain: ---',sw,0.99,x,0.99,x,0.01,0.01,0.99,x,x,x,0.99,x,x,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,0.01,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,0.99,x,x,0.01,x,0.99,0.99,0.99,x,x,x,x,x,0.01),
        ('Bacillus pumilis','Colony: smooth \n Color: yellow \n Margins: --- \n Location: --- \n Type Strain: ---',afs,0.99,0.1,0.99,x,0.01,0.9,0.01,x,x,x,0.99,x,x,0.99,0.99,x,x,0.99,0.9,x,x,0.45,x,0.99,0.99,x,0.75,x,0.99,x,x,x,0.95,x,x,x,x,x,x,x,0.99,0.01,0.99,0.01,x,x,0.99,x,0.99,x,x,0.01,x,x,x,0.01,0.01,0.95,0.95,x,x,x,x,x,0.99),
        ('Bacillus simplex','Colony: 3-6 mm diameter raised umbonate \n Color: cream glossy \n Margins: irregular \n Location: --- \n Type Strain: ---',s,0.99,0.01,0.99,0.01,0.01,0.99,0.99,x,x,x,0.99,x,x,0.99,0.99,x,x,0.99,0.01,0.01,0.01,0.01,x,0.99,0.5,0.01,0.01,x,0.5,x,0.99,0.99,0.99,0.01,0.01,0.01,x,x,x,x,0.99,0.99,0.01,0.01,x,x,0.99,x,0.01,x,0.99,0.99,x,x,x,0.01,0.01,0.99,0.99,x,x,x,x,0.01,0.99),
        ('Bacillus smithii','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.01,x,x,x,0.99,0.99,x,x,x,0.99,x,x,x,0.01,x,x,0.99,0.01,x,x,0.01,x,x,0.01,x,0.01,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.99,0.01,0.01,x,x,0.99,x,0.67,x,0.99,0.99,x,x,x,0.01,0.33,0.67,0.99,x,x,x,x,x,0.01),
        ('Bacillus sphaericus','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.89,x,x,x,0.33,0.44,x,x,x,x,x,x,x,0.01,x,x,0.01,0.01,x,x,0.01,x,x,0.01,x,0.01,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,0.33,0.99,0.44,0.99,x,x,0.89,x,0.01,x,0.11,0.01,x,x,x,0.01,0.89,0.11,0.01,x,x,x,x,x,0.01),
        ('Bacillus stearothermophilus','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.01,x,x,x,0.5,0.99,x,x,x,0.99,x,x,x,0.01,x,x,0.99,0.01,x,x,0.01,x,x,0.75,x,0.75,x,0.25,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.99,0.01,0.01,x,x,0.75,x,0.99,x,0.99,0.99,x,x,x,0.01,0.99,0.01,0.99,x,x,x,x,x,0.01),
        ('Bacillus subtilis','Colony: dull rugose \n Color: cream-yellow or orange or pink-red or brown-black \n Margins: round or irregular \n Location: --- \n Type Strain: ---',afpsw,0.99,0.01,0.99,x,x,0.87,0.99,x,x,x,0.99,x,x,x,0.99,x,x,0.99,0.33,x,x,0.13,x,x,0.99,x,0.99,x,0.99,x,x,x,0.8,0.01,0.01,0.01,x,x,x,x,0.01,0.01,0.99,0.73,x,x,0.99,x,0.99,x,0.27,0.99,x,x,x,0.01,0.01,0.99,0.99,x,x,x,x,0.99,0.99),
        ('Bacillus Taxon 18','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.01,x,x,x,0.01,0.99,x,x,x,x,x,x,x,0.01,x,x,0.99,0.01,x,x,0.01,x,x,0.01,x,0.01,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01,0.99,0.99,x,x,0.99,x,0.99,x,0.01,0.99,x,x,x,0.01,0.01,0.99,0.99,x,x,x,x,x,0.99),
        ('Bacillus Taxon 21','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.01,x,x,x,0.99,0.99,x,x,x,x,x,x,x,0.99,x,x,0.99,0.99,x,x,0.01,x,x,0.99,x,0.99,x,0.99,x,x,x,0.99,x,x,x,x,x,x,x,0.99,0.99,0.99,0.99,x,x,0.99,x,0.99,x,0.01,0.99,x,x,x,0.99,0.99,0.5,0.5,x,x,x,x,x,0.99),
        ('Bacillus Taxon 24','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.01,x,x,x,0.5,0.01,x,x,x,x,x,x,x,0.5,x,x,0.99,0.99,x,x,0.01,x,x,0.99,x,0.99,x,0.99,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01,0.01,0.01,x,x,0.99,x,0.99,x,0.01,0.5,x,x,x,0.99,0.01,0.99,0.99,x,x,x,x,x,0.01),
        ('Bacillus Taxon 26','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.01,x,x,x,0.99,0.99,x,x,x,x,x,x,x,0.01,x,x,0.5,0.01,x,x,0.01,x,x,0.01,x,0.01,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01,0.01,0.01,x,x,0.99,x,0.01,x,0.5,0.99,x,x,x,0.01,0.01,0.99,0.99,x,x,x,x,x,0.01),
        ('Bacillus Taxon 27','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.17,x,x,x,0.5,0.01,x,x,x,x,x,x,x,0.67,x,x,0.67,0.01,x,x,0.01,x,x,0.17,x,0.01,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01,0.01,0.01,x,x,0.99,x,0.99,x,0.01,0.63,x,x,x,0.01,0.17,0.83,0.99,x,x,x,x,x,0.01),
        ('Bacillus Taxon 28','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.01,x,x,x,0.01,0.01,x,x,x,x,x,x,x,0.01,x,x,0.01,0.01,x,x,0.01,x,x,0.01,x,0.01,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01,0.01,0.01,x,x,0.99,x,0.99,x,0.01,0.5,x,x,x,0.01,0.01,0.99,0.99,x,x,x,x,x,0.01),
        ('Bacillus Taxon 29','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.01,x,x,x,0.99,0.01,x,x,x,x,x,x,x,0.01,x,x,0.01,0.01,x,x,0.01,x,x,0.01,x,0.01,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01,0.01,0.01,x,x,0.99,x,0.99,x,0.5,0.99,x,x,x,0.01,0.01,0.99,0.99,x,x,x,x,x,0.01),
        ('Bacillus Taxon 33','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.01,x,x,x,0.99,0.01,x,x,x,x,x,x,x,0.5,x,x,0.01,0.01,x,x,0.01,x,x,0.01,x,0.01,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,0.5,0.99,0.01,0.01,x,x,0.99,x,0.99,x,0.99,0.01,x,x,x,0.01,0.01,0.01,0.99,x,x,x,x,x,0.01),
        ('Bacillus Taxon 4','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.99,x,x,x,0.5,0.33,x,x,x,x,x,x,x,0.99,x,x,0.99,0.99,x,x,0.99,x,x,0.99,x,0.99,x,0.99,x,x,x,0.99,x,x,x,x,x,x,x,0.99,0.01,0.17,0.99,x,x,0.83,x,0.99,x,0.99,0.99,x,x,x,0.01,0.99,0.01,0.99,x,x,x,x,x,0.01),
        ('Bacillus Taxon 41','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.01,x,x,x,0.01,0.01,x,x,x,x,x,x,x,0.01,x,x,0.01,0.01,x,x,0.01,x,x,0.01,x,0.01,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.99,0.99,0.99,x,x,0.99,x,0.01,x,0.01,0.01,x,x,x,0.99,0.99,0.01,0.99,x,x,x,x,x,0.01),
        ('Bacillus thuringiensis','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,x,0.99,x,0.01,0.99,0.99,x,x,x,0.99,x,x,0.01,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01,0.99,x,x,0.99,x,x,x,x,x,x,x,x,x,0.99,x,x,0.99,x,0.99,x,x,x,x,0.01,0.99,0.99,x,x,x,x,x,0.99),
        ('Brevibacillus brevis','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',asw,0.99,0.01,0.99,x,0.01,0.45,0.91,x,x,x,0.99,x,x,0.01,0.01,x,x,0.73,0.01,x,x,0.01,x,x,0.01,x,0.09,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,0.15,0.73,0.99,0.99,x,x,0.99,x,0.01,x,0.91,0.01,x,x,x,0.01,0.99,0.82,0.91,x,x,x,x,x,0.01),
        ('Brevibacillus laterosporus','Colony: --- \n Color: white-yellow \n Margins: --- \n Location: larval honey bees \n Type Strain: ---',aw,0.99,0.11,0.99,x,x,0.11,0.99,x,x,x,0.99,x,x,x,0.2,x,x,0.6,0.01,x,x,0.01,x,0.99,0.01,x,0.01,x,0.4,x,x,x,0.01,x,x,x,x,x,x,x,0.15,0.01,0.99,0.15,x,x,0.99,x,0.6,0.99,0.67,0.01,x,x,x,0.01,0.89,0.99,0.99,x,x,x,x,x,0.01),
        ('Geobacillus stearothermophilus','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',asw,x,x,0.99,x,0.01,x,x,x,x,x,0.99,x,x,0.99,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,x,x,x,0.99,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,x,x,x,0.99,0.01,0.99,x,x,x,x,x,0.01),
        ('Lysinibacillus fusiformis','Colony: smooth \n Color: opaque \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.5,0.99,0.01,0.01,0.99,0.01,x,x,x,0.01,x,x,0.01,0.01,x,x,0.01,0.01,x,x,0.01,x,0.01,0.01,x,0.01,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.99,0.25,0.25,x,x,0.99,x,0.01,x,0.01,0.01,x,x,x,0.75,0.99,0.5,0.25,x,x,x,x,0.01,0.01),
        ('Lysinibacillus sphaericus','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',asw,0.99,x,0.99,x,0.01,x,0.01,x,x,x,0.01,x,x,0.01,0.01,x,x,0.01,0.01,x,x,0.01,x,0.01,0.01,x,0.01,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,0.99,x,0.01,x,x,x,x,0.99,0.01,0.01,x,x,x,x,x,0.01),
        ('Paenibacillus alvei','Colony: 1-3 mm diameter \n Color: white-yellow \n Margins: irregular \n Location: --- \n Type Strain: ---',asw,0.99,0.99,0.99,x,0.99,0.01,0.01,x,x,x,0.99,x,x,0.01,0.92,x,x,0.01,0.54,x,x,0.01,x,x,0.15,x,0.99,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01,0.99,0.92,x,x,0.99,x,0.99,0.99,0.99,0.99,x,x,x,0.31,0.92,0.23,0.99,x,x,x,x,x,0.99),
        ('Paenibacillus amylolyticus','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.99,0.99,x,x,0.01,0.99,x,x,x,0.99,x,x,x,0.99,x,x,0.99,0.99,x,x,0.99,x,x,0.33,x,0.99,x,0.99,x,x,x,0.99,x,x,x,x,x,x,x,0.03,0.99,0.01,0.01,x,x,0.33,x,0.6,x,0.33,0.99,x,x,x,0.01,0.99,0.01,0.99,x,x,x,x,x,0.01),
        ('Paenibacillus apiarius','Colony: 1 mm diameter smooth \n Color: translucent \n Margins: entire \n Location: dead larval honey bees \n Type Strain: ---',a,0.99,0.99,0.99,x,0.01,0.99,0.99,x,x,x,0.99,x,x,0.01,0.99,x,x,0.01,0.99,x,x,0.01,x,x,0.01,x,0.99,x,0.99,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01,0.99,0.99,x,x,0.99,x,0.99,x,0.99,0.99,x,x,0.99,0.99,0.99,0.99,0.99,x,x,x,x,x,0.01),
        ('Paenibacillus larvae pulvifaciens','Colony: 3 mm diameter \n Color: unpigmented buff or red \n Margins: --- \n Location: larval honey bees \n Type Strain: ---',a,0.99,0.01,0.99,x,0.01,x,0.99,x,x,x,x,x,x,x,0.01,x,x,0.99,0.01,x,x,0.99,x,x,0.01,x,0.01,x,0.01,x,x,x,0.01,x,x,x,x,x,x,x,0.01,0.01,0.99,0.67,x,x,0.99,x,0.01,x,0.33,0.01,x,x,x,0.01,0.99,0.99,0.99,x,x,x,x,x,0.01),
        ('Paenibacillus lentimorbus','Colony: < 1 mm diameter \n Color: cream-brown \n Margins: --- \n Location: infects larval insects \n Type Strain: ---',a,0.01,x,0.99,x,0.01,0.01,0.01,x,x,x,0.99,x,x,0.01,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,0.01,x,0.01,x,x,x,x,0.99,0.99,0.99,x,x,x,x,x,0.01),
        ('Paenibacillus macerans','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',apw,0.99,0.99,0.99,x,x,0.01,0.99,x,x,x,x,x,x,x,0.99,x,x,0.99,0.9,x,x,0.99,x,x,0.9,x,0.9,x,0.99,x,x,x,0.99,x,x,x,x,x,x,x,0.1,0.01,0.99,0.99,x,x,0.01,x,0.99,x,0.5,0.99,x,x,x,0.01,0.99,0.01,0.99,x,x,x,x,x,0.01),
        ('Paenibacillus macquariensis','Colony: --- \n Color: --- \n Margins: --- \n Location: soil ANTARCTICA \n Type Strain: ---',s,0.99,x,0.99,x,0.01,0.01,0.01,x,x,x,0.99,x,x,0.01,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,x,0.99,x,x,x,0.01,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,0.99,x,x,0.01,x,0.99,0.01,0.99,x,x,x,x,x,0.01),
        ('Paenibacillus pabuli','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.99,x,x,x,0.01,0.01,x,x,x,x,x,x,x,0.99,x,x,0.99,0.5,x,x,0.99,x,x,0.99,x,0.99,x,0.99,x,x,x,0.99,x,x,x,x,x,x,x,0.99,0.01,0.99,0.99,x,x,0.99,x,0.99,x,0.01,0.99,x,x,x,0.01,0.99,0.5,0.99,x,x,x,x,x,0.01),
        ('Paenibacillus polymyxa','Colony: --- \n Color: --- \n Margins: --- \n Location: --- \n Type Strain: ---',s,0.99,0.01,x,x,0.01,0.18,0.99,x,x,x,x,x,x,x,0.99,x,x,0.99,0.91,x,x,0.91,x,x,0.82,x,0.99,x,0.99,x,x,x,0.91,x,x,x,x,x,x,x,0.09,0.01,0.99,0.64,x,x,0.99,x,0.99,x,0.01,0.99,x,x,x,0.01,0.91,0.64,0.99,x,x,x,x,x,0.99),
        ('Paenibacillus popilliae','Colony: --- \n Color: --- \n Margins: --- \n Location: isolated from larval insects \n Type Strain: ---',a,0.01,x,x,x,0.01,0.01,0.01,x,x,x,0.99,x,x,0.01,x,x,x,x,x,x,x,x,x,0.01,x,x,x,x,x,x,x,0.99,0.01,x,x,x,x,x,x,x,x,x,x,x,x,x,0.01,x,x,0.01,x,0.01,x,x,x,x,0.99,x,0.99,x,x,x,x,x,0.01),
        ('Paenibacillus thiaminolyticus','Colony: 1-2 mm diameter smooth \n Color: translucent \n Margins: entire \n Location: --- \n Type Strain: ---',af,0.99,0.99,0.99,x,0.99,0.01,0.99,x,x,x,0.99,x,x,0.01,0.99,x,x,0.99,0.99,x,x,0.99,0.99,0.01,0.99,x,0.99,x,0.99,x,x,0.99,0.01,0.01,0.01,0.01,x,x,x,x,0.01,0.99,0.99,0.01,x,x,0.99,x,0.99,x,0.99,0.99,x,x,x,x,0.99,0.01,0.99,x,x,x,x,x,0.01),
        ('Virgibacillus pantothenticus','Colony: 1-4 mm diameter convex \n Color: opaque or creamy-grey \n Margins: slightly irregular \n Location: --- \n Type Strain: ---',s,0.99,0.22,0.99,0.01,0.01,0.01,0.99,x,x,x,0.99,x,0.01,x,0.01,0.01,x,0.67,0.01,x,x,0.01,x,0.01,0.99,x,0.01,x,0.99,x,x,0.99,0.01,0.01,x,x,x,x,x,x,0.67,0.99,0.01,0.01,x,x,0.99,x,0.99,x,0.01,0.99,x,x,x,0.01,0.99,0.01,0.99,x,x,x,x,x,0.01)]

    def searchbuttonclick(self, event):
        self.id_frame.destroy()
        self.id_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.id_frame.pack(side=TOP, fill=BOTH)

        # button defaults
        self.adon_option.set("?")
        self.ala_option.set("?")
        self.amp_option.set("?")
        self.amy_option.set("?")
        self.amyg_option.set("?")
        self.arab_option.set("?")
        self.arg_option.set("?")
        self.asp_option.set("?")
        self.cas_option.set("?")
        self.cat_option.set("?")
        self.cell_option.set("?")
        self.ceph_option.set("?")
        self.chi_option.set("?")
        self.chlor_option.set("?")
        self.cit_option.set("?")
        self.coag_option.set("?")
        self.dna_option.set("?")
        self.dul_option.set("?")
        self.endo_b_option.set("?")
        self.endo_c_option.set("?")
        self.endo_o_option.set("?")
        self.esc_option.set("?")
        self.ethan_option.set("?")
        self.fru_option.set("?")        
        self.galac_option.set("?")
        self.gel_option.set("?")
        self.glug_option.set("?")
        self.glu_option.set("?")
        self.glut_option.set("?")
        self.glux_option.set("?")
        self.glyc_option.set("?")
        self.h2s_option.set("?")
        self.hem_option.set("?")
        self.hip_option.set("?")
        self.hist_option.set("?")
        self.ind_option.set("?")
        self.ino_option.set("?")
        self.lac_option.set("?")
        self.lys_option.set("?")
        self.mal_option.set("?")
        self.man_option.set("?")
        self.mann_option.set("?")
        self.meli_option.set("?")
        self.motil_option.set("?")
        self.nal_option.set("?")
        self.nit1_option.set("?")
        self.nit2_option.set("?")
        self.nit3_option.set("?")
        self.onpg_option.set("?")
        self.orn_option.set("?")
        self.oxi_option.set("?")
        self.phen_option.set("?")
        self.phos_option.set("?")
        self.poly_option.set("?")
        self.raf_option.set("?")
        self.rham_option.set("?")
        self.sal_option.set("?")
        self.salt_option.set("?")
        self.sorb_option.set("?")
        self.starch_option.set("?")
        self.strep_option.set("?")
        self.suc_option.set("?")
        self.temp_option.set("?")
        self.tre_option.set("?")
        self.trypto_option.set("?")
        self.tw20_option.set("?")
        self.tw80_option.set("?")
        self.tyro_option.set("?")
        self.urea_option.set("?")
        self.val_option.set("?")
        self.vp_option.set("?")
        self.xyl_option.set("?")

        if (self.group_option.get()=="Gram Negative Facultative Anaerobe Bacillus" and self.fast_option.get()=="None"):
            bac=self.A+self.B+self.C+self.D
        if (self.group_option.get()=="Gram Negative Facultative Anaerobe Bacillus" and self.fast_option.get()=="Salt"):
            bac=self.E
        if (self.group_option.get()=="Gram Negative Aerobe Bacillus" and self.fast_option.get()=="None"):
            nothing
        if (self.group_option.get()=="Gram Negative Aerobe Coccus" and self.fast_option.get()=="None"):
            nothing
        if (self.group_option.get()=="Gram Positive Facultative Anaerobe Bacillus" and self.fast_option.get()=="None"):
            nothing
        if (self.group_option.get()=="Gram Positive Aerobe Bacillus" and self.fast_option.get()=="None"):
            nothing
        if (self.group_option.get()=="Gram Positive Facultative Anaerobe Coccus" and self.fast_option.get()=="None"):
            nothing
        if (self.group_option.get()=="Gram Positive Aerobe Coccus" and self.fast_option.get()=="None"):
            nothing
        if (self.group_option.get()=="Spore Forming Bacillus and Coccus" and self.fast_option.get()=="None"):
            bac=self.Z

        for isolates in bac:
            i = bac.index(isolates)
            if self.enter.get()==bac[i][0]:

                bacwin = Toplevel(background="white")
                Label(bacwin, text = bac[i][0], font = "bold", background = "white").pack(side=TOP, anchor = N)
                Label(bacwin, text = bac[i][1], background = "white").pack(side=LEFT)
                
                Label(self.id_frame, text = bac[i][0], background = "white").pack(side=TOP, anchor = N)
                if bac[i][3]>= 0.85: self.cat_option.set('+')
                if bac[i][3]<= 0.15: self.cat_option.set('--')
                if bac[i][4]>= 0.85: self.oxi_option.set('+')
                if bac[i][4]<= 0.15: self.oxi_option.set('--')
                if bac[i][5]>= 0.85: self.motil_option.set('+')
                if bac[i][5]<= 0.15: self.motil_option.set('--')
                if bac[i][6]>= 0.85: self.h2s_option.set('+')
                if bac[i][6]<= 0.15: self.h2s_option.set('--')
                if bac[i][7]>= 0.85: self.ind_option.set('+')
                if bac[i][7]<= 0.15: self.ind_option.set('--')
                if bac[i][8]>= 0.85: self.cit_option.set('+')
                if bac[i][8]<= 0.15: self.cit_option.set('--')
                if bac[i][9]>= 0.85: self.nit1_option.set('+')
                if bac[i][9]<= 0.15: self.nit1_option.set('--')
                if bac[i][10]>= 0.85: self.nit2_option.set('+')
                if bac[i][10]<= 0.15: self.nit2_option.set('--')
                if bac[i][11]>= 0.85: self.nit3_option.set('+')
                if bac[i][11]<= 0.15: self.nit3_option.set('--')
                if bac[i][12]>= 0.85: self.glux_option.set('+')
                if bac[i][12]<= 0.15: self.glux_option.set('--')
                if bac[i][13]>= 0.85: self.glu_option.set('+')
                if bac[i][13]<= 0.15: self.glu_option.set('--')
                if bac[i][14]>= 0.85: self.glug_option.set('+')
                if bac[i][14]<= 0.15: self.glug_option.set('--')
                if bac[i][15]>= 0.85: self.adon_option.set('+')
                if bac[i][15]<= 0.15: self.adon_option.set('--')
                if bac[i][16]>= 0.85: self.arab_option.set('+')
                if bac[i][16]<= 0.15: self.arab_option.set('--')
                if bac[i][17]>= 0.85: self.cell_option.set('+')
                if bac[i][17]<= 0.15: self.cell_option.set('--')
                if bac[i][18]>= 0.85: self.dul_option.set('+')
                if bac[i][18]<= 0.15: self.dul_option.set('--')
                if bac[i][19]>= 0.85: self.ethan_option.set('+')
                if bac[i][19]<= 0.15: self.ethan_option.set('--')
                if bac[i][20]>= 0.85: self.fru_option.set('+')
                if bac[i][20]<= 0.15: self.fru_option.set('--')
                if bac[i][21]>= 0.85: self.galac_option.set('+')
                if bac[i][21]<= 0.15: self.galac_option.set('--')
                if bac[i][22]>= 0.85: self.glyc_option.set('+')
                if bac[i][22]<= 0.15: self.glyc_option.set('--')
                if bac[i][23]>= 0.85: self.ino_option.set('+')
                if bac[i][23]<= 0.15: self.ino_option.set('--')
                if bac[i][24]>= 0.85: self.lac_option.set('+')
                if bac[i][24]<= 0.15: self.lac_option.set('--')
                if bac[i][25]>= 0.85: self.mal_option.set('+')
                if bac[i][25]<= 0.15: self.mal_option.set('--')
                if bac[i][26]>= 0.85: self.man_option.set('+')
                if bac[i][26]<= 0.15: self.man_option.set('--')
                if bac[i][27]>= 0.85: self.mann_option.set('+')
                if bac[i][27]<= 0.15: self.mann_option.set('--')
                if bac[i][28]>= 0.85: self.meli_option.set('+')
                if bac[i][28]<= 0.15: self.meli_option.set('--')
                if bac[i][29]>= 0.85: self.raf_option.set('+')
                if bac[i][29]<= 0.15: self.raf_option.set('--')
                if bac[i][30]>= 0.85: self.rham_option.set('+')
                if bac[i][30]<= 0.15: self.rham_option.set('--')
                if bac[i][31]>= 0.85: self.sal_option.set('+')
                if bac[i][31]<= 0.15: self.sal_option.set('--')
                if bac[i][32]>= 0.85: self.sorb_option.set('+')
                if bac[i][32]<= 0.15: self.sorb_option.set('--')
                if bac[i][33]>= 0.85: self.suc_option.set('+')
                if bac[i][33]<= 0.15: self.suc_option.set('--')
                if bac[i][34]>= 0.85: self.tre_option.set('+')
                if bac[i][34]<= 0.15: self.tre_option.set('--')
                if bac[i][35]>= 0.85: self.xyl_option.set('+')
                if bac[i][35]<= 0.15: self.xyl_option.set('--')
                if bac[i][36]>= 0.85: self.arg_option.set('+')
                if bac[i][36]<= 0.15: self.arg_option.set('--')
                if bac[i][37]>= 0.85: self.lys_option.set('+')
                if bac[i][37]<= 0.15: self.lys_option.set('--')
                if bac[i][38]>= 0.85: self.orn_option.set('+')
                if bac[i][38]<= 0.15: self.orn_option.set('--')
                if bac[i][39]>= 0.85: self.phen_option.set('+')
                if bac[i][39]<= 0.15: self.phen_option.set('--')
                if bac[i][40]>= 0.85: self.trypto_option.set('+')
                if bac[i][40]<= 0.15: self.trypto_option.set('--')
                if bac[i][41]>= 0.85: self.amp_option.set('+')
                if bac[i][41]<= 0.15: self.amp_option.set('--')
                if bac[i][42]>= 0.85: self.ceph_option.set('+')
                if bac[i][42]<= 0.15: self.ceph_option.set('--')
                if bac[i][43]>= 0.85: self.chlor_option.set('+')
                if bac[i][43]<= 0.15: self.chlor_option.set('--')
                if bac[i][44]>= 0.85: self.nal_option.set('+')
                if bac[i][44]<= 0.15: self.nal_option.set('--')
                if bac[i][45]>= 0.85: self.poly_option.set('+')
                if bac[i][45]<= 0.15: self.poly_option.set('--')
                if bac[i][46]>= 0.85: self.strep_option.set('+')
                if bac[i][46]<= 0.15: self.strep_option.set('--')
                if bac[i][47]>= 0.85: self.amy_option.set('+')
                if bac[i][47]<= 0.15: self.amy_option.set('--')
                if bac[i][48]>= 0.85: self.amyg_option.set('+')
                if bac[i][48]<= 0.15: self.amyg_option.set('--')
                if bac[i][49]>= 0.85: self.cas_option.set('+')
                if bac[i][49]<= 0.15: self.cas_option.set('--')
                if bac[i][50]>= 0.85: self.chi_option.set('+')
                if bac[i][50]<= 0.15: self.chi_option.set('--')
                if bac[i][51]>= 0.85: self.esc_option.set('+')
                if bac[i][51]<= 0.15: self.esc_option.set('--')
                if bac[i][52]>= 0.85: self.gel_option.set('+')
                if bac[i][52]<= 0.15: self.gel_option.set('--')
                if bac[i][53]>= 0.85: self.hip_option.set('+')
                if bac[i][53]<= 0.15: self.hip_option.set('--')
                if bac[i][54]>= 0.85: self.starch_option.set('+')
                if bac[i][54]<= 0.15: self.starch_option.set('--')
                if bac[i][55]>= 0.85: self.tw20_option.set('+')
                if bac[i][55]<= 0.15: self.tw20_option.set('--')
                if bac[i][56]>= 0.85: self.tw80_option.set('+')
                if bac[i][56]<= 0.15: self.tw80_option.set('--')
                if bac[i][57]>= 0.85: self.tyro_option.set('+')
                if bac[i][57]<= 0.15: self.tyro_option.set('--')
                if bac[i][58]>= 0.85: self.urea_option.set('+')
                if bac[i][58]<= 0.15: self.urea_option.set('--')
                if bac[i][59]>= 0.85: self.endo_b_option.set('+')
                if bac[i][59]<= 0.15: self.endo_b_option.set('--')
                if bac[i][60]>= 0.85: self.endo_c_option.set('+')
                if bac[i][60]<= 0.15: self.endo_c_option.set('--')
                if bac[i][61]>= 0.85: self.endo_o_option.set('+')
                if bac[i][61]<= 0.15: self.endo_o_option.set('--')
                if bac[i][62]>= 0.85: self.coag_option.set('+')
                if bac[i][62]<= 0.15: self.coag_option.set('--')
                if bac[i][63]>= 0.85: self.dna_option.set('+')
                if bac[i][63]<= 0.15: self.dna_option.set('--')
                if bac[i][64]>= 0.85: self.phos_option.set('+')
                if bac[i][64]<= 0.15: self.phos_option.set('--')
                if bac[i][65]>= 0.85: self.hem_option.set('+')
                if bac[i][65]<= 0.15: self.hem_option.set('--')
                if bac[i][66]>= 0.85: self.onpg_option.set('+')
                if bac[i][66]<= 0.15: self.onpg_option.set('--')
                if bac[i][67]>= 0.85: self.vp_option.set('+')
                if bac[i][67]<= 0.15: self.vp_option.set('--')

    def idbuttonclick(self, event):
        self.id_frame.destroy()
        self.id_frame = Frame(self.main_right_frame, borderwidth=5, height=50, background="white")
        self.id_frame.pack(side=TOP, fill=BOTH)

        bac=()

        if (self.gram_option.get()=="?" or
        self.shape_option.get()=="?" or
        self.meta_option.get()=="?" or
        self.endo_option.get()=="?" or
        self.cat_option.get()=="?" or
        self.oxi_option.get()=="?" or
        self.glu_option.get()=="?"):
            Label(self.id_frame, text = "Error: need more data \n", background = "white").pack(side=TOP, anchor = N)
            
        if (self.group_option.get()=="Gram Negative Facultative Anaerobe Bacillus" and
        self.fast_option.get()=="None" and
        self.gram_option.get()=="--" and
        self.shape_option.get()=="bacillus" and
        self.meta_option.get()=="fac anaerobe" and
        self.endo_option.get()=="--" and
        self.cat_option.get()=="--" and
        self.oxi_option.get()=="--" and
        self.nit1_option.get()=="--" and
        self.glu_option.get()=="+"):
            bac=self.A

        if (self.group_option.get()=="Gram Negative Facultative Anaerobe Bacillus" and
        self.fast_option.get()=="None" and 
        self.gram_option.get()=="--" and
        self.shape_option.get()=="bacillus" and
        self.meta_option.get()=="fac anaerobe" and
        self.endo_option.get()=="--" and
        self.cat_option.get()=="+" and
        self.oxi_option.get()=="--" and
        self.nit1_option.get()=="--" and
        self.glu_option.get()=="+"):
            bac=self.B

        if (self.group_option.get()=="Gram Negative Facultative Anaerobe Bacillus" and
        self.fast_option.get()=="None" and 
        self.gram_option.get()=="--" and
        self.shape_option.get()=="bacillus" and
        self.meta_option.get()=="fac anaerobe" and
        self.endo_option.get()=="--" and
        self.cat_option.get()=="+" and
        self.oxi_option.get()=="--" and
        self.nit1_option.get()=="+" and
        self.glu_option.get()=="+"):
            bac=self.C

        if (self.group_option.get()=="Gram Negative Facultative Anaerobe Bacillus" and
        self.fast_option.get()=="None" and 
        self.gram_option.get()=="--" and
        self.shape_option.get()=="bacillus" and
        self.meta_option.get()=="fac anaerobe" and
        self.endo_option.get()=="--" and
        self.cat_option.get()=="+" and
        self.oxi_option.get()=="+" and
        self.nit1_option.get()=="+" and
        self.glu_option.get()=="+"):
            bac=self.D

        if (self.group_option.get()=="Gram Negative Facultative Anaerobe Bacillus" and
        self.fast_option.get()=="Salt" and
        self.gram_option.get()=="--" and
        self.shape_option.get()=="bacillus" and
        self.meta_option.get()=="fac anaerobe" and
        self.endo_option.get()=="--" and
        self.cat_option.get()=="+" and
        self.oxi_option.get()=="+" and
        self.nit1_option.get()=="+" and
        self.glu_option.get()=="+"):
            bac=self.E

        if (self.group_option.get()=="Gram Negative Facultative Anaerobe Bacillus" and
        self.fast_option.get()=="Blood"):
            nothing

            
        if (self.group_option.get()=="Gram Negative Facultative Anaerobe Bacillus" and
        self.fast_option.get()=="Yeast" and
        self.gram_option.get()=="--" and
        self.shape_option.get()=="bacillus" and
        self.meta_option.get()=="fac anaerobe" and
        self.endo_option.get()=="--" and
        self.cat_option.get()=="+" and
        self.oxi_option.get()=="--" and
        self.glu_option.get()=="+"):
            nothing

        if (self.group_option.get()=="Gram Negative Aerobe Bacillus" and
        self.fast_option.get()=="None"):
            nothing
        if (self.group_option.get()=="Gram Positive Facultative Anaerobe Bacillus" and
        self.fast_option.get()=="None"):
            nothing
        if (self.group_option.get()=="Gram Positive Aerobe Bacillus" and
        self.fast_option.get()=="None"):
            nothing
        if (self.group_option.get()=="Gram Positive Facultative Anaerobe Coccus" and
        self.fast_option.get()=="None"):
            nothing            
        if (self.group_option.get()=="Gram Positive Aerobe Coccus" and
        self.fast_option.get()=="None"):
            nothing
        if (self.group_option.get()=="Spore Forming Bacillus and Coccus" and
        self.fast_option.get()=="None" and
        self.gram_option.get()=="+" and
        self.shape_option.get()=="bacillus" and
        self.cat_option.get()=="+"):
            bac=self.Z

        def plus(matrix, i):
            return [row[i] for row in matrix]
                    
        def minus(matrix, i):
            return [1.00-row[i] for row in matrix]

        bact=zip(*bac)
        bact2=bact[0:3]
        bact3=bact[0:3]
            
        if self.cat_option.get()=="+":
            bact2.append(plus(bac,3))
            bact3.append(plus(bac,3))
        if self.cat_option.get()=="--":
            bact2.append(minus(bac,3))
            bact3.append(plus(bac,3))

        if self.oxi_option.get()=="+":
            bact2.append(plus(bac,4))
            bact3.append(plus(bac,4))
        if self.oxi_option.get()=="--":
            bact2.append(minus(bac,4))
            bact3.append(plus(bac,4))

        if self.motil_option.get()=="+":
            bact2.append(plus(bac,5))
            bact3.append(plus(bac,5))
        if self.motil_option.get()=="--":
            bact2.append(minus(bac,5))
            bact3.append(plus(bac,5))

        if self.h2s_option.get()=="+":
            bact2.append(plus(bac,6))
            bact3.append(plus(bac,6))
        if self.h2s_option.get()=="--":
            bact2.append(minus(bac,6))
            bact3.append(plus(bac,6))

        if self.ind_option.get()=="+":
            bact2.append(plus(bac,7))
            bact3.append(plus(bac,7))
        if self.ind_option.get()=="--":
            bact2.append(minus(bac,7))
            bact3.append(plus(bac,7))

        if self.cit_option.get()=="+":
            bact2.append(plus(bac,8))
            bact3.append(plus(bac,8))
        if self.cit_option.get()=="--":
            bact2.append(minus(bac,8))
            bact3.append(plus(bac,8))

        if self.nit1_option.get()=="+":
            bact2.append(plus(bac,9))
            bact3.append(plus(bac,9))
        if self.nit1_option.get()=="--":
            bact2.append(minus(bac,9))
            bact3.append(plus(bac,9))

        if self.nit2_option.get()=="+":
            bact2.append(plus(bac,10))
            bact3.append(plus(bac,10))
        if self.nit2_option.get()=="--":
            bact2.append(minus(bac,10))
            bact3.append(plus(bac,10))

        if self.nit3_option.get()=="+":
            bact2.append(plus(bac,11))
            bact3.append(plus(bac,11))
        if self.nit3_option.get()=="--":
            bact2.append(minus(bac,11))
            bact3.append(plus(bac,11))

        if self.glux_option.get()=="+":
            bact2.append(plus(bac,12))
            bact3.append(plus(bac,12))
        if self.glux_option.get()=="--":
            bact2.append(minus(bac,12))
            bact3.append(plus(bac,12))

        if self.glu_option.get()=="+":
            bact2.append(plus(bac,13))
            bact3.append(plus(bac,13))
        if self.glu_option.get()=="--":
            bact2.append(minus(bac,13))
            bact3.append(plus(bac,13))

        if self.glug_option.get()=="+":
            bact2.append(plus(bac,14))
            bact3.append(plus(bac,14))
        if self.glug_option.get()=="--":
            bact2.append(minus(bac,14))
            bact3.append(plus(bac,14))

        if self.adon_option.get()=="+":
            bact2.append(plus(bac,15))
            bact3.append(plus(bac,15))
        if self.adon_option.get()=="--":
            bact2.append(minus(bac,15))
            bact3.append(plus(bac,15))

        if self.arab_option.get()=="+":
            bact2.append(plus(bac,16))
            bact3.append(plus(bac,16))
        if self.arab_option.get()=="--":
            bact2.append(minus(bac,16))
            bact3.append(plus(bac,16))

        if self.cell_option.get()=="+":
            bact2.append(plus(bac,17))
            bact3.append(plus(bac,17))
        if self.cell_option.get()=="--":
            bact2.append(minus(bac,17))
            bact3.append(plus(bac,17))

        if self.dul_option.get()=="+":
            bact2.append(plus(bac,18))
            bact3.append(plus(bac,18))
        if self.dul_option.get()=="--":
            bact2.append(minus(bac,18))
            bact3.append(plus(bac,18))

        if self.ethan_option.get()=="+":
            bact2.append(plus(bac,19))
            bact3.append(plus(bac,19))
        if self.ethan_option.get()=="--":
            bact2.append(minus(bac,19))
            bact3.append(plus(bac,19))

        if self.fru_option.get()=="+":
            bact2.append(plus(bac,20))
            bact3.append(plus(bac,20))
        if self.fru_option.get()=="--":
            bact2.append(minus(bac,20))
            bact3.append(plus(bac,20))

        if self.galac_option.get()=="+":
            bact2.append(plus(bac,21))
            bact3.append(plus(bac,21))
        if self.galac_option.get()=="--":
            bact2.append(minus(bac,21))
            bact3.append(plus(bac,21))

        if self.glyc_option.get()=="+":
            bact2.append(plus(bac,22))
            bact3.append(plus(bac,22))
        if self.glyc_option.get()=="--":
            bact2.append(minus(bac,22))
            bact3.append(plus(bac,22))

        if self.ino_option.get()=="+":
            bact2.append(plus(bac,23))
            bact3.append(plus(bac,23))
        if self.ino_option.get()=="--":
            bact2.append(minus(bac,23))
            bact3.append(plus(bac,23))

        if self.lac_option.get()=="+":
            bact2.append(plus(bac,24))
            bact3.append(plus(bac,24))
        if self.lac_option.get()=="--":
            bact2.append(minus(bac,24))
            bact3.append(plus(bac,24))

        if self.mal_option.get()=="+":
            bact2.append(plus(bac,25))
            bact3.append(plus(bac,25))
        if self.mal_option.get()=="--":
            bact2.append(minus(bac,25))
            bact3.append(plus(bac,25))

        if self.man_option.get()=="+":
            bact2.append(plus(bac,26))
            bact3.append(plus(bac,26))
        if self.man_option.get()=="--":
            bact2.append(minus(bac,26))
            bact3.append(plus(bac,26))

        if self.mann_option.get()=="+":
            bact2.append(plus(bac,27))
            bact3.append(plus(bac,27))
        if self.mann_option.get()=="--":
            bact2.append(minus(bac,27))
            bact3.append(plus(bac,27))

        if self.meli_option.get()=="+":
            bact2.append(plus(bac,28))
            bact3.append(plus(bac,28))
        if self.meli_option.get()=="--":
            bact2.append(minus(bac,28))
            bact3.append(plus(bac,28))

        if self.raf_option.get()=="+":
            bact2.append(plus(bac,29))
            bact3.append(plus(bac,29))
        if self.raf_option.get()=="--":
            bact2.append(minus(bac,29))
            bact3.append(plus(bac,29))

        if self.rham_option.get()=="+":
            bact2.append(plus(bac,30))
            bact3.append(plus(bac,30))
        if self.rham_option.get()=="--":
            bact2.append(minus(bac,30))
            bact3.append(plus(bac,30))

        if self.sal_option.get()=="+":
            bact2.append(plus(bac,31))
            bact3.append(plus(bac,31))
        if self.sal_option.get()=="--":
            bact2.append(minus(bac,31))
            bact3.append(plus(bac,31))

        if self.sorb_option.get()=="+":
            bact2.append(plus(bac,32))
            bact3.append(plus(bac,32))
        if self.sorb_option.get()=="--":
            bact2.append(minus(bac,32))
            bact3.append(plus(bac,32))

        if self.suc_option.get()=="+":
            bact2.append(plus(bac,33))
            bact3.append(plus(bac,33))
        if self.suc_option.get()=="--":
            bact2.append(minus(bac,33))
            bact3.append(plus(bac,33))

        if self.tre_option.get()=="+":
            bact2.append(plus(bac,34))
            bact3.append(plus(bac,34))
        if self.tre_option.get()=="--":
            bact2.append(minus(bac,34))
            bact3.append(plus(bac,34))

        if self.xyl_option.get()=="+":
            bact2.append(plus(bac,35))
            bact3.append(plus(bac,35))
        if self.xyl_option.get()=="--":
            bact2.append(minus(bac,35))
            bact3.append(plus(bac,35))

        if self.arg_option.get()=="+":
            bact2.append(plus(bac,36))
            bact3.append(plus(bac,36))
        if self.arg_option.get()=="--":
            bact2.append(minus(bac,36))
            bact3.append(plus(bac,36))

        if self.lys_option.get()=="+":
            bact2.append(plus(bac,37))
            bact3.append(plus(bac,37))
        if self.lys_option.get()=="--":
            bact2.append(minus(bac,37))
            bact3.append(plus(bac,37))

        if self.orn_option.get()=="+":
            bact2.append(plus(bac,38))
            bact3.append(plus(bac,38))
        if self.orn_option.get()=="--":
            bact2.append(minus(bac,38))
            bact3.append(plus(bac,38))

        if self.phen_option.get()=="+":
            bact2.append(plus(bac,39))
            bact3.append(plus(bac,39))
        if self.phen_option.get()=="--":
            bact2.append(minus(bac,39))
            bact3.append(plus(bac,39))

        if self.trypto_option.get()=="+":
            bact2.append(plus(bac,40))
            bact3.append(plus(bac,40))
        if self.trypto_option.get()=="--":
            bact2.append(minus(bac,40))
            bact3.append(plus(bac,40))

        if self.amp_option.get()=="+":
            bact2.append(plus(bac,41))
            bact3.append(plus(bac,41))
        if self.amp_option.get()=="--":
            bact2.append(minus(bac,41))
            bact3.append(plus(bac,41))

        if self.ceph_option.get()=="+":
            bact2.append(plus(bac,42))
            bact3.append(plus(bac,42))
        if self.ceph_option.get()=="--":
            bact2.append(minus(bac,42))
            bact3.append(plus(bac,42))

        if self.chlor_option.get()=="+":
            bact2.append(plus(bac,43))
            bact3.append(plus(bac,43))
        if self.chlor_option.get()=="--":
            bact2.append(minus(bac,43))
            bact3.append(plus(bac,43))

        if self.nal_option.get()=="+":
            bact2.append(plus(bac,44))
            bact3.append(plus(bac,44))
        if self.nal_option.get()=="--":
            bact2.append(minus(bac,44))
            bact3.append(plus(bac,44))

        if self.poly_option.get()=="+":
            bact2.append(plus(bac,45))
            bact3.append(plus(bac,45))
        if self.poly_option.get()=="--":
            bact2.append(minus(bac,45))
            bact3.append(plus(bac,45))

        if self.strep_option.get()=="+":
            bact2.append(plus(bac,46))
            bact3.append(plus(bac,46))
        if self.strep_option.get()=="--":
            bact2.append(minus(bac,46))
            bact3.append(plus(bac,46))

        if self.amy_option.get()=="+":
            bact2.append(plus(bac,47))
            bact3.append(plus(bac,47))
        if self.amy_option.get()=="--":
            bact2.append(minus(bac,47))
            bact3.append(plus(bac,47))

        if self.amyg_option.get()=="+":
            bact2.append(plus(bac,48))
            bact3.append(plus(bac,48))
        if self.amyg_option.get()=="--":
            bact2.append(minus(bac,48))
            bact3.append(plus(bac,48))
            
        if self.cas_option.get()=="+":
            bact2.append(plus(bac,49))
            bact3.append(plus(bac,49))
        if self.cas_option.get()=="--":
            bact2.append(minus(bac,49))
            bact3.append(plus(bac,49))

        if self.chi_option.get()=="+":
            bact2.append(plus(bac,50))
            bact3.append(plus(bac,50))
        if self.chi_option.get()=="--":
            bact2.append(minus(bac,50))
            bact3.append(plus(bac,50))

        if self.esc_option.get()=="+":
            bact2.append(plus(bac,51))
            bact3.append(plus(bac,51))
        if self.esc_option.get()=="--":
            bact2.append(minus(bac,51))
            bact3.append(plus(bac,51))

        if self.gel_option.get()=="+":
            bact2.append(plus(bac,52))
            bact3.append(plus(bac,52))
        if self.gel_option.get()=="--":
            bact2.append(minus(bac,52))
            bact3.append(plus(bac,52))

        if self.hip_option.get()=="+":
            bact2.append(plus(bac,53))
            bact3.append(plus(bac,53))
        if self.hip_option.get()=="--":
            bact2.append(minus(bac,53))
            bact3.append(plus(bac,53))

        if self.starch_option.get()=="+":
            bact2.append(plus(bac,54))
            bact3.append(plus(bac,54))
        if self.starch_option.get()=="--":
            bact2.append(minus(bac,54))
            bact3.append(plus(bac,54))

        if self.tw20_option.get()=="+":
            bact2.append(plus(bac,55))
            bact3.append(plus(bac,55))
        if self.tw20_option.get()=="--":
            bact2.append(minus(bac,55))
            bact3.append(plus(bac,55))

        if self.tw80_option.get()=="+":
            bact2.append(plus(bac,56))
            bact3.append(plus(bac,56))
        if self.tw80_option.get()=="--":
            bact2.append(minus(bac,56))
            bact3.append(plus(bac,56))

        if self.tyro_option.get()=="+":
            bact2.append(plus(bac,57))
            bact3.append(plus(bac,57))
        if self.tyro_option.get()=="--":
            bact2.append(minus(bac,57))
            bact3.append(plus(bac,57))

        if self.urea_option.get()=="+":
            bact2.append(plus(bac,58))
            bact3.append(plus(bac,58))
        if self.urea_option.get()=="--":
            bact2.append(minus(bac,58))
            bact3.append(plus(bac,58))

        if self.endo_b_option.get()=="+":
            bact2.append(plus(bac,59))
            bact3.append(plus(bac,59))
        if self.endo_b_option.get()=="--":
            bact2.append(minus(bac,59))
            bact3.append(plus(bac,59))

        if self.endo_c_option.get()=="+":
            bact2.append(plus(bac,60))
            bact3.append(plus(bac,60))
        if self.endo_c_option.get()=="--":
            bact2.append(minus(bac,60))
            bact3.append(plus(bac,60))

        if self.endo_o_option.get()=="+":
            bact2.append(plus(bac,61))
            bact3.append(plus(bac,61))
        if self.endo_o_option.get()=="--":
            bact2.append(minus(bac,61))
            bact3.append(plus(bac,61))

        if self.coag_option.get()=="+":
            bact2.append(plus(bac,62))
            bact3.append(plus(bac,62))
        if self.coag_option.get()=="--":
            bact2.append(minus(bac,62))
            bact3.append(plus(bac,62))

        if self.dna_option.get()=="+":
            bact2.append(plus(bac,63))
            bact3.append(plus(bac,63))
        if self.dna_option.get()=="--":
            bact2.append(minus(bac,63))
            bact3.append(plus(bac,63))

        if self.phos_option.get()=="+":
            bact2.append(plus(bac,64))
            bact3.append(plus(bac,64))
        if self.phos_option.get()=="--":
            bact2.append(minus(bac,64))
            bact3.append(plus(bac,64))

        if self.hem_option.get()=="+":
            bact2.append(plus(bac,65))
            bact3.append(plus(bac,65))
        if self.hem_option.get()=="--":
            bact2.append(minus(bac,65))
            bact3.append(plus(bac,65))

        if self.onpg_option.get()=="+":
            bact2.append(plus(bac,66))
            bact3.append(plus(bac,66))
        if self.onpg_option.get()=="--":
            bact2.append(minus(bac,66))
            bact3.append(plus(bac,66))

        if self.vp_option.get()=="+":
            bact2.append(plus(bac,67))
            bact3.append(plus(bac,67))
        if self.vp_option.get()=="--":
            bact2.append(minus(bac,67))
            bact3.append(plus(bac,67))

        bac2=zip(*bact2)
        bac3=zip(*bact3)

        bac4={}

        if self.algo_option.get()=="Geometric Mean":
            bac4 = [(item[0], "%.2f"% (item[2]()*reduce(mul,item[3:])**(1.0/len(item[1:])))) for item in bac2]
            
        if self.algo_option.get()=="Bayes Theorem":
            sigma = float(sum(reduce(mul,item[3:]) for item in bac2))
            bac4 = [(item[0], "%.2f" % (item[2]()*reduce(mul, item[3:])/sigma)) for item in bac2]
            
        if self.algo_option.get()=="Phi Coefficient":
            Label(self.id_frame, text = "Unwritten Code", background = "white").pack(side=TOP, anchor = W)

        bac5 = sorted(bac4, key=lambda item: item[1], reverse=True)
        
        Label(self.id_frame, text = bac5[0], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = bac5[1], background = "white").pack(side=TOP, anchor = W)
        Label(self.id_frame, text = bac5[2], background = "white").pack(side=TOP, anchor = W)
        
bacteria = Bacteria(root)       
root.mainloop()
