from tkinter import *
num = 0

QA1 = ["You hate cats. Like hate hate them. Someone is telling you about how much you love cats and ask you what you think of cats. How do you respond?", "I hate cats.", "I'm more of a dog person but I still like cats.", "I love cats!"]
QA2 = ["You and your'e friend are in a debate about politics. You tell him a fact is wrong and you decide to look it up as proof. You end up being right. You say:", "Ha I told you so.", "Yeah I read about this last week.", "I wasn't sure either."]
QA3 = ["You LOVE Juicy Fruit Gum. You take out your gum in class and an classmate next to you asks for a peice.", "Don't give him one.", "Give him one as long as it's not the last peice.", "Give him one."]
QA4 = ["If you had the choice between these super powers you would choose:", "invisibility", "mind-reading", "telekenis"]
QA5 = ["It's saturday night. Choose between the following:", "Hang out with your best friend", "Watch a movie with 4 friends", "Go to a giant house party"]
QA6 = ["What is most important in high school", "Makin Paper", "Good grades", "Fun"]
QA7 = ["What is the best university", "Harvard", "Stanford", "MIT"]
QA8 = ["What is the best girl to guy ratio at a party", "30%", "50%", "70%"]
QA9 = ["What is the best color", "Blue", "Red", "Thats a lame question"]
QA10 = ["Out of the following you would rather do:", "Surfing", "Minecraft Bed Wars", "Gardening"]
Q11 = ["You are talking with your friend about which of the following:", "Girls/boys", "Politics/Philosophy", "School"]
QA12 = ["You listen to:", "Rap", "Country", "Classic Rock"]
QA13 = ["This quiz is", "Awesome", "Okay", "Dumb"]

qList = [QA1, QA2, QA3]
currentSet = qList[num]
root = Tk()
root.geometry("1000x100+200+300")

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
    global currentSet
    global qList
    num += 1
    currentSet = qList[num]
    theQuestion.set(currentSet[0])
    response1.set(currentSet[1])
    response2.set(currentSet[2])
    response3.set(currentSet[3])


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

spacer1 = Label(sLeftFrame, text="          ")
spacer2 = Label(sRightFrame, text="          ")

theQuestion = StringVar()
Label(topFrame, textvariable=theQuestion).pack()
theQuestion.set(currentSet[0])

response1 = StringVar()
Label(leftFrame, textvariable=response1).pack(side = BOTTOM)
response1.set(currentSet[1])

spacer1.pack(side = BOTTOM)

response2 = StringVar()
Label(middleFrame, textvariable=response2).pack(side = BOTTOM)
response2.set(currentSet[2])

spacer2.pack(side = BOTTOM)

response3 = StringVar()
Label(rightFrame, textvariable=response3).pack(side = BOTTOM)
response3.set(currentSet[3])

button1 = Button(leftFrame, text="Response 1", command= resp1)
button2 = Button(middleFrame, text="Response 2", command= resp2)
button3 = Button(rightFrame, text="Response 3", command= resp3)
button1.pack(side = TOP)
button2.pack(side = TOP)
button3.pack(side = TOP)
root.mainloop()