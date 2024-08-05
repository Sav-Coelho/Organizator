import os,shutil,zipfile
os.chdir('C:\\Users\whohe\Videos\ovo')
with zipfile.ZipFile(file='exemplo.zip') as zip_ref:
    for arquivo in zip_ref.namelist():
        if "DAS" in arquivo:
            zip_ref.extractall()
            zip_ref.close()
