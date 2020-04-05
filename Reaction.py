from ReactionType import ReactionType 
from User import User
class Reaction:
    def __init__(self, reaction, actor):
        self.reactionType = ReactionType.HEART
        self.user = User(actor)

    def parseReactionToString(self, jsonString):
        # Write code to parse
        pass

    


