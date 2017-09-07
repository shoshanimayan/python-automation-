import os
def directoryWalk():
    root = input("choose root: ")
    try:
        if not os.path.exists(root):
            raise Exception(' not a root')
            
        for folderName, subfolders, filenames in os.walk(root):
            print('The current folder is '+ folderName)
            for subfolder in subfolders:
                print('SUBFOLDER OF ' +folderName+":" + subfolder )
            for filename in filenames:
                print("FILE INSIDE " + folderName + ': ' + filename)
            print("")
    except Exception as e:
        print(type(e))
        print(e)
directoryWalk()
