from core.models.pr import ContentPlan

class ContentPlanner:
    async def plan(self, diff, mappings, confidence) -> ContentPlan:
        return ContentPlan(action="update_block", target_page_id=mappings[0].page_id if mappings else None)