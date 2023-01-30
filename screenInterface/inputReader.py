import convNode

# Reads input from filename, returns dictinoary of conversation nodes, with format {nodeID:convNode}


def readInput(filename):
    file = open(filename, 'r')
    read = file.readlines()
    nodes = {}

    for line in read:
        currentLine = (line.strip()).split(" - ")
        if len(currentLine) > 1:
            nodes.update({currentLine[0]: convNode.convNode(currentLine[0], currentLine[1],
                                                            currentLine[2], currentLine[3])})
    return nodes
