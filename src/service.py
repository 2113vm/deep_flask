from typing import Any

from src.model import DummyModel


class Service:
    def __init__(self, config: dict = None):
        self.config = config or {}
        self.model = DummyModel(config.get("model"))
        print(f"Run {self.config.get('name')} service")

    def business_pipeline(self, data: Any) -> Any:
        return f"Got message {self.model.predict(data)}"
