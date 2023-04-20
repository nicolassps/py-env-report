from abc import ABC, abstractmethod
import typing
from model.health_check_request import HealthCheckRequest

class HealthCheckRequestProvider(ABC):
    @abstractmethod
    def retrieve_all(self) -> typing.List[HealthCheckRequest]:
        pass