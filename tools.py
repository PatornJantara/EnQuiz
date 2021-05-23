# this is used to group a question to its folder

import os
import shutil

this_path = os.getcwd()
old_path = this_path +'\\'+'pic'+'\\'  
des_path = this_path +'\\'+'pic2'+'\\' 

special = []
trigger = 1
folder  = 201 # folder question start at 
for file in os.listdir(old_path):
    
    if trigger == 1 :

        shutil.move(old_path+file, des_path+ '\\'+str(folder)+'\\' + 'q.png')
        trigger += 1

    elif trigger == 2 :

        shutil.move(old_path+file, des_path+ '\\'+str(folder)+'\\' + '1.png')
        trigger += 1

    elif trigger == 3 :

        shutil.move(old_path+file, des_path+ '\\'+str(folder)+'\\' + '2.png')
        trigger += 1

    elif trigger == 4 :

        shutil.move(old_path+file, des_path+ '\\'+str(folder)+'\\' + '3.png')
        trigger += 1

    elif trigger == 5 :

        shutil.move(old_path+file, des_path+ '\\'+str(folder)+'\\' + '4.png')

        if folder in special :

            trigger += 1

        else:

            trigger = 1
            folder += 1
    
    elif trigger == 6  :
            shutil.move(old_path+file, des_path+ '\\'+str(folder)+'\\' + '5.png')
            trigger = 1
            folder += 1


    
