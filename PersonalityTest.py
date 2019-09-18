from tkinter import *
num = 0
agreeability = 0
extraversion = 0
judgability = 0

QA1 = ["You hate cats. Like hate hate them. Someone is telling you about how much you love cats and ask you what you think of cats. How do you respond?", "I hate cats.", "I'm more of a dog person but I still like cats.", "I love cats!"]
QA2 = ["You and your'e friend are in a debate about politics. You tell him a fact is wrong and ou decide to look it up as proof. You end up being right. You say:", "Ha I told you so.", "Yeah I read about this last week.", "I wasn't sure either."]
QA3 = ["You LOVE Juicy Fruit Gum. You take out your gum in class and an classmate next to you asks for a peice.", "Don't give him one.", "Give him one as long as it's not the last peice.", "Give him one."]




qList = [QA1, QA2, QA3]



root = Tk()

def resp1 ():
    print("resp1")
    labelUpdate()
def resp2 ():
    print("resp2")
    labelUpdate()
def resp3 ():
    print("resp3")
    labelUpdate()


def labelUpdate():
    global num
    num += 1


topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)
leftFrame = Frame(bottomFrame)
leftFrame.pack(side = LEFT)
sLeftFrame = Frame(bottomFrame)
sLeftFrame.pack(side = LEFT)
middleFrame = Frame(bottomFrame)
middleFrame.pack(side = LEFT)
sRightFrame = Frame(bottomFrame)
sRightFrame.pack(side = LEFT)
rightFrame = Frame(bottomFrame)
rightFrame.pack(side = LEFT)

currentSet = qList[num]

theQuestion = Label(topFrame, text= currentSet[0])
response1 = Label(leftFrame, text= currentSet[1])
response2 = Label(middleFrame, text= currentSet[2])
response3 = Label(rightFrame, text= currentSet[3])
spacer1 = Label(sLeftFrame, text= "          ")
spacer2 = Label(sRightFrame, text= "          ")
button1 = Button(leftFrame, text= "Response 1", command= resp1)
button2 = Button(middleFrame, text= "Response 2", command= resp2)
button3 = Button(rightFrame, text= "Response 3", command= resp3)
theQuestion.pack()
button1.pack(side = TOP)
button2.pack(side = TOP)
button3.pack(side = TOP)
response1.pack(side = BOTTOM)
spacer1.pack(side = BOTTOM)
response2.pack(side = BOTTOM)
spacer2.pack(side = BOTTOM)
response3.pack(side = BOTTOM)



root.mainloop()