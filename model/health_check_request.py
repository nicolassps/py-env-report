from enumeration.http_method import HttpMethod
from enumeration.protocol import Protocol

class HealthCheckRequest:
    
    def __init__(self, description, url, type, body, protocol, method, header):

        if not method: method = HttpMethod.GET
        if not protocol: protocol = Protocol.HTTPS
        if bool(header): header = {'Content-Type': 'application/json'}

        if (method in [HttpMethod.POST, HttpMethod.PUT]) and (not body or not header.get('Content-Type', None)):
            raise Exception("Invalid request, method is POST or PUT and body or content-type is Empty ")

        self.description = description
        self.url = url
        self.type = type
        self.protocol = protocol
        self.body = body
        self.method = method
        self.header = header