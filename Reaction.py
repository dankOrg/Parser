from ReactionType import ReactionType 
from User import User
class Reaction:
    def __init__(self, reaction, actor):
        self.reactionType = ReactionType.parseReactionFromString(reaction)
        self.user = User(actor)


    


