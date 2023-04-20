from enum import Enum

class Protocol(Enum):
    HTTPS = ('https://')
    HTTP = ('http://')

    def __init__(self, uri):
        self.uri = uri