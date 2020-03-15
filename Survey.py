#Survey with questions 

# Python Question List
questions_list = ["Question 1: What crisis/disaster are you interested in supporting?", "Question 2: What global issues do you value?", "Question 3: What causes are you interested in supporting?"]

# List of options for each of the questions
options_list = [
    ["1. Flooding", "2. Hurricanes & Tropical Storms", "3. Diseases", "4. Wildfires", "5. Earthquakes","6. Droughts", "7. Tornadoes & Severe Storms"], #Different Crisis/Natural Disasters
    ["1. Poverty", "2. Education", "3. Environment", "4. Health/Well-being", "5. Equality", "6. Hunger & Clean Water", "7. Shelter", "8. Animals", "9. Art, Culture, Humanities", "10. Community Development"]] #Global Issues

causes_list = ["Poverty", "Education", "Environment", "Health/Well-being", "Equality", "Hunger & Clean Water", "Shelter", "Animals", "Art, Culture, Humanities", "Community Development"]

causes_dict = {
    "Poverty": ["Multipurpose Human Services Organizations", "Social Services", "Development and Relief Services"],
    "Education": ["Adult Education Programs and Services", "Early Childhood Programs and Services", "Education Policy and Reform", "Scholarship and Financial Support", "Special Education", "Youth Education Programs and Services","Multipurpose Human Services Organizations" ],
    "Environment": ["Botanical Gardens, Parks, and Nature Centers", "Environmental Protection and Conservation",  "Humanitarian Relief Supplies", "Development and Relief Services", "Non-Medical Science & Technology Research"],
    "Health/Well-being": ["Diseases, Disorders, and Disciplines", "Medical Research", "Patient and Family Support", "Treatment and Prevention Services", "Children's and Family Services", "Multipurpose Human Services Organizations", "Rescue Missions", "Social Services", "Youth Development, Shelter, and Crisis Services", "Development and Relief Services", "Social and Public Policy Research"],
    "Equality": ["Multipurpose Human Services Organizations", "Social Services", "Advocacy and Education", "Development and Relief Services", "Humanitarian Relief Supplies", "International Peace, Security, and Affairs", "Religious Activities", "Religious Media and Broadcasting", "Non-Medical Science & Technology Research", "Social and Public Policy Research"],
    "Hunger & Clean Water": ["Food Banks, Food Pantries, and Food Distribution"],
    "Shelter": ["Homeless Services", "Social Services", "Youth Development, Shelter, and Crisis Services",  "Humanitarian Relief Supplies"],
    "Animals": ["Animal Rights, Welfare and Services", "Wildlife Conservation", "Zoos and Aquariums"],
    "Art, Culture, Humanities": ["Libraries, Historical Societies and Landmark Preservation", "Museum", "Performing Arts", "Public Broadcasting and Media"],
    "Community Development": ["Community Foundations", "Housing and Neighborhood Development", "Jewish Foundation", "United Ways", "Religious Activities", "Religious Media and Broadcasting", "Social and Public Policy Research"]
    }

#user input of answers
issue_count = len(options_list[1])
answer_list1 = []
answer_list2 = []
temp_list = []
answer = 0
remove_index = []

# question 1

def q_1A(): # Question 1 First Choice
    print(questions_list[0] + "\n" + "\n".join(options_list[0]))
    print("What is your first choice?")
    ans = input()
    answer = int(ans)
    if answer <= 0 or answer > issue_count:
        print("Invalid response. Type a number from 1 to 7")
        q_1A()
    else:
        answer_list1.append(options_list[0][answer-1])
        remove_index.append(answer)
        temp_list = options_list[0][:answer-1] + options_list[0][answer:]
        q_1B(options_list, temp_list, remove_index)

def q_1B(options_list, temp_list, remove_index): # Question 1 Second Choice
    print("What is your second choice?" + "\n" + "\n".join(temp_list))
    ans = input()
    answer = int(ans)
    if answer == remove_index[0]:
        print("Invalid input. Choose one of the following:" + "\n")
        q_1B(options_list, temp_list, remove_index)
    elif answer <= 0 or answer > issue_count:
        print("Invalid Response. Choose one of the following:" + "\n")
        q_1B(options_list, temp_list, remove_index)
    else:
        answer_list1.append(options_list[0][answer-1]) # put answer into answer list
        temp_index = temp_list.index(answer_list1[1]) # remove that answer from the temp list by getting its index in temp list
        remove_index.append(answer) # put index of removed - index is in original list -1
        del temp_list[temp_index]
        q_1C(options_list, temp_list, remove_index)

def q_1C(options_list, temp_list, remove_index): # Question 1 Third Choice
    print("What is your third choice?" + "\n" + "\n".join(temp_list))
    ans = input()
    answer = int(ans)
    if answer == remove_index[0] or answer == remove_index[1]:
        print("Invalid input. Choose one of the following:" + "\n")
        q_1C(options_list, temp_list, remove_index)
    elif answer <= 0 or answer > issue_count:
        print("Invalid Response. Choose one of the following:" + "\n")
        q_1C(options_list, temp_list, remove_index)
    else:
        answer_list1.append(options_list[0][answer-1]) # put answer into answer list
        remove_index.clear()
        temp_list = []
        answer = 0
    
    print("Crisis/Disaster Responses: " + "\n" + "\n".join(answer_list1) + "\n\n")

def q_2():
    print(questions_list[1] + "\n" + "\n".join(options_list[1]))

    print("You may select up to 5 (Enter 'done' when you no longer want to select):")
    enter = True
    i = 0
    x = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth"}
    while enter:
        if i == 5:
            enter = False
            print("Max count reached")
            break
        else:
            print("Select your " + x[i+1] + " choice:")
            ans = input()
            if ans == "done":
                break
            answer = int(ans)
            if answer <= 0 or answer > issue_count:
                print("Invalid input. Please choose one of the following:")
                q_2()
            else:
                answer_list2.append(options_list[1][answer-1])
                remove_index.append(answer-1)
                i += 1
    
    print("Global Issues Choices: " + "\n" + "\n".join(answer_list2) + "\n\n")

def q_3():
    final_val_causes = []

    for x in remove_index:
        cause = causes_list[x]
        final_val_causes.extend(causes_dict[cause])
    final_val_causes = list(set(final_val_causes))

    cause_choices = []

    for cause in final_val_causes:
        cause_choices.append(str(final_val_causes.index(cause)+1) + ". " + cause)

    if len(cause_choices) > 10:
        print(questions_list[2] + "\n" + "\n".join(cause_choices))
        print("You may select up to 10:")
    else:
        print("Final Causes:" + "\n" + "\n".join(final_val_causes) + "\n\n")




if __name__=="__main__":
    q_1A()
    q_2()
    q_3()
