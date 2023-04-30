#imports
import shutil
import os
import datetime

#automated files backup script -> (cron or task scheduler)
#todo : - delete backup > 7 days
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
    date_time = datetime.datetime.now().strftime("%Y-%m-%d")
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

def rm_old_backup(bl):
    for backup_folder in os.listdir(bl):
        date_backup = backup_folder.split("_")
        date_backup = date_backup[1]
        date_backup = datetime.datetime.strptime(date_backup, "%Y-%m-%d")
        date_now = datetime.datetime.now()
        date_difference = (date_now - date_backup).days
        if date_difference > 7:
            folder_to_delete = os.path.join(bl, backup_folder)
            shutil.rmtree(folder_to_delete)

#run save
save(folder_to_save, backup_location)
rm_old_backup(backup_location)
