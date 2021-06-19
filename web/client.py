from flask import Flask

from src.service import Service
from .endpoints import (
    RecognitionEndpoint,
    HealthCheckEndpoint,
)


class FlaskApplication(Flask):
    def __init__(
        self,
        recognition_service: Service,
    ):
        super().__init__(__name__)
        self.recognition_service = recognition_service
        self._add_all_routes()

    def _add_all_routes(self):
        # add a recognition endpoint
        self.add_url_rule(
            "/recognize",
            "recognize",
            RecognitionEndpoint(self.recognition_service),
            methods=["POST"],
        )
        # add a healthcheck endpoint
        self.add_url_rule(
            "/healthcheck",
            "healthcheck",
            HealthCheckEndpoint(),
            methods=["GET"],
        )
