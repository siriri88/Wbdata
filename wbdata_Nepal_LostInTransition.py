# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 19:36:29 2018

@author: shres
"""

import wbdata
import pandas as pd
import datetime

#Dictionary that describes the indicators used in analysis
iEcon_Descriptive = {'EF.EFM.RANK.XD':'Economic Fitness Ranking (1 = high, 149 = low)[EFR]',\
                     'NY.GDP.MKTP.CD':'GDP (current US$)',\
                     'NY.GDP.MKTP.KD.ZG':'GDP Growth (annual%)', \
                     'SP.RUR.TOTL.ZS':'Percent Rural Population',\
                     'SP.POP.GROW':'Population growth (annual %)',\
                     'GC.DOD.TOTL.GD.ZS':'Central government debt, total (% of GDP)', \
                     'NE.EXP.GNFS.ZS':'Exports of goods and services (% of GDP)',\
                     'GC.XPN.TOTL.GD.ZS': 'Expense (% of GDP)' , \
                     'NE.IMP.GNFS.ZS': 'Imports of goods and services (% of GDP)',\
                     'BX.TRF.PWKR.DT.GD.ZS':'Personal remittance, paid (current US$)' } 

#Dictionary used to choose the indicators and the column names of the subsequent dataframe without GDP
iEcon = {#'EF.EFM.RANK.XD':'EFR', 'NY.GDP.MKTP.CD':'GDP',\
         'NY.GDP.MKTP.KD.ZG':'GDP_growth_annual', 'SP.RUR.TOTL.ZS':'percent_rural_pop',\
         'SP.POP.GROW':'pop_growth','GC.DOD.TOTL.GD.ZS':'central_gov_debt', \
         'NE.EXP.GNFS.ZS':'exports', 'GC.XPN.TOTL.GD.ZS': 'expense' , 'NE.IMP.GNFS.ZS': 'imports', \
         'BX.TRF.PWKR.DT.GD.ZS':'remittance' } 

#Setting the date for which we want to look at the data
date_range = (datetime.datetime(1900, 1, 1), datetime.datetime(2017, 1, 1))

#Dictionary Describing timeline of Nepal history
dict_timeline = {'before 1951': 'Rana Regime', '1952-1955':'King Tribhuvan Regime', \
					  '1955-1959':'King Mahendra Regime', '1959-1960':'Multi-party Constitution'\
					  '1960-1962': 'King Mahendra Coup', '1962-1972':'Panchayat System'\
					  '1972-1990': 'Kind Birendra', '1990':'Jana Andolan I',\
					  '1991-1994':'First NCP led Democracy', '1994-1995':'Communist party', \
					  '1995-2006':'Maoist led Civil War', '2001':'Royal Assassination',\
					  '2001-2006':'Gyanendra Regime', '2007-2008': 'Transition from civil war'\
					  '2008-2009':'Prachhanda led Federal Democratic Republic',\
					  '2009-2010': 'Madhav Kumar Nepal', '2010-2017':'Lost in transition'
					 

#Getting the dataframe from wbdata with chosen indicators
df = wbdata.get_dataframe(iEcon, country='NPL', data_date = date_range,  convert_date=True) #getting the required indicators
df = df.sort_index()