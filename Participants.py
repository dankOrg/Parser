from User import User

class Participants:

    
    def __init__(self, nameArr):
        
        self.participants = []
        for name in nameArr:
            self.participants.append(User(name))
