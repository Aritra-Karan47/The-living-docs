from core.llm.providers.claude import ClaudeAdapter
from core.llm.providers.openai import OpenAIAdapter
from core.llm.providers.gemini import GeminiAdapter
from core.config import settings

class LLMRouter:
    def get_adapter(self, complexity: str = "normal"):
        if settings.anthropic_api_key:
            return ClaudeAdapter()
        if settings.gemini_api_key:
            return GeminiAdapter()
        if settings.openai_api_key:
            return OpenAIAdapter()
        raise RuntimeError(
            "No LLM API key found. Set GEMINI_API_KEY in your .env file."
        )
