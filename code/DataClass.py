
import spacy
from spacy.lang.fr import French
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher
import nltk
import pandas as pd
import xlsxwriter 
import numpy as np
from thefuzz import fuzz, process


nlp = spacy.load("fr_core_news_sm")

class Data :

    def ClassData_Ipro(text,sheet): 
        
        datast= [Line for Line in text if "gratuit" not in Line]
        Hotelname= datast[0]
        for line in datast :    
            if 'dzd' in line : 
                Hotelprix = line
            #elif 'en ' in line :
                #Arangement = line
        add_row = np.array([[Hotelname, Hotelprix]])
        sheet=np.append(sheet, add_row, axis=0)

        return sheet

    def ClassData_Mygo(text,wilaya,sheet):
        datast= [Line for Line in text if ", {}".format(str(wilaya)) and "offre spéciale!" not in Line]
        Hotelname= datast[0]
        for line in datast :    
            if 'dzd' in line : 
                Hotelprix = line
        add_row = np.array([[Hotelname, Hotelprix]])
        sheet=np.append(sheet, add_row, axis=0)
        return sheet

    def ClassData_clic(sheet,priceslist,hotellist): 
        
        add_row = np.array([hotellist, priceslist])
        sheet=np.append(sheet, add_row)
        return sheet



    def ClassData_comparison(sheet,joined_list):

        add_row = np.array([joined_list])
        sheet=np.append(sheet, add_row, axis=0)
        return sheet
        





        

