from User import User
from Photo import Photo
from Reaction import Reaction

class Message:
    
    def __init__(self, sender_name, timestamp_ms, photos, reactions, type):
        self.user =  User(sender_name)
        self.timestamp_ms = timestamp_ms

        self.photosArr = [] 
        for photo in photos:
            self.photosArr.append(Photo(photo['uri'], photo['creation_timestamp']))

        self.photos = self.photosArr

        self.reactionArr = []
        for reaction in reactions:
            self.reactionArr.append(Reaction(reaction['reaction'], reaction['actor']))

        self.reactions = self.reactionArr
        
