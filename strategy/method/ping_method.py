from strategy.method_strategy import Strategy
from model.result import Result
from pythonping import ping
from model.health_check_request import HealthCheckRequest

class Ping(Strategy):
    def execute(self, request: HealthCheckRequest) -> Result:
        responses = ping(request.url, verbose=True)._responses

        response = next(iter(responses))
        milliseconds = round(response.time_elapsed * 1000, 2)

        return Result(request.description, milliseconds, 200)