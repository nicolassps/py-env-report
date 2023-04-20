import typing
from model.health_check_request import HealthCheckRequest
from provider.health_check_request_provider import HealthCheckRequestProvider
from file.xml_reader import XmlReader
from enumeration.http_method import HttpMethod

class HealthCheckRequestXmlProvider(HealthCheckRequestProvider):
    def __init__(self):
        pass

    def retrieve_all(self) -> typing.List[HealthCheckRequest]:
        xml_reader = XmlReader('resources/requests.xml')

        requests = xml_reader.read_child('request', 
                                         ['description', 'url', 'type', 'method', 'body'], 
                                         ['Content-Type', 'SOAPAction', 'Authorization'], 
                                         ['description', 'url', 'type'])

        return list(map(self.__convert_to_health_check_request, requests))
    
    def __convert_to_health_check_request(self, request):
        return HealthCheckRequest(request.get('description'),
                                  request.get('url'), 
                                  request.get('type'), 
                                  request.get('protocol'), 
                                  request.get('body'),
                                  HttpMethod[self.__get_or_default(request, 'method', 'GET')],
                                  request.get('attributes'))
    
    def __get_or_default(self, dict_, key, default):
        return dict_.get(key) if dict_.get(key) is not None else default