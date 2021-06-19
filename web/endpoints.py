from abc import abstractmethod

from flask import Response, request

from src.service import Service


class BaseEndpoint:
    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class RecognitionEndpoint(BaseEndpoint):
    def __init__(self, recognition_service: Service):
        self.recognition_service = recognition_service

    def __call__(self, *args, **kwargs):
        return self.recognition_service.business_pipeline(data=request.data)


class HealthCheckEndpoint(BaseEndpoint):
    def __call__(self, *args, **kwargs):
        return Response(status=200)
