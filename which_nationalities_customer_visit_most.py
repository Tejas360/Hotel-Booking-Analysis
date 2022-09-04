import matplotlib.pyplot as plt #matplotlib(python visualization package or library) pyplot is python module in matplotlib 
import matplotlib as mpl #matplotlib package
import matplotlib.animation as animation #animation module from mpl package
import matplotlib.axis as axs #axis module from mpl package
import pandas as pd #pandas package of python
import numpy as np #python's package for scientific computing
import seaborn as sns #statistical graph plotting package of python

#Creation of DataFrame
hotel_booking_df=pd.read_csv(r'https://drive.google.com/uc?id=d/1wuF1pJKO4pleroRKXygX9ekp8YWOj53M')

#using pandas group by method I made the country wise grouped multiindex series

country_wise=hotel_booking_df.groupby(["hotel","country"])["country"].count()

#we need two barh garphs ,one graph for different nationalities customer visiting City hotel and other for Resort hotel
#that's why we need two seperate figures and two seperate axes 
fig3,ax3=plt.subplots()
fig4,ax4=plt.subplots()



#sorting values by default ascending order
new_df1=country_wise["City Hotel"].sort_values()

#selecting top 5 most visiting nationalities
gra1=new_df1.tail(5)

#using horizontal bar graph we plot nationalities vs count
ax3.barh(gra1.index,gra1.values)
#labels of respective axis
ax3.yaxis.set_label_text("Nationalities")
ax3.xaxis.set_label_text("Number of Customers of City Hotel")

#same with resort hotel now 
#sorting values by default ascending order
new_df2=country_wise["Resort Hotel"].sort_values()

#selecting top 5 most visiting nationalities
gra2=new_df2.tail(5)

#using horizontal bar graph we plot nationalities vs count
ax4.barh(gra2.index,gra2.values)
#labels of respective axis
ax4.yaxis.set_label_text("Nationalities")
ax4.xaxis.set_label_text("Number of Customers of Resort Hotel")
fig3.text(0.5,0.5,"portugal")

#using show function of matplotlib's figure object 
fig3.show()
fig4.show()

