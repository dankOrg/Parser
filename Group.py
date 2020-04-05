from Participants import Participants
from Message import Message

class Group:
    
    def __init__(self, participants, messages, title, is_still_participant, thread_type, thread_path):
        self.participants = Participants(participants) #Array of users
        
        self.messagesArr = []
        for message in messages:
            #IGNORING CONTENT
            if('photos' in message and 'reactions' in message):
                self.messagesArr.append(Message(message['sender_name'], message['timestamp_ms']
                , message['photos'], message['reactions'], message['type']))  

        self.messages = self.messagesArr
        self.title = title #Name of group shat
        self.is_still_participant = is_still_participant
        self.thread_type = thread_type #RegularGroup or something else
        self.thread_path = thread_path #Name of the the chat folder in the inbox folder
        