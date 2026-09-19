from .base_session import BaseSession


class FMSession(BaseSession):
    def __init__(self, session) -> None:
        self.session = session

    async def get_streaming_response(self, prompt: str): # type: ignore
        try:
            async for chunk in self.session.stream_response(prompt):
                yield chunk
        except Exception as e:  # noqa: BLE001
            raise RuntimeError(f"streaming error: {e}")


class MacOS27Plus:
    def __init__(self) -> None:
        import apple_fm_sdk as fm
        self.fm = fm

        # Get the default system foundation model
        self.model = fm.SystemLanguageModel()

        # Check if the model is available
        is_available, reason = self.model.is_available()
        if not is_available:
            raise ConnectionError(f"MacOS27Plus FoundationModel: {reason}")

    def make_session(self, system: str, tools):
        is_available, _ = self.model.is_available()
        if not is_available:
            raise ConnectionError("model is not responding")

        # [в работе] здесь можно передать системный промпт и список тулзов
        session = self.fm.LanguageModelSession(
            instructions=system,
            model=self.model,
            tools=None
        )

        return FMSession(session)
