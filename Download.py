
from fileinput import filename

def pdf_downloader(url,name,file_name):
    from pathlib import Path # fix addrrss
    import requests

    file_name=file_name+name  
    response = requests.get(url)
    with open('Past Papers/'+name,"wb") as f:
        f.write(response.content)
    f.close()
    

def code_finder(source):
    import re
    code=re.compile(r'\((\d\d\d\d)\)')
    search=code.search(source)
    print(search.group()[1:-1])
    return (search.group()[1:-1])


def empty_file_deleter(file):
    import os

    file
    if os.path.getsize(file) == 14971:
        os.remove(file)




source=r"https://papers.gceguide.com/Cambridge%20IGCSE/Mathematics%20(0580)" #get rid of final code 
year=['14']
weather=['m']
type=['ms']
region=['1']
paper=['4']
code=code_finder(source)
print(code)

def linker(code,source):
    for y in year:
        for w in weather:
            if w!='m': 
                for t in type:
                    for r in region:
                        for p in paper:
                            paper_name=w+y+'_'+t+'_'+p+r+'.pdf'
                            link_name=source+'/'+'20'+y+'/'+ code + '_'+paper_name
                            pdf_downloader(link_name,paper_name)
                            print(link_name,paper_name) #remove in final build
            else: 
                for t in type:
                    for p in paper:
                        paper_name=str(w)+y+'_'+t+'_'+p+'2'+'.pdf'
                        link_name=source+'/' + '20' + y + '/'+code+'_'+paper_name
                        pdf_downloader(link_name,paper_name)
                        print(link_name,paper_name) #remove in final build

linker(code,source)

