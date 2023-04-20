from abc import ABC, abstractmethod
from model.health_check_request import HealthCheckRequest

class HealthCheckRequestAdapter(ABC):
    @abstractmethod
    def convert_to_health_check_request(self, request: dict) -> HealthCheckRequest:
        pass

