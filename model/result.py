from model.metric import Metric

class Result:
    def __init__(self, description, response_time, status_code, metric = Metric(), error=""):
        self.description = description
        self.status_code = status_code
        self.metric = metric
        self.response_time = response_time
        self.error = error

    def get_metric_caution(self):
        return self.metric.get_caution_level(self.response_time)

    def assert_status_code(self):
        return self.metric.is_expected_status_code(self.status_code)
    
    def get_formatted_response_time(self):
        return "{0:.2f}{1}".format(self.response_time, self.metric.get_unit())
    
    def is_error(self) -> bool:
        return self.status_code >= 400
