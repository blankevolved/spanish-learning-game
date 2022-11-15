import random
import os
import json
current_set = 'basic_set'
score = 0
top_scores = []

def save():
    if os.path.exists('save.json') == False:
        with open('save.json', 'w+') as json_file:
            json_file.write('{"top_scores":[], "current_set":""}')
            json_file.close()
    
    with open('save.json', 'r') as json_file:
        loaded_json = json.load(json_file)
        json_file.close()
    
    with open('save.json', 'w+') as json_file:
        top_scores.sort(reverse=True)
        loaded_json['top_scores'] = top_scores
        loaded_json['current_set'] = current_set
        json_file.seek(0)
        json.dump(loaded_json, json_file, indent=4)
        json_file.truncate()

        json_file.close()

def load():
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

def clear():
 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
load()
set = __import__(current_set, fromlist=['set'])

def list_top_scores():
    top_scores.sort(reverse=True)
    index = 0
    num = 1
    print("Top Scores:")
    for i in top_scores:
        print(f"{num}: {top_scores[index]}")
        if num >= 10:
            break
        index = index + 1
        num = num + 1
    while num <= 10:
        print(f"{num}: 0")
        num = num + 1
def start():
    global lan
    global opplang
    while True:
        clear()
        print('1. Start Game')
        print('2. Top Scores')
        print('3. Pick a new set')
        inp = input('>>> ')
        if inp == '1':
            clear()
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
            list_top_scores()
            input()
        elif inp == '3':
            clear()
            name = input('Set name: (file ending in .py) ')
            global current_set
            global set
            try:
                set = __import__(name, fromlist=['set'])
                try:
                    set.set
                    current_set = name
                    save()
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
    ran = random.choice(set.set)
    print(f'Score: {score}\n')
    print(f'{ran[lan]}:')
    inp = input()
    clear()
    if inp == ran[opplang] or inp == ran[opplang].lower():
        score = score + 100
        print('Correct!')
    else:
        print('Incorrect!')
        top_scores.append(score)
        list_top_scores()
        score = 0
        save()
        inp = input('Try again? (y/n): ')
        if inp == 'y':
            main()
        else:
            start()
            

while True:
    main()