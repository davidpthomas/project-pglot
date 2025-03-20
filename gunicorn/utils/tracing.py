import logging
import uuid

class RequestTracer:
    def __init__(self):
        self.logger = logging.getLogger("RequestTracer")
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(request_id)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def generate_request_id(self):
        return str(uuid.uuid4())

    def log_with_request_id(self, message, request_id=None):
        if request_id is None:
            request_id = self.generate_request_id()
        extra = {'request_id': request_id}
        self.logger.info(message, extra=extra)

# Example usage
if __name__ == "__main__":
    tracer = RequestTracer()
    request_id = tracer.generate_request_id()
    tracer.log_with_request_id("Starting process", request_id)
    tracer.log_with_request_id("Process completed", request_id)