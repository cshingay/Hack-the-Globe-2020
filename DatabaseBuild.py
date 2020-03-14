#Builds Database of Charities

from bs4 import BeautifulSoup as bs
import requests
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
import pandas as pd

print(sys.version+"\n");
allowed = True;
data = []


#getting first page
charityURL = requests.get("https://www.charitywatch.org/top-rated-charities").text
wiki = bs(charityURL, 'lxml')
wiki.prettify();

#grabbing first listing of charity
init = wiki.find("div", attrs={'id':'list-2'});

while(allowed): #try/except to avoid NoneType
    try:
        category = init.find("h2").get_text(); #finds category of charity
        charities = init.tbody.findAll("a"); #finds charities in category

        for i in charities: #searches each charity in category
            name = i.get_text();
            org = [];
            org.append(name);
            org.append(category);
            #calls new website to search other data
            name = name.replace(" ", "-").replace("(","").replace(")","");
            name = name.lower();
            extraURL = requests.get("https://www.charitywatch.org/charities/" + name).text;
            extr = bs(extraURL, 'lxml');
            extr.prettify();
            stats = extr.findAll("div", attrs={'class':'charity-stat'})
            try:
                for i in range(1, 3):
                    percent = stats[i].get_text();
                    percent = percent.replace(" ", "").replace("\t", "").replace("\n", "")
                    org.append(percent)
            except:
                break;

            data.append(org);

        init = init.find_next_sibling("div");
    except:
        allowed = False;

df = pd.DataFrame(data, columns = ['Charity Name', 'Cause', 'Program Percentage', 'Cost to $100']);
print(df)

df.to_csv('charityDatabase.txt')
