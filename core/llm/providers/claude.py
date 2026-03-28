import anthropic
from core.llm.base import LLMAdapter
from core.config import settings
from pydantic import BaseModel

class ClaudeAdapter(LLMAdapter):
    async def generate_structured(self, prompt: str, output_schema: type[BaseModel]):
        client = anthropic.Anthropic(api_key=settings.anthropic_api_key)
        # Real call would use tools/structured output - placeholder for brevity
        return output_schema(score=85, explanation="Claude analysis")