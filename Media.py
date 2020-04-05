from MediaType import MediaType

class Media:
    def __init__(self, timestamp, mediaData):
        self.timestamp = timestamp
        self.mediaData = mediaData
        self.mediaType = MediaType.parseMediaFromString(mediaData)
