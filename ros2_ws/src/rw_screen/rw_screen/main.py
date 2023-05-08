import classes
import inputReader
import functions

intros = inputReader.readInputIntros('input.txt')
options = inputReader.readInputOptions('input.txt')
nodes = inputReader.readInputNodes('input.txt')
convStarts = inputReader.readInputConvStarts('input.txt')


# printInput()

numOfOptions = len(options)
selected = False

functions.introPhrase(intros)
functions.displayOptions(options, numOfOptions)
while not selected:
    selection = input()
    if selection < 1 or selection > numOfOptions:
        print("Invalid Selection")
    else:
        nextNode = (options.get(selection)).ConvID
        print(nextNode)
