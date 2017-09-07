
# copies an entire folder and its contents into a zip file whose filename increments


import zipfile, os
def backupToZip(folder):
    #back up the entire contents of folder into into a zip
    folder = os.path.abspath(folder) # make sure folder is absolute

    number = 1
    while True:
        zipFilename = os.path.basename(folder) +'_'+str(number)+".zip"
        if not os.path.exists(zipFilename):
            break
        number+=1

    # create a zip file
    print ('creating %s...'% (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # compress the files on each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('adding files in %s...'%(foldername))
        backupZip.write(foldername)
        for filename in Filenames:
            newBase = os.path.base(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
    print("Done")
    
