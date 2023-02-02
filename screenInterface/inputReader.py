import classes

# Reads input from filename, returns dictinoary of conversation nodes, with format {nodeID:convNode}


def readInputNodes(filename):
    file = open(filename, 'r')
    read = file.readlines()
    nodes = {}

    for line in read:
        currentLine = (line.strip()).split(" - ")
        if len(currentLine) > 1 and currentLine[0][0] != '%' and currentLine[0][0] != 'o':
            nodes.update({currentLine[0]: classes.convNode(currentLine[0], currentLine[1],
                                                           currentLine[2], currentLine[3])})
    return nodes


def readInputOptions(filename):
    file = open(filename, 'r')
    read = file.readlines()
    options = {}

    for line in read:
        currentLine = (line.strip()).split(" - ")
        if len(currentLine) > 1 and currentLine[0][0] == 'o':
            options.update({currentLine[1]: classes.option(
                currentLine[1], currentLine[2], currentLine[3])})
    return options
