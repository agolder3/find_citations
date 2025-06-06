import os

f     = open("publication_list.txt", "r")
lines = f.readlines()

for line in lines:
    os.system("./find_citations.sh " + line.strip("\n").split(" , ")[1] + " " + line.strip("\n").split(" , ")[0].replace(" ", "_").replace(":", "").replace(">", "").replace("Ω", "ohm"))