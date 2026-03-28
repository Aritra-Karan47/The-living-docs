# core/llm/base.py
from abc import ABC, abstractmethod
from typing import Any, Protocol

class LLMAdapter(Protocol):
    async def generate_structured(
        self,
        prompt: str,
        output_schema: type[BaseModel],
        temperature: float = 0.0,
        model: str | None = None
    ) -> BaseModel: ...

    async def generate_raw(self, prompt: str) -> str: ...