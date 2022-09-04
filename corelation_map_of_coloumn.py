import matplotlib.pyplot as plt #matplotlib(python visualization package or library) pyplot is python module in matplotlib 
import matplotlib as mpl #matplotlib package
import matplotlib.animation as animation #animation module from mpl package
import matplotlib.axis as axs #axis module from mpl package
import pandas as pd #pandas package of python
import numpy as np #python's package for scientific computing
import seaborn as sns #statistical graph plotting package of python


#making DataFrame hotel_booking_df by using .read_csv() method of pandas
hotel_booking_df=pd.read_csv(r'https://drive.google.com/uc?id=d/1wuF1pJKO4pleroRKXygX9ekp8YWOj53M')

#setting figure size
plt.figure(figsize=(18,10))

#making heatmap using .heatmap() of seaborn package of python
sns.heatmap(hotel_booking_df.corr(),annot=True)
#setting title of figure
plt.title('Co-relation of the columns')
