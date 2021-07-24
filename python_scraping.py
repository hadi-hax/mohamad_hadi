#pip install requests
import requests  
#pip install openpuxl   
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
#pip install beautifulsoup4   # i think it was this
from bs4 import BeautifulSoup

# we make vareble for storeg the elements
job = []
client = []
time1 = []
offer = []
desc = []

# we include this library for get the link
result = requests.get("https://mostaql.com/projects?category=development&budget_max=10000&sort=latest")

# dim vareble for take content
src = result.content

# here we include library to edit in html
suop = BeautifulSoup(src ,"lxml")

# here we go to web said and we get the tags we need it
job_titles = suop.find_all("span" , { "class":"text-zeta12 text-meta"})
client_name = suop.find_all("a" , {"class":"text-muted"})
time = suop.find_all("time")
offers = suop.find_all("li" , {"class":"text-muted"})
description = suop.find_all("a" , {"class":"details-url"})

# this for to extract the text 
for i in range(len(job_titles)):
    job.append(job_titles[i].text)
    client.append(client_name[i].text)
    time1.append(time[i].text)
    desc.append(description[i].text)
for j in range(len(offers)):
    offer.append(offers[j].text)
print("the 1 page is complet")
# this loop for the repertnal all above to athre page
for h in range(2,15):
    result = requests.get(f"https://mostaql.com/projects?page={h}&category=development&budget_max=10000&sort=latest")

    src = result.content

    suop = BeautifulSoup(src ,"lxml")

    job_titles = suop.find_all("span" , { "class":"text-zeta12 text-meta"})
    client_name = suop.find_all("a" , {"class":"text-muted"})
    time = suop.find_all("time")
    offers = suop.find_all("li" , {"class":"text-muted"})
    description = suop.find_all("a" , {"class":"details-url"})

    for i in range(len(job_titles)):
        job.append(job_titles[i].text)
        client.append(client_name[i].text)
        time1.append(time[i].text)
        desc.append(description[i].text)
    for j in range(len(offers)):
        offer.append(offers[j].text)
    print(f"the {h} page is complet")

# here we biging use the library openpyxl for edit in our file

# we write the titles for column
ws.append(["عنوان المشروع","اسم العميل", "مدة الطلب", "عدد العروض", "الوصف"])

#this loop to wite in cilumn because this library it write onle row or one element
for i in range(len(job)):
    ws["A"+str(i+2)] = job[i]

for i in range(len(job)):
    ws["B"+str(i+2)] = client[i]
    
for i in range(len(job)):
    ws["C"+str(i+2)] = time1[i]

g = 1  
for i in range(len(offer)):
    if ((i%2) != 0):
       g += 1
       ws["D"+str(g)] = offer[i]  
   
for i in range(len(job)):
    ws["E"+str(i+2)] = desc[i]

# to save work in my file
wb.save('jobs.xlsx')
