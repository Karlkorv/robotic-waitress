# The conversation node class - representing a stage in a conversation
class convNode:
    def __init__(self, ID, Text, AnswText, AnswID):
        self.ID = ID
        self.Text = Text
        self.AnswText = AnswText
        self.AnswID = AnswID


class option:
    def __init__(self, ID, Text, ConvID):
        self.ID = ID
        self.Text = Text
        self.ConvID = ConvID
