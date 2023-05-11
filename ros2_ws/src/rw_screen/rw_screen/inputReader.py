from rw_screen import classes
import string


def readInputNodes(path):
    """
    Creates a dictionary of all the conversation nodes in the input file.
    The Key is the node's ID, the Value is a convNode object: {ID:convNode}
    """
    file = open(path + "input.txt", 'r')
    read = file.readlines()
    nodes = {}

    for line in read:
        currentLine = (line.strip()).split(" - ")
        if len(currentLine) > 1 and (currentLine[0][0]).isnumeric():
            # Turn Answers into a list of answers
            answText = currentLine[2].split("| ")
            # Turn AnswerIDs into a list if IDs
            answIDs = currentLine[3].split("| ")
            nodes.update({int(currentLine[0]): classes.convNode(currentLine[0],  split_long_sentence(currentLine[1]), currentLine[1],
                                                                answText, answIDs, path + "animations/" + currentLine[4] + ".mp4")})
    file.close()
    return nodes

def readInputConvStarts(path):
    """
    Creates a dictionary of all the conversation nodes in the input file.
    The Key is the node's ID, the Value is a convNode object: {ID:convNode}
    """
    file = open(path + "input.txt", 'r')
    read = file.readlines()
    convStarts = {}

    counter = 1
    for line in read:
        currentLine = (line.strip()).split(" - ")
        if len(currentLine) > 1 and currentLine[0][0] == 'c':
            # Turn Answers into a list of answers
            answText = currentLine[2].split("| ")
            # Turn AnswerIDs into a list if IDs
            answIDs = currentLine[3].split("| ")
            convStarts.update({counter : classes.convStart(counter,  split_long_sentence(currentLine[1]), currentLine[1],
                                                                answText, answIDs, path + "animations/" + currentLine[4] + ".mp4")})
            counter += 1
    file.close()
    return convStarts

def readInputOptions(path):
    """
    Creates a dictionary of all the conversation options in the input file.
    The Key is the option's ID, the Value is a option object: {ID:option}
    """
    file = open(path + "input.txt", 'r')
    read = file.readlines()
    options = {}

    for line in read:
        currentLine = (line.strip()).split(" - ")
        if len(currentLine) > 1 and currentLine[0][0] == 'o':
            options.update({int(currentLine[1]): classes.option(
                currentLine[1], currentLine[2], currentLine[3])})
    file.close()
    return options


def readInputIntros(path):
    """
    Creates a dictionary of all the intro phrases in the input file.
    The Key is the intro's ID, the Value is a intro object: {ID:intro}
    """
    file = open(path + "input.txt", 'r')
    read = file.readlines()
    intros = {}

    for line in read:
        currentLine = (line.strip()).split(" - ")
        if len(currentLine) > 1 and currentLine[0][0] == 'i':
            intros.update({int(currentLine[1]): classes.intro(
                currentLine[1], split_long_sentence(currentLine[2]))})
    file.close()
    return intros


def readInputFarewells(path):
    """
    Creates a dictionary of all the farewell phrases in the input file.
    The Key is the farewell's ID, the Value is a farewell object: {ID:farewell}
    """
    file = open(path + "input.txt", 'r')
    read = file.readlines()
    farewells = {}

    for line in read:
        currentLine = (line.strip()).split(" - ")
        if len(currentLine) > 1 and currentLine[0][0] == 'f':
            farewells.update({int(currentLine[1]): classes.farewell(
                currentLine[1],  split_long_sentence(currentLine[2]))})
    file.close()
    return farewells



def split_long_sentence(sentence):
    if len(sentence) <= 30:
        return sentence
    else:
        last_space_index = sentence.rfind(' ', 0, 30)
        if last_space_index == -1:
            last_space_index = 30
        return sentence[:last_space_index].strip() + '\n' + split_long_sentence(sentence[last_space_index:].strip())