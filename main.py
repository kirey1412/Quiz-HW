import pgzrun
WIDTH=700
HEIGHT=580

questionfile="Quiz Master practice/questionlist.txt"
timeleft=10
gameover=False
score=0

# create shapes
    # marqueebox = moving text above
marqueebox=Rect(0,0,800,60)
mainquestionbox=Rect(0,0, 300,20)
timerbox=Rect(0,0, 150,155)
skipbox=Rect(0,0,60,135)
option_one=Rect(0,0,60,140)
option_two=Rect(0,0,60,140)
option_three=Rect(0,0,60,140)
option_four=Rect(0,0,60,140)
options=[option_one, option_two, option_three, option_four]

marquemessage=""

questions=[] # questions list contains all the questions in .txt file
questioncount=0 # questioncount==0 because we haven't start the game. nothing is adding
questionindex=0 # displayed questions will be starting from the very beginning at 0 index point

# for questions to be shown on screen, read question is needed; open book (txt) for (computer) to read infos
def readquestion():
    global questioncount, questions
    readfile=open(questionfile, "r")
    for question in readfile:
        questions.append(question) # adding element as in the bracket to the end of a list
        questioncount+=1
    readfile.close()

def nextquestion(): # question and options combined
    global questionindex, questions
    questionindex+=1  # if a question is answered, this var will help indicate for question shift.
    return questions.pop(0).split(",") # pop removes the last question in order to move forward to the next question
# return is returning the value
def draw():
    screen.fill("lightpink")
    # screen.draw.filled_rect is used to color rectangle mentioned in brackets. colors is mentioned after, seperated with comma and double quotation.
    screen.draw.filled_rect(marqueebox,"black") # use black for transparancy
    screen.draw.filled_rect(mainquestionbox,(249,205,212))
    screen.draw.filled_rect(timerbox,(236,161,172))
    screen.draw.filled_rect(skipbox,(178,91,110))
    for answerbox in options:
        screen.draw.filled_rect(answerbox,(255,170,165))
    #'options' already stand for 4 options=options 1-4
    
    marquemessage="Welcome to Quiz Master!"
    screen.draw.textbox(marquemessage,marqueebox,color=(110,26,61),shadow=(0.5,0.5),scolor="dimgray")
    screen.draw.textbox(a[0], mainquestionbox, color=(165,60,90), shadow=(0.5,0.5), scolor="dimgray") # 0 because starting at the very beginning of the questions list
    index=1
    # for option in options:   #For loop; 'option' serves as each of the options in 'options'; in For loop, multiple elements in the same list could be simplified for a command
      #  screen.draw.textbox(a[1], option, color=(220,166,170), shadow=(0.5,0.5), scolor="dimgray")
    # index+=1
    # print("Hello")
    for i in options:
        screen.draw.textbox(a[index], i, color=(110,26,61), shadow=(0.5,0.5), scolor="dimgray")
        index+=1
    screen.draw.textbox("skip",skipbox, color=(110,26,61), shadow=(0.5,0.5), scolor="dimgray")
    screen.draw.textbox(str(timeleft), timerbox, color=(202,106,132), shadow=(0.5,0.5), scolor="dimgray")

def updatetime():
        global timeleft
        if timeleft:
            timeleft-=1
        else:
            gameover()

def game_over():
    global timeleft, gameover
    nextquestion=[message,"-","-","-","-"] # message = the text inside the question box
    if timeleft==0:
        message="You got {score} questions correct."
        gameover=True

def movemarquee():
    marqueebox.x-=2 #sliding text by 2 px
    if marqueebox.right<0:
        marqueebox.left=WIDTH

readquestion()
a = nextquestion()
# whenever the function is having return in it, we call the function inside the variable.

def update(): #marqueebox is always sliding. so it always need an update for every second in order to slide.
    movemarquee()

clock.schedule_interval(updatetime,1) # 1 as it stands to count down one by one (decreasing) from timeleft, which is 10




pgzrun.go()