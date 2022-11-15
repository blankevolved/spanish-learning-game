# Spanish Learning Game (SLG)
## Use Case:

You use this tool to practice spanish words you define in a set

## Create a Set:

Create a file ending with .py [ (name).py ].

Create a dict variable in the file you just created:
```
set = {}
```
Add your words like this:
```
set = {
    0:{
        'en':(word),
        'sp':(word)
    }
}
```
For every new word increse the number, starting from 0:
```
set = {
    0:{
        'en':(word),
        'sp':(word)
    }
    1:{
        'en':(another_word),
        'sp':(another_word)
    }
}
```
## Import a Set
Run the main.py file, you will see a screen similar to this:
```
1. Start Game
2. Top Scores
3. Pick a new set
>>> 
```
Select 'Pick a new set', you should now see a screen like this:
```
Set name: (file ending in .py) 
```
Type in the file ending in .py's name, you will now be taken back to the start screen. 

You can start the game and the new set will be used. 

## Saving/Loading
Your top scores and current set are saved in the 'save.json' file.

You can freely edit this file if anything goes wrong.

The 'save.json' file is loaded when you run 'main.py'