# Repository to find citations of works

## Install jq (Example : Ubuntu):
```
sudo apt-get update
sudo apt install dos2unix
sudo apt-get install jq
```

## Install doi2bib
```
sudo pip install doi2bib
```

## Create Publication List and Get all citations
```
echo "paper1 , <DOI>" >> publication_list.txt
echo "paper2 , <DOI>" >> publication_list.txt
python3 generate_bib.py
```

## Get citation info for a specific author:
```
python3 citations_by_author.py <author_name> > <author_name.txt>
```

## Example:

<img width="1879" height="561" alt="image" src="https://github.com/user-attachments/assets/46156928-7eab-46e4-bd69-0786c09bc5dc" />

