import asyncio
from core.llm.router import LLMRouter

class ParallelExecutor:
    async def run_multiple(self, prompts: list, schema):
        router = LLMRouter()
        tasks = [router.get_adapter().generate_structured(p, schema) for p in prompts]
        return await asyncio.gather(*tasks, return_exceptions=True)