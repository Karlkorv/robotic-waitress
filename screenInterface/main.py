import classes
import inputReader
import random


def printNodes():
    for key in nodes.keys():
        c = nodes.get(key)
        print("ID: " + c.ID + ", Text: " + c.Text +
              ", AnswText: " + c.AnswText + ", AnswID: " + c.AnswID)


def printOptions():
    for key in options.keys():
        o = options.get(key)
        print("ID: " + o.ID + ", Text: " + o.Text +
              ", ConvID: " + o.ConvID)


def printInput():
    print("-----Options")
    printOptions()
    print("-----Nodes")
    printNodes()


def getRandomintroNode():
    intros = []
    for key in nodes.keys():
        if int(key) < 1000 and int(key) > 100:
            intros.append(nodes.get(key))
    r = random.randrange(0, len(intros))
    return intros[r]


def introPhrase():
    print(getRandomintroNode().Text)


def displayOptions():
    for key in range(1, len(options) + 1):
        o = options.get(str(key))
        print(o.ID + ": " + o.Text),
    print("")


options = inputReader.readInputOptions('input.txt')
nodes = inputReader.readInputNodes('input.txt')

# printInput()

numOfOptions = len(options)
selected = False

introPhrase()
displayOptions()
while not selected:
    selection = input()
    if selection < 1 or selection > numOfOptions:
        print("Invalid Selection")
    else:
        nextNode = (options.get(str(selection))).ConvID
        print(nextNode)
