# renames filenames with American MM-DD-YYYY date
#format to European DD-MM-YY
import shutil, os, re

renameDates():

    # create a regex that matches files with the American date format
    datePattern = re.compile(r"""^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$""", re.VERBOSE)
    # loop over the files in the working directory
    for amerFilename in os.listdir('.'):
        mo=datePattern.search(amerFilename)
    #skip names without date
        if mo==None:
            continue
        # get the differnt parts of the filename
        beforePart = mo.group(1)
        monthPart= mo.group(2)
        dayPart= mo.group(4)
        yearPart=mo.group(6)
        afterPart=mo.group(8)

        # form the european -style filename
        euroFilename= beforePart+dayPart+'-'+monthPart+"-"+yearPart+afterPart

        #get the full, absolute file paths
        absWorkingDir= os.path.abspath('.')
        amerFilename = os.path.join(absWorkingDir, amerFilename)
        euroFilename = os.path.join(absWorkingDir, euroFilename)

        # rename the files
        print('renaming "%" to "%s"...'%(amerFilename, euroFilename))
        shutil.move(amerFilename, euroFilename)
    
    

