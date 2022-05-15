rows = ['id', 'self.gram_option', 'self.shape_option', 'self.meta_option', 'self.cat_option', 
        'self.oxi_option', 'self.endo_option', 'self.motil_option', 'self.h2s_option', 'self.ind_option', 
        'self.cit_option', 'self.nit_option', 'self.urea_option', 'self.glu_option', 'self.arab_option', 
        'self.glyc_option', 'self.lac_option', 'self.man_option', 'self.raf_option', 'self.sal_option', 
        'self.sorb_option', 'self.suc_option', 'self.xyl_option', 'self.salt_option', 'self.temp_option']
 
        if (self.gram_option.get()==("--") and
            self.shape_option.get()==("bacillus") and
            self.meta_option.get()==("fac anaerobe")):
                f = open('home/turtleman/Documents/Python/neg_fac_bac.csv', "r")


# Also, some genera may appear in more than one Mega-Group--will this cause hiccups?

        id = "Gram Negative Aerobic Bacillus"
        and 
        genus = Acetobacter or Deinobacter or Flavimonas
        if
        gram_option = "-" and shape_option = "bacillus" and meta_option = "aerobe" and 
        cat_option = "+" and oxi_option = "-" and endo_option = "-"


        id = "Gram Negative Aerobic Bacillus"
        and
        genus = Acidovorax or Argobacterium or Argomonas or Alcaligenes or 
        Azomonas or Azobacter or Comamonas or Cupriavidis or Ensifer or 
        Flavobacterium or Hydrogenophila or Pseudomonas or Rhizobacter or
        Roseomonas or Serpens or Shingobacterium or Variovorax or Zoogloea
        if 
        gram_option = "-" and shape_option = "bacillus" and meta_option = "aerobe" and 
        cat_option = "+" and oxi_option = "+" and endo_option = "-"


        id = "Gram Negative \n Facultative Anaerobic Bacillus" 
        and
        genus = Budvicia or Buttiauxella or Citrobacter or Edwardsiella
        or Enterobacter or Escheria or Hafnia or Klebsiella or Kluyvera or
        Lecleria or Leminorella or Moellerella or Morganella or Pantoea
        or Pragia or Proteus or Salmonella or Serratia or Shigella or Yersinia 
        if
        gram_option = "-" and shape_option = "bacillus" and meta_option = "fac anaerobe" and 
        cat_option = "+" and oxi_option = "-" and endo_option = "-"


        id = "Gram Negative \n Facultative Anaerobic Bacillus"
        and
        genus = Aeromonas or Plesiomonas or Vibrio or Chromobacterium
        if 
        gram_option = "-" and shape_option = "bacillus" and meta_option = "fac anaerobe" and 
        cat_option = "+" and oxi_option = "+" and endo_option = "-"


        id = "Gram Positive \n Facultative Anaerobic Coccus"
        and 
        genus = Enterococcus or Lactococcus or Leuconostoc or Pedicoccus or Vagococcus
        if 
        gram_option = "+" and shape_option = "coccus" and meta_option = "fac anaerobe" and 
        cat_option = "-" and oxi_option = "-" and endo_option = "-"


        id = "Gram Positive \n Facultative Anaerobic Coccus"
        and
        genus = Trichoccus
        if 
        gram_option = "+" and shape_option = "coccus" and meta_option = "fac anaerobe" and 
        cat_option = "+" and oxi_option = "-" and endo_option = "-"


        id = "Gram Positive Aerobic Coccus"
        and
        genus = Dermabacter or Planococcus
        if 
        gram_option = "+" and shape_option = "coccus" and meta_option = "aerobe" and 
        cat_option = "+" and oxi_option = "-" and endo_option = "-"


        id = "Gram Positive Aerobic Coccus"
        and
        genus = Deinococcus or Micrococcus
        if 
        gram_option = "+" and shape_option = "coccus" and meta_option = "aerobe" and 
        cat_option = "+" and oxi_option = "+" and endo_option = "-"


        id = "Gram Positive Aerobic \n Endospore-Forming Coccus"
        and
        genus = Sporosarcina
        if 
        gram_option = "+" and shape_option = "coccus" and meta_option = "aerobe" and 
        cat_option = "+" and oxi_option = "+" and endo_option = "+"






        for line in f.readlines():
            line(1) = id,
            line(2) == self.cat_option(),
            line(3) == self.oxi_option(),
            line(4) == self.endo_option(),
            line(5) == self.motil_option(),
            line(6) == self.h2s_option(),
            line(7) == self.ind_option(),
            line(8) == self.cit_option(),
            line(9) == self.nit_option(),
            line(10) == self.urea_option(),
            line(11) == self.glu_option(),
            line(12) == self.arab_option(),
            line(13) == self.glyc_option(),
            line(14) == self.lac_option(),
            line(15) == self.man_option(),
            line(16) == self.raf_option(),
            line(17) == self.sal_option(),
            line(18) == self.sorb_option(),
            line(19) == self.suc_option(),
            line(20) == self.xyl_option(),
            line(21) == self.salt_option(),
            line(22) == self.temp_option()