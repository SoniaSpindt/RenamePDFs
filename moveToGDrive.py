import shutil
import glob
import re
import os

quizFolder = input("Drag the quiz folder containing the renamed files here. Then, hit enter: ").strip()
sortDestination = input("Drag the Google Drive Folder containing the student folders here. Then, hit enter: ").strip()
sortDestination = sortDestination.replace('\\','')

for origfile in glob.glob(quizFolder + "/*.pdf"):
    pdfname = os.path.basename(origfile)
    numcaps = len(re.findall('([A-Z])', pdfname.split('_')[0]))
    if numcaps == 2:
        parts = re.search(r'([A-Z][^A-Z]+)([A-Z][^_]+)', pdfname)
        if parts is None or len(parts.groups()) != 2:
            print(f"FILE {origfile} has an unusualname! Skipping")
            continue
        lastName, firstName = parts.groups()
        shutil.copyfile(origfile, sortDestination+'/'+f"{lastName}, {firstName}/{pdfname}" )
    elif numcaps == 3:
        parts = re.search(r'([A-Z][^A-Z]+)([A-Z][^A-Z]+)([A-Z][^_]+)', pdfname)
        if parts is None or len(parts.groups()) != 3:
            print(f"FILE {origfile} has an unusualname! Skipping")
            continue
        lastName1, lastName2, firstName = parts.groups()
        if not os.path.exists(sortDestination+'/'+f"{lastName1}-{lastName2}, {firstName}"):
            print(f"FILE {origfile} has an unusualname! Skipping")
            continue
        shutil.copyfile(origfile, sortDestination+'/'+f"{lastName1}-{lastName2}, {firstName}/{pdfname}" )
    else:
        print("File", origfile, "has an unusual name! skipping")
