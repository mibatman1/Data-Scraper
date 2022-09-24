from bs4 import BeautifulSoup
import requests
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials



print("Enter the skill that you are familier with: ")
fs=input("> ")
print("Enter Skill that you are not familier with: ")
ufs=input("> ")
print("Where do you want to save the data?: \n Press 0 to save into device and 1 to save into Google Sheet")
print("1-Into Device: \n2-Sheet: ")
op=int(input("Enter the choice: "))
print(f"Filtering out {ufs}")





def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup=BeautifulSoup(html_text,'lxml')
    js=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index, j in enumerate(js):
        jf=j.find('span',class_='sim-posted').span.text
        if 'few' in jf: 
            c=j.find('h3',class_='joblist-comp-name').text.replace(' ','')
            s=j.find('span',class_='srp-skills').text.replace(' ','')
            mi=j.header.h2.a['href']
            if ufs not in s:
                with open(f'/home/mibatman/Desktop/PYPR{index}.txt','w') as l:
                    l.write(f'Company Name: {c.strip()}')
                    l.write(f'Required Skills: {s.strip()}')
                    l.write(f'More info: {mi}')
                print(f'File saved: {index}')



def sheet_a():
    scope=["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds=ServiceAccountCredentials.from_json_keyfile_name('Test-sheet-e432f87de6bc.json',scope)
    client=gspread.authorize(creds)
    sheet=client.open('Tut').sheet1

    html_text=requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={fs}&txtLocation=').text
    soup=BeautifulSoup(html_text,'lxml')
    js=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index, j in enumerate(js):
        jf=j.find('span',class_='sim-posted').span.text
        if 'few' in jf: 
            c=j.find('h3',class_='joblist-comp-name').text.replace(' ','')
            s=j.find('span',class_='srp-skills').text.replace(' ','')
            mi=j.header.h2.a['href']
            if ufs not in s:
                l=f"Company Name:{c.strip()}"
                t=f"Required Skills:{s.strip()}"
                z=f"More info:{mi}"
                insert=[l,t,z]
                for q in range(1,100):
                    sheet.insert_row(insert,q)




if __name__=='__main__':
    while True:
        if op==1:
            sheet_a()
            time_wait=10
            print(f'Waiting {time_wait} minutes....')
            time.sleep(time_wait*60)
        else:
            find_jobs()
            time_wait=10
            print(f"waiting {time_wait} minutes....")
            time.sleep(time_wait*60)