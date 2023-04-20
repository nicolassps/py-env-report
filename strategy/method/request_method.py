from enumeration.http_method import HttpMethod
from strategy.method_strategy import Strategy
from model.result import Result
import requests 
from requests.exceptions import SSLError
from model.health_check_request import HealthCheckRequest

class Request(Strategy):
    def execute(self, request: HealthCheckRequest) -> Result:
        try:
            if(request.method in [HttpMethod.POST, HttpMethod.PUT, HttpMethod.DELETE]):
                response = requests.post(request.protocol.uri + request.url, data=request.body)
            else:
                response = requests.get(request.protocol.uri + request.url)    
            
            milliseconds = round(response.elapsed.total_seconds() * 1000, 2)
            return Result(request.description, milliseconds, response.status_code)
        except SSLError as error:
            return Result(request.description, 0, 503, error="SSLError ocurred") 
        except Exception as error:
            return Result(request.description, 0, 500, error="Unknown error ocurred")