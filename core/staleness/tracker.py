from core.models.pr import PREvent

class StalenessTracker:
    async def update(self, page_id: str, pr_number: int):
        pass  # writes to Notion DB

    def generate_report(self, pr=None):
        return {"freshness_leaderboard": []}