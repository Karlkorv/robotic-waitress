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


def getRandomintroNode(intros):
    r = random.randrange(1, len(intros) + 1)
    return intros.get(r)


def introPhrase(intros):
    print(getRandomintroNode(intros).Text)


def displayOptions(options, numOfOptions):
    for key in range(1, numOfOptions + 1):
        o = options.get(key)
        print(o.ID + ": " + o.Text),
    print("")
