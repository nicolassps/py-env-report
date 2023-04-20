from enumeration.caution_level import CautionLevel
from util.numeric import percentage

class Metric:
    UNIT = "ms"

    def __init__(self, expected_status_code=200, response_time_base_value=50):
        self.response_time_base_value = response_time_base_value
        self.expected_status_code = expected_status_code

    def get_caution_level(self, metric_value):
        percent_metric = percentage(metric_value, self.response_time_base_value)

        if (percent_metric < 20):
            return CautionLevel.LOW
        elif (percent_metric < 50):
            return CautionLevel.MEDIUM

        return CautionLevel.HIGH

    def is_expected_status_code(self, status_code):
        return self.expected_status_code == status_code
    
    def get_unit(self):
        return self.UNIT