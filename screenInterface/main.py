import convNode
import inputReader


def printNodes():
    for key in nodes.keys():
        convNode = nodes.get(key)
        print("ID: " + convNode.ID + ", Text: " + convNode.Text +
              ", AnswText: " + convNode.AnswText + ", AnswID: " + convNode.AnswID)


nodes = inputReader.readInput('input.txt')

printNodes()
