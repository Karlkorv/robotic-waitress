class convNode:
    """The conversation node class - representing a stage in a conversation

    Defined by it's ID. Stores the text the robot should "say",
    the text each button should read, and to what node each button is linked to"""

    def __init__(self, ID, Text, NoSplitText, AnswText, AnswID, Animation):
        self.ID = ID
        self.Text = Text
        self.NoSplitText = NoSplitText
        self.AnswText = AnswText
        self.AnswID = AnswID
        self.Animation = Animation

class convStart:
    """The conversation node class - representing a stage in a conversation

    Defined by it's ID. Stores the text the robot should "say",
    the text each button should read, and to what node each button is linked to"""

    def __init__(self, ID, Text, NoSplitText, AnswText, AnswID, Animation):
        self.ID = ID
        self.Text = Text
        self.NoSplitText = NoSplitText
        self.AnswText = AnswText
        self.AnswID = AnswID
        self.Animation = Animation


class option:
    """The option class - representing the conversation options at the start of a new interaction

    Defined by it's ID. Stores the text each button should read, and to what node each button is linked to"""

    def __init__(self, ID, Text, ButtonAnswID):
        self.ID = ID
        self.Text = Text
        self.ButtonAnswID = ButtonAnswID


class intro:
    """The intro class - representing the random introphrases the robot says at a new interaction"""

    def __init__(self, ID, Text):
        self.ID = ID
        self.Text = Text


class farewell:
    """The farewell class - representing the random farewell phrases the robot says at the end of a interaction"""

    def __init__(self, ID, Text):
        self.ID = ID
        self.Text = Text
