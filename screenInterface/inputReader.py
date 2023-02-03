import classes

# Reads input from filename, returns dictinoary of conversation nodes, with format {nodeID:convNode}


def readInputNodes(filename):
    file = open(filename, 'r')
    read = file.readlines()
    nodes = {}

    for line in read:
        currentLine = (line.strip()).split(" - ")
        if len(currentLine) > 1 and currentLine[0][0] != '%' and currentLine[0][0] != 'o' and currentLine[0][0] != 'i':
            # Turn Answers into a list of answers
            answText = currentLine[2].split(", ")
            #Turn AnswerIDs into a list if IDs
            answIDs = currentLine[3].split(", ")
            nodes.update({int(currentLine[0]): classes.convNode(currentLine[0], currentLine[1],
                                                                answText, answIDs)})
    return nodes


def readInputOptions(filename):
    file = open(filename, 'r')
    read = file.readlines()
    options = {}

    for line in read:
        currentLine = (line.strip()).split(" - ")
        if len(currentLine) > 1 and currentLine[0][0] == 'o':
            options.update({int(currentLine[1]): classes.option(
                currentLine[1], currentLine[2], currentLine[3])})
    return options


def readInputIntros(filename):
    file = open(filename, 'r')
    read = file.readlines()
    intros = {}

    for line in read:
        currentLine = (line.strip()).split(" - ")
        if len(currentLine) > 1 and currentLine[0][0] == 'i':
            intros.update({int(currentLine[1]): classes.intro(
                currentLine[1], currentLine[2])})
    return intros
