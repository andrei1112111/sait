from abc import ABC, abstractmethod


class BaseSession(ABC):
    @abstractmethod
    async def get_streaming_response(self, prompt: str):
        pass
