import textract
import re
import shutil
import sys
import os
import glob

def main():
    #Get directory of PDFs and new home directory
    directoryPath = input("Drag your folder of PDFs here. Then, hit enter: ").strip()
    newDirectoryPath = input("Drag your destination folder here. Then, hit enter: ").strip()
    #sortDestination = input("Drag the Google Drive Folder containing the student folders here. Then, hit enter: ").strip()

    #Get quiz number from user
    quiz = input("What quiz number are these reports for? Please enter an integer: ")

    #Rename all the files
    for fileName in glob.glob(directoryPath + "/*.pdf"):
        print("Operating on ", fileName)
        renameFile(fileName, quiz, newDirectoryPath)

def renameFile(fileName, quizNum, directory):

    # Grab student name from PDF
    text = textract.process(fileName, method='tesseract', language='eng')
    match = re.search(r'student:(.*)\(', text.decode('utf8'))
    if match:
        fullName = match.groups()[0].strip()
        nameParts = fullName.split(" ", 1)
        lastName = nameParts[1].replace(" ", "")
        firstInitial = nameParts[0][0]

        #Make copy of PDF and rename using student name and quiz number
        newfilename = lastName + nameParts[0] + "_Q" + quizNum + ".pdf"
        shutil.copyfile(fileName, directory + "/" + newfilename)
        # shutil.copyfile(fileName, sortDestination.replace('\\', '')+"/"+fullName+"/"+newfilename)
    else:
        print("No name found in ", fileName)

main()
