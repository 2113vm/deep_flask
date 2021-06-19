from typing import Any


class DummyModel:
    def __init__(self, config: dict = None):
        self.config = config or {}

    def predict(self, data: Any) -> Any:
        print(f"Got {data}")
        return data
