
import os
import re
text_to_search = input("Enter Text to Search : ").lower()
filelist = os.listdir("/Users/umar/Desktop/Ibrahim/Training/Regex")
filenamelist = []

def funct(a):
    match = list(re.finditer(r'txt$',a))
    if(match!=[]):
        return True
    else:
        return False

filenamelist = list(filter(funct,filelist))
print("list of files - ",filenamelist)
for i in filenamelist:
    myFile = open(i, mode = "r")
    file_name=(myFile.name)
    list_of_line=[]
    lineNum = 1
    while True:
        line = myFile.readline()
        # line is empty so exit
        if not line:
            break
        line = line.lower()
        found = list(re.finditer(text_to_search,line))
        if(found!=[]):
           list_of_line.append(lineNum)
        lineNum += 1
        
    if(list_of_line!=[]):
        print(text_to_search,"is found in",file_name," at verse",list_of_line)
    else:
        print("Not found in ",file_name)

    myFile.close()
