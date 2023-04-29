#imports

import shutil
import os
import datetime

#automated files backup script -> (cron or task scheduler)
#todo : - for each backup create new folder in backup_location with named with current date 
#       - delete backup > 7 days
#       - check if the content of folder_to_save is the same as the folder in backup_location

##########################################
##########################################
#######   VARIABLE TO MODIFY  ############
##########################################
##########################################

folder_to_save = "/home/ryuk/Documents/backuptest"
backup_location = "/home/ryuk/Documents/savetest"

#saving method
def save(fts, bl):
    date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    new_backup_folder = bl + "/backup_" + date_time
    # print(new_backup_folder)
    os.mkdir(new_backup_folder)
    for file_or_folder in os.listdir(fts):
        #combine file name and path 
        #if we don't combine, shutil.copy wont be able to find the file/folder for copying  
        file_or_forlder_name = os.path.join(fts, file_or_folder)
        if os.path.isdir(file_or_forlder_name):    
            shutil.copytree(file_or_forlder_name, os.path.join(new_backup_folder, file_or_folder))
        else:
            shutil.copy(file_or_forlder_name, new_backup_folder)

#run save
save(folder_to_save, backup_location)
