from core.models.pr import ProcessedDiff, NotionMapping
from core.notion.client import MCPClient
from utils.logging import logger

class PageResolver:
    async def resolve(self, diff: ProcessedDiff) -> list[NotionMapping]:
        if not diff.architecture_components:
            return []
        client = MCPClient()
        query = " ".join(diff.architecture_components[:3])
        logger.info(f"[PageResolver] Searching Notion for: {query}")
        results = await client.search_pages(query)
        return [
            NotionMapping(
                page_id=r["id"],
                title=r["title"],
                relevance_score=0.9,
                match_reason=f"Matched query: {query}"
            )
            for r in results
        ]
