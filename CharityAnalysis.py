#%%codecell
'''
Top Disasters:
- Flooding
- Diseases
- Wildfires

Top Categories:
- Environment
- Equality
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('HTG_UsedFiles/charities.txt',lineterminator='\n');
data = data.drop(['Unnamed: 0'], axis=1);


causes_dict = {
    "Poverty": ["Multipurpose Human Services Organizations", "Social Services", "Development and Relief Services"],
    "Education": ["Adult Education Programs and Services", "Early Childhood Programs and Services", "Education Policy and Reform", "Scholarship and Financial Support", "Special Education", "Youth Education Programs and Services","Multipurpose Human Services Organizations" ],
    "Environment": ["Botanical Gardens, Parks, and Nature Centers", "Environmental Protection and Conservation", "Non-Medical Science & Technology Research"],
    "Relief": ["Humanitarian Relief Supplies", "Development and Relief Services"],
    "Health/Well-being": ["Diseases, Disorders, and Disciplines", "Medical Research", "Patient and Family Support", "Treatment and Prevention Services", "Children's and Family Services", "Multipurpose Human Services Organizations", "Rescue Missions", "Social Services", "Youth Development, Shelter, and Crisis Services", "Development and Relief Services", "Social and Public Policy Research"],
    "Equality": ["Multipurpose Human Services Organizations", "Social Services", "Advocacy and Education", "International Peace, Security, and Affairs", "Religious Activities", "Religious Media and Broadcasting", "Non-Medical Science & Technology Research", "Social and Public Policy Research"],
    "Hunger & Clean Water": ["Food Banks, Food Pantries, and Food Distribution"],
    "Shelter": ["Homeless Services", "Social Services", "Youth Development, Shelter, and Crisis Services"],
    "Animals": ["Animal Rights, Welfare and Services", "Wildlife Conservation", "Zoos and Aquariums"],
    "Art, Culture, Humanities": ["Libraries, Historical Societies and Landmark Preservation", "Museum", "Performing Arts", "Public Broadcasting and Media"],
    "Community Development": ["Community Foundations", "Housing and Neighborhood Development", "Jewish Foundation", "United Ways", "Religious Activities", "Religious Media and Broadcasting", "Social and Public Policy Research"]
    };

#%%codecell

def getCharities(globalIssues): #takes in array of global issues, returns charity list
    totalCharities = [[0 for x in range(len(globalIssues))] for y in range(2)];
    for i in range(0, len(globalIssues), 1):
        issue = globalIssues[i];
        concatArr = [];
        arr = causes_dict.get(issue);
        for cause in arr:
            charityList = data.loc[data['Cause'] == cause];
            concatArr.append(charityList);
        charityList = pd.concat(concatArr);
        totalCharities[i][0] = issue;
        totalCharities[i][1] = (charityList);
    return totalCharities;

def sortTopProgExp(df):
    retrDF = df.sort_values(['Program Expenses'], ascending =0);
    retrDF = retrDF.drop(['Fundraising Expenses', 'Administrative Expenses'], axis=1);
    printDF = retrDF.drop(["Category", "['Program Name', 'Expense Percentage']", 'Fundraising Efficiency'], axis=1);
    print(printDF.head(5));
    return retrDF.head(5);

if __name__=="__main__":

    '''

    Through set-up form will pick a number (up to 5) primary global issues
    For this example, picked Environment & Equality

    '''
    globalIssues = ["Environment", "Equality"];

    for i in range(0, len(globalIssues), 1):
        '''
        Top 5 charities, sorted in terms of cause and percent of funds that go
        twoards programs are picked to be considered by further algorithms.
        '''
        listing = getCharities(globalIssues);
        print("Charities for: "+globalIssues[i])
        top5 = sortTopProgExp(listing[i][1]);
    #%%codecell
