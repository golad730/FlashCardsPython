import random

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

notes = ['A','B','D','E','F','G','MidC','HighC','HighD','HighE','HighF','HighG']


def load_images(card_images):

    global notes
    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    for note in notes:
        name = "Cards\{}.{}".format(note, extension)
        print(name)
        image = tkinter.PhotoImage(file=name)
        card_images.append((note,image))

def clearBoard():
    global title_label,flashcard, a1, a2, a3, a4

    flashcard.destroy()
    a1.destroy()
    a2.destroy()
    a3.destroy()
    a4.destroy()


def Correct():
    global score
    print("Thats the right answer")
    score += 1
    print(score)

def InCorrect():
    global live
    print("Thats incorrect")
    live -= 1
    print(live)


def checkAnswer():
    global ansVar, score, ans, live

    selection = ansVar.get()

    print(selection)
    print(ans)

    correctAnswer = bool(selection == ans)

    if correctAnswer:
        Correct()
        clearBoard()
        getQuestion()


    else:
        InCorrect()
        clearBoard()
        getQuestion()



def choiceGenerator():
    global ans, next_card

    choices = []

    next_card = deck.pop(0)
    ans = next_card[0]
    print(ans)
    choices.append(ans)

    for j in range(0,3):

        beta = random.randint(0,len(notes)-1)

        if (notes[beta] == ans):
            choice = notes[beta + 1]
            print("Answer choice is: {}".format(choice))
            choices.append(choice)

        if (notes[beta] != ans):
            choice = notes[beta]
            choices.append(choice)



    print(choices)
    random.shuffle(choices)
    print(choices)
    deck.append(next_card)

    return choices



def getQuestion():

    global title_label,flashcard, a1, a2, a3, a4
    global ansVar, ans, next_card
    ansVar = tkinter.StringVar()


    choices = choiceGenerator()



    title_label.configure(text="What note is this?")

    flashcard = tkinter.Label(mainWindow, image=next_card[1], relief='raised')
    flashcard.pack(pady=(10,10))

    a1 = tkinter.Radiobutton(mainWindow,text=choices[0], relief="flat",border=0,background="#CCCDCC", value=choices[0],variable=ansVar, command=checkAnswer)
    a1.pack(pady=(10,10),padx=(20,20))

    a2 = tkinter.Radiobutton(mainWindow,text=choices[1], relief="flat",border=0,background="#CCCDCC", value=choices[1],variable=ansVar, command=checkAnswer)
    a2.pack(pady=(10,10),padx=(20,20))

    a3 = tkinter.Radiobutton(mainWindow,text=choices[2], relief="flat",border=0,background="#CCCDCC", value=choices[2],variable=ansVar, command=checkAnswer)
    a3.pack(pady=(10,10),padx=(20,20))

    a4 = tkinter.Radiobutton(mainWindow,text=choices[3], relief="flat",border=0,background="#CCCDCC", value=choices[3],variable=ansVar, command=checkAnswer)
    a4.pack(pady=(10,10),padx=(20,20))




def startQuiz():
    startButton.destroy()
    rulesLabel.destroy()
    instructionsLabel.destroy()
    trebleClef_image.destroy()
    getQuestion()



mainWindow = tkinter.Tk()

# set up the screen and the frames for the dealer and players
mainWindow.title("Flash Cards")
mainWindow.geometry('360x640')
mainWindow.configure(background="#5B648F")

notesStack = []
load_images(notesStack)
print(notesStack)

deck = list(notesStack)

random.shuffle(deck)

next_card = deck.pop(0)
deck.append(next_card)
print(deck)


score = 0
live = 3
print(live)


title_label = tkinter.Label(mainWindow, text="Musical Notes ", font=("Comic sans MS",24,"bold"), background="#5B648F", foreground="#ffffff")
title_label.pack(pady=(10,10))


Start_image = tkinter.PhotoImage(file="Cards\TrebleClef.png")
trebleClef_image = tkinter.Label(mainWindow, image=Start_image, border=5,background="#CCCDCC")
trebleClef_image.pack()

startButtonImage = tkinter.PhotoImage(file="Resources\StartButton.png")

startButton = tkinter.Button(mainWindow,image=startButtonImage,relief="flat",border=0,background="#5B648F", command=startQuiz)
startButton.pack(pady=(10,0))


instructionsLabel = tkinter.Label(mainWindow,text="Read the rules, \n click start when ready", background="#5B648F",font=("Consoles",14),justify="center")
instructionsLabel.pack()

rulesLabel = tkinter.Label(mainWindow,
                   text="This quiz has 10 question"
                        "\nYou have 20s to solve a question"
                        "\nOnce you select a radio button, that will be a final choice"
                        "\nSo think before you select",
                   width=100,
                   font=("Times",14),
                   background="#291A4C",
                   foreground="#FF5722")



rulesLabel.pack()

score_label = tkinter.Label(mainWindow, text="score: {}".format(score), font=("Consolas",18,"bold"), background="#5B648F", foreground="#ffffff")
score_label.pack(pady=(10,5))
time_label = tkinter.Label(mainWindow, text="Lives: {}".format(live), font=("Consolas",18,"bold"), background="#5B648F", foreground="#ffffff")
time_label.pack(pady=(0,10))



mainWindow.mainloop()
