'''
General Structure:
    - Used beautifulsoup api to scrape data about charities from Charity Navigator
    - Data gathered:
        - Name
        - General Category
        - Specific Cause
        - Financial Data
            - Program Expense Percentage
            - Administrative Expense Percentage
            - Fundraising Expense Percentage
            - Fundraising Efficiency
        - Focused Programs
            - Program name
            - Percent of budget allocated towards
    - Created pandas dataframe and saved as txt file
'''

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import pandas as pd

arr = [];
titles = [];
found = False;

titles.append("Charity");
titles.append("Category");
titles.append("Cause");

pageNum = 0
allow = True
while(allow):
    try:
        url = "https://www.charitynavigator.org/index.cfm?FromRec="+str(pageNum*20)+"&bay=search.results&overallrtg=4"
        html = requests.get(url).text;
        page = bs(html, 'lxml');
        page.prettify();
        lists = page.findAll("td", attrs={'class':'highlight-matches'});
        a = lists[1]

        for item in lists:
            info = []
            name = item.a.get_text();
            slogan = item.p.get_text();
            info.append(name);

            general = item.find("p", attrs={'class':'category'}).get_text();
            general = general.replace('LOCATION:', "");
            general = general.replace('\n', '');
            general = general.replace('\t', '');
            category = general[general.index(": ")+2:general.index("CAUSE")-38]
            cause = general[general.index("CAUSE")+42:];
            cause = cause[1:len(cause)-14]

            info.append(category);
            info.append(cause);

            itemLink = item.a.get('href');
            charityPage = requests.get(itemLink).text;
            nPage = bs(charityPage, 'lxml');
            nPage.prettify();

            data = nPage.findAll("a", {'class':'glossary'});
            j = 0
            for section in data:
                txt = section.get_text(); #need this once
                if(not found):
                    titles.append(txt);
                pa = section.parent.findNext('td').get_text();
                pa = pa.replace(" ", "");
                if(len(pa) <= 10):
                    info.append(pa);
                    if(j == 3):
                        break;
                    j+=1;
            found = True;

            programLink = itemLink.replace("summary","programs");
            programPage = requests.get(programLink).text;
            page = bs(programPage, 'lxml');
            page.prettify();

            okay = True;
            prog = page.find("table", {'class':'summaryPage'});
            try:
                each = prog.findAll('tr')
            except:
                info.append(["No Program Info"])
                okay = False;
            programs = []
            if(okay):
                for i in range(1, len(each), 1):
                    term = each[i].find("td");
                    progName = term.get_text();
                    term = term.findNext('td').findNext('td')
                    expensePerc = term.get_text().replace(" ","");
                    expensePerc = expensePerc.replace("\r", "")
                    expensePerc = expensePerc.replace("\n","");
                    pro = [];
                    pro.append(progName);
                    pro.append(expensePerc);
                    programs.append(pro)
                info.append(programs)
            arr.append(info)
        pageNum+=1;
        print(pageNum)
    except:
        allow = False;
        print("we break");
        break;

titles.append(["Program Name", "Expense Percentage"])

df = pd.DataFrame(arr, columns = titles);
df.to_csv("charities.txt");
print("hello");
