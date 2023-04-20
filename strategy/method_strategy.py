from abc import ABC, abstractmethod
from model.result import Result
from model.health_check_request import HealthCheckRequest

class Strategy(ABC):
    @abstractmethod
    def execute(self, request: HealthCheckRequest) -> Result:
        pass