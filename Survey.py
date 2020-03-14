# Survey with questions 

# Python Question List
questions_list = ["What crisis/disaster are you interested in supporting?", "What global issues do you value?", "What do you value in a charity?"]

# List of options for each of the questions
options_list = [
    ["1. Flooding", "2. Hurricanes & Tropical Storms", "3. Diseases", "4. Wildfires", "5. Earthquakes","6. Droughts", "7. Tornadoes & Severe Storms"], #Different Crisis/Natural Disasters
    ["1. Poverty", "2. Education", "3. Environment", "4. Health/Well-being", "5. Equality", "6. Hunger & Clean Water", "7. Shelter"], #Global Issues
    [""]]

#user input of answers
answer_list = []
temp_list = []
answer = 0
remove_index = []

# question 1
def q_1A():
    print(questions_list[0] + "\n" + "\n".join(options_list[0]))
    print("What is your first choice?")
    ans = input()
    answer = int(ans)
    if answer <= 0 or answer > 7:
        print("Invalid response. Type a number from 1 to 7")
        q_1A()
    else:
        answer_list.append(options_list[0][answer-1])
        remove_index.append(answer)
        temp_list = options_list[0][:answer-1] + options_list[0][answer:]
        q_1B(options_list, temp_list, remove_index)

def q_1B(options_list, temp_list, remove_index):
    print("What is your second choice?" + "\n" + "\n".join(temp_list))
    ans = input()
    answer = int(ans)
    if answer == remove_index[0]:
        print("Invalid input. Choose one of the following:" + "\n")
        q_1B(options_list, temp_list, remove_index)
    elif answer <= 0 or answer > 7:
        print("Invalid Response. Choose one of the following:" + "\n")
        q_1B(options_list, temp_list, remove_index)
    else:
        answer_list.append(options_list[0][answer-1]) # put answer into answer list
        print(answer_list)
        temp_index = temp_list.index(answer_list[1]) # remove that answer from the temp list by getting its index in temp list
        print(temp_index)
        remove_index.append(answer) # put index of removed - index is in original list
        print(temp_list)
        del temp_list[temp_index]
        print(temp_list)
        q_1C(options_list, temp_list, remove_index)

def q_1C(options_list, temp_list, remove_index):
    

if __name__=="__main__":
    q_1A()