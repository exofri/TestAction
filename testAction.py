import os
import datetime


now = datetime.datetime.now()


with open('out.txt', 'a+') as file:
     
    file.writelines(str(now.year)+"/"+ str(now.month)+"/"+ str(now.day)+"   "+ str(now.hour)+":"+ str(now.minute)+":"+ str(now.second)+"\n")
