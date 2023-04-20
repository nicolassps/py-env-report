from model.health_check_request import HealthCheckRequest
from model.result import Result
from strategy.method.request_method import Request
from strategy.method.ping_method import Ping

def execute(request: HealthCheckRequest) -> Result:
    if(request.type == 'request'):
        return Request().execute(request=request)
    
    return Ping().execute(request=request)    