from google.colab import drive
drive.mount('/content/drive')

import matplotlib.pyplot as plt #matplotlib(python visualization package or library) pyplot is python module in matplotlib 
import matplotlib as mpl #matplotlib package
import matplotlib.animation as animation #animation module from mpl package
import matplotlib.axis as axs #axis module from mpl package
import pandas as pd #pandas package of python
import numpy as np #python's package for scientific computing
import seaborn as sns

path='/content/drive/MyDrive/Capstone/Hotel Bookings.csv'

hotel_booking_df=pd.read_csv(path)

#Data Exploration and Data Cleaning

#show upper rows
hotel_booking_df.head()

#Show bottom rows
hotel_booking_df.tail()

hotel_booking_df.info()

hotel_booking_df[hotel_booking_df.duplicated()]

hotel_booking_df.isnull().sum().sort_values(ascending=False)

# converting object type to datetime
hotel_booking_df['reservation_status_date'] = pd.to_datetime(hotel_booking_df['reservation_status_date'], format = '%Y-%m-%d')
