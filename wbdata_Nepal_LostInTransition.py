# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 19:36:29 2018

@author: shres
"""

import wbdata
import pandas as pd
import datetime
import matplotlib.pyplot as plt

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
         'NY.GDP.MKTP.KD.ZG':'GDP_growth_annual',\
		   #'SP.RUR.TOTL.ZS':'percent_rural_pop',\
         'SP.POP.GROW':'pop_growth','GC.DOD.TOTL.GD.ZS':'central_gov_debt', \
         'NE.EXP.GNFS.ZS':'exports', 'GC.XPN.TOTL.GD.ZS': 'expense' , 'NE.IMP.GNFS.ZS': 'imports', \
         'BX.TRF.PWKR.DT.GD.ZS':'remittance' } 

#Setting the date for which we want to look at the data
date_range = (datetime.datetime(1970, 1, 1), datetime.datetime(2017, 1, 1))

#Dictionary Describing timeline of Nepal history
dict_timeline = {#'1951': 'Rana', '1952':'Tribhuvan', \
					  #'1955':'Mahendra', '1959':'Constitution',\
					  #'1960': 'MahendraCoup', '1962':'Panchayat',\
					  '1972': 'Birendra','1991':'NCP_Democracy', '1994':'Communist', \
					  '1995':'Civil_War', \
					  '2001':'Gyanendra', '2007': 'Civil_War_trans',\
					  '2009':'Prachhanda',\
					  '2010':'Transition'}
					 

#Getting the dataframe from wbdata with chosen indicators
df = wbdata.get_dataframe(iEcon, country='NPL', data_date = date_range,  convert_date=True) #getting the required indicators
df = df.sort_index()

#Plotting the data
df_plot = df
df_plot.index = df_plot.index.year.astype(int)
plt.plot(df_plot)
plt.legend(df.columns)
i = 1
for d in dict_timeline:
	plt.axvline(int(d))
	if i%2==0:
		plt.text(int(d)+0.25, 60, dict_timeline[d], rotation=60)
	else:
		plt.text(int(d)+0.25, 70, dict_timeline[d],rotation=60)
	i += 1
plt.title('World Bank Indicators at different political stages of Nepal')
plt.text(1972.5,-5,'*Everything except population and GDP growth is measured in % of GDP')
plt.show()
