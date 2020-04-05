class Group:
    def __init__(self, mesages, participants, title, thread_type, thread_path):
        self.participants = participants #Array of users
        self.title = title #Name of group shat
        self.thread_type = thread_type #RegularGroup or something else
        self.thread_path = thread_path #Name of the the chat folder in the inbox folder
        self.messages = messages