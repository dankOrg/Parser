
class ReactionType():
    HEART="unicode"
    SMILE="unicode"
    OOH="unicode"
    SAD_TEAR="unicode"
    ANGRY="unicode"
    UPVOTE="unicode"
    DOWNVOTE="unicode"

    @staticmethod
    def parseReactionFromString(strToParse):
        # Write code to parse to Reaction From Sring
        return ReactionType.HEART