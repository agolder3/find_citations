import glob
import sys

author = sys.argv[1]

for filename in glob.glob("*.bib"):
    
    f     = open(filename, "r")
    lines = f.readlines()
    cited = False

    for line in lines:
        if author in line:
            cited = True
            break
    
    if cited:
        print("Cited Paper :", filename.strip(".bib").replace("-citations","").replace("_", " "))
        print("Citing Papers : ")
        i = 0    
        for line in lines:
            if author in line:
                line_contents = line.split(",")
                for j in range(len(line_contents)):
                    if "title" in line_contents[j] and not "booktitle" in line_contents[j]:
                        print(str(i + 1), line_contents[j].split("=")[1].strip("{").replace("}",""))
        
                i = i + 1

        print("\n")