import random
import os
import json
from glob import glob
current_set = 'basic_set'
score = 0
top_scores = []

def save():
    ## check if save.json dosent exist, if it dosent create it.
    if os.path.exists('save.json') == False:
        with open('save.json', 'w+') as json_file:
            json_file.write('{"top_scores":[], "current_set":""}')
            json_file.close()
    
    ## load the json file with the json module and store it in loaded_json
    with open('save.json', 'r') as json_file:
        loaded_json = json.load(json_file)
        json_file.close()
    
    ## write to the save file
    with open('save.json', 'w+') as json_file:
        top_scores.sort(reverse=True)
        loaded_json['top_scores'] = top_scores
        loaded_json['current_set'] = current_set
        json_file.seek(0)
        json.dump(loaded_json, json_file, indent=4)
        json_file.truncate()

        json_file.close()

def load():
    ## check if save.json exists
    if os.path.exists('save.json') == True:
        with open('save.json', 'r') as json_file:
            loaded_json = json.load(json_file)
            global top_scores
            global current_set
            try:
                top_scores = loaded_json['top_scores']
                current_set = loaded_json['current_set']
            except:
                pass    

            json_file.close()
## clears the screen
def clear():
 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
## load data from save
load()
## import set var from the current set
set = __import__(current_set, fromlist=['set'])

def list_top_scores():
    ## reverse scores
    top_scores.sort(reverse=True)
    ## define index and num
    index = 0
    num = 1
    print("Top Scores:")
    ## print each top score except for the ones over num 10
    for i in top_scores:
        print(f"{num}: {top_scores[index]}")
        if num >= 10:
            break
        index = index + 1
        num = num + 1
    ## print up the rest of the scores as a score of 0
    while num <= 10:
        print(f"{num}: 0")
        num = num + 1
# start menu
def start():
    global lan
    global opplang
    global current_set
    while True:
        clear()
        print(f'Current Set: {current_set}\n')
        print('1. Start Game')
        print('2. Top Scores')
        print('3. Pick a new set')
        inp = input('>>> ')

        if inp == '1':
            clear()
            ## set lang and opplang for the game, then start it
            lan = input('Select the language you want to prompted in (en, sp): ')
            if lan == 'en':
                opplang = 'sp'
                break
            elif lan == 'sp':
                opplang = 'en'
                break
            else:
                print('Invalid Option')

        elif inp == '2':
            ## list the top scores
            list_top_scores()
            input()

        elif inp == '3':
            clear()
            ## print all .py files in the current directory
            print('All .py files in the current directory:')
            for i in glob("*.py"):
                print(i)
            print()
            ## get the set name to try and import
            name = input('Set name: (file ending in .py) ')
            global set
            ## try to import name, if it dosent import, return an error
            try:
                ## import the set
                set = __import__(name, fromlist=['set'])
                try:
                    ## check if the set has a set var
                    set.set
                    ## if so set the current set to name
                    current_set = name
                    save()
                ## if it dosent import the set var, return an error
                except AttributeError:
                    print('No name variable found in file')
                    input()
            except ImportError:
                print('That file dosent exist')
                input()

start()
clear()
def main():
    global score
    global lan
    global opplang
    ## get random number from current set
    ran = random.choice(set.set)
    ## print score and random word
    print(f'Score: {score}\n')
    print(f'{ran[lan]}:')
    ## get user input
    inp = input('>>> ')
    clear()
    ## check if inp matches the correct answer
    if inp == ran[opplang] or inp == ran[opplang].lower():
        ## increase score
        score = score + 100
        print('Correct!')
    else:
        print('Incorrect!')
        ## add the current score to the top scores list
        top_scores.append(score)
        ## list the top scores
        list_top_scores()
        ## reset score
        score = 0
        ## save the game
        save()
        ## ask user if they wanna try again
        inp = input('Try again? (y/n): ')
        if inp == 'y':
            ## run game again
            main()
        else:
            ## go back to start menu
            start()
            
## main loop
while True:
    main()