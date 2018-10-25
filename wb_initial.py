# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 13:25:13 2018

@author: shres
"""
import wbdata
import pandas as pd
import datetime

iEcon = {'EF.EFM.RANK.XD':'Economic Fitness Ranking', 'DP.DOD.DECT.CR.CG.Z1':'Gross Central Government Debt','NE.EXP.GNFS.ZS':'Exports of Goods and Services', 'GC.XPN.TOTL.GD.ZS': 'Expense', '6.0.GDP_current': 'GDP', '6.0.GDPpc_constant': 'GDP per capita', '5.51.01.10.gdp': 'GDP per capita growth', '6.0.GNIpc': 'GNI per capita', 'NE.IMP.GNFS.ZS': 'Imports', 'BX.TRF.PWKR.GD.ZS': 'Workers Remittance'}#,'BX.TRF.PWKR.DT.GD.ZS':'Personal remittance' } 
cUndeveloped = ['NPL', 'RWA', 'BGD', 'HTI'] # Nepal, Rwanda, Bangladesh, Haiti 
cDeveloping = ['CHN', 'IND', 'BRA', 'NGA'] # China, India, Brazil, Nigeria
cDeveloped = ['USA', 'DEU', 'LUX', 'JPN'] # USA, Germany, Luxembourg, Japan
cAll = ['NPL', 'RWA', 'BGD', 'HTI','CHN', 'IND', 'BRA', 'NGA','USA', 'DEU', 'LUX', 'JPN']
date_range = (datetime.datetime(1995, 1, 1), datetime.datetime(2017, 1, 1))
years = [str(i) for i in range(1995,2018)]

df_Econ = wbdata.get_dataframe(iEcon, country=cAll, data_date = date_range,  convert_date=False) #getting the required indicators
dfu_Econ = df_Econ.unstack(level=0) #Unstacking the columns by countries
dfu_Econ = dfu_Econ[dfu_Econ.index.isin(years)] #Removing the quarterly data and get just the required years