import random
from rw_screen import classes


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


def get_options(options) -> classes.option:
    options = inputReader.readInputOptions('input.txt')
    return options


def printInput():
    print("-----Options")
    printOptions()
    print("-----Nodes")
    printNodes()


def getRandomintroNode(intros) -> classes.intro:
    r = random.randrange(1, len(intros) + 1)
    return intros.get(r)


def getRandomFarewell(farewells) -> classes.farewell:
    r = random.randrange(1, len(farewells) + 1)
    return farewells.get(r)

def getRandomConvStart(starts) -> classes.convStart:
    r = random.randrange(1, len(starts) + 1)
    return starts.get(r)

def get_node(nodes, nodeID):
    if nodeID == "[]":
        return None
    else:
        return nodes.get(nodeID)


def introPhrase(intros):
    print(getRandomintroNode(intros).Text)


def displayOptions(options, numOfOptions):
    for key in range(1, numOfOptions + 1):
        o = options.get(key)
        print(o.ID + ": " + o.Text),
    print("")
