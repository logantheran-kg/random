import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

txt = input("Enter word: ")

def word(txt):
    #Convert to lowercase
    txt = txt.lower()
    closematch = get_close_matches(txt, data.keys(), cutoff=0.8)[0]

    if txt in data:
        return data[txt]
    
    elif len(closematch) != 0:
        answer =  input("Did you mean: {}?\n Y/N? ".format(closematch))
        
        if answer == "Y":
            return data[closematch]
                   

    else:
            return ("Word not found. Please check and try again.")
    

output = word(txt)

if type(output) == list:
    count = 0
    for data in output:
        count = count + 1
        print("{}. {}".format(count, data))
        

else:
    print(output)
