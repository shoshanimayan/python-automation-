#removes the header from all CS files in the current directory

import csv, os

os.makedirs('headerRemoved', exist_ok=True)
#loop through every files in the current directory
for csvFile in os.listdir('.'):
    if not csvFile.endswith('.csv'):
        continue # skip non csv file
    print( 'removing header from '+ csvFile +"...")

    # read the csv file in
    csvRows=[]
    csvFileObj = open(csvFile)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num==1:
            continue #skip first row
        csvRows.append(row)
    csvFileObj.close()

    #write out the CSV file
    csvObj= open(os.path.join('headerRemoved', csvFile), newline='')
    csvWriter = csv.writer(csvObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvObj.close()
    
