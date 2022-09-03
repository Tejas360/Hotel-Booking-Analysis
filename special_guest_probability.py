import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
url="https://drive.google.com/file/d/1KBfKrJK_UWw8RiCFLP8MxtD6VIDrxr5G/view?usp=sharing"
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
hotel_booking_df = pd.read_csv(url)

#filter the data using filter method of pandas DataFrame Object
filter_df =hotel_booking_df.filter(items=["hotel", "total_of_special_requests"])
sort_df_by_special_request_truthy= filter_df[filter_df["total_of_special_requests"]>0]
special_request_count = sort_df_by_special_request_truthy.groupby(["hotel"])["total_of_special_requests"].count()
total_bookings_done=filter_df.groupby(["hotel"])["total_of_special_requests"].count()
special_request_probability=pd.Series(
[ special_request_count["City Hotel"]/(total_bookings_done["City Hotel"]) ,
 special_request_count["Resort Hotel"]/(total_bookings_done["Resort Hotel"])],
["City Hotel", "Resort Hotel"] )
 

fig2,plot_special_request_probability=plt.subplots()
plot_srp=plot_special_request_probability.bar(special_request_probability.index,special_request_probability.values,color=["red","blue"])







plot_special_request_probability.title.set_color("red")
plot_special_request_probability.title.set_fontsize(25)
plot_special_request_probability.set_yticks([x/10  for x in range(11)])
text_city_hotel=fig2.text(0.2,0.3,str( np.round(special_request_probability["City Hotel"]*100))+"%"   )
text_resort_hotel=fig2.text(0.6,0.2,str( np.round(special_request_probability["Resort Hotel"]*100))+"%"   )






text_city_hotel.set_fontsize(20)
text_city_hotel.set_color("white")
text_city_hotel.set_fontweight(900)

text_resort_hotel.set_fontsize(20)
text_resort_hotel.set_color("white")
text_resort_hotel.set_fontweight(900)

xaxis_label =plot_special_request_probability.xaxis.set_label_text("Hotel type")
xaxis_label.set_color("brown")
xaxis_label.set_fontsize("20")

yaxis_label =plot_special_request_probability.yaxis.set_label_text(" Probability")
yaxis_label.set_color("brown")
yaxis_label.set_fontsize("20")

fig2.set_figwidth(20)
title_p2=fig2.text(0.2,0.90,"special request probability")
title_p2.set_fontsize(20)
title_p2.set_color("blue")

credit_title_p2=fig2.text(0.5,0.90,"Analyse and visualize by Tejas Rajput(patil) from team Data digger",fontsize=10,fontweight=10,color="red",fontfamily="monospace")

project_detail_p2=fig2.text(0.2,0.98,"AlmaBetter Capstone Project year 2022",fontsize=10,fontweight=900,color="black",fontfamily="monospace")

fig2.show()


#comprehensive ANimation
incr_h=0
def incr(frame):
    global incr_h
    if incr_h> (special_request_count["City Hotel"]/(total_bookings_done["City Hotel"])):
        v2=plot_special_request_probability.properties()["children"][0].set_height( special_request_count["City Hotel"]/(total_bookings_done["City Hotel"]))
    else:
        v2=plot_special_request_probability.properties()["children"][0].set_height(incr_h)

    if incr_h> (special_request_count["Resort Hotel"]/(total_bookings_done["Resort Hotel"]) ):
        plot_special_request_probability.properties()["children"][1].set_height(special_request_count["Resort Hotel"]/(total_bookings_done["Resort Hotel"]))
    else:
      plot_special_request_probability.properties()["children"][1].set_height(incr_h)
    
    incr_h+=0.01

anim_srp=animation.FuncAnimation(fig2 ,incr,interval=100)















 



















