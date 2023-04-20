from provider.health_check_request_provider import HealthCheckRequestProvider
from strategy.method_factory import execute
import typing
from model.result import Result

class EnvironmentExecutor:
    def __init__(self, provider: HealthCheckRequestProvider):
        self.provider = provider

    def execute(self) -> typing.List[Result]:
        results = []

        for request in self.provider.retrieve_all():
            result = execute(request=request)
            results.append(result)

        return results