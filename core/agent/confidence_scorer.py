from core.models.pr import ConfidenceReport, ProcessedDiff

class ConfidenceScorer:
    async def score(self, diff: ProcessedDiff, mappings) -> ConfidenceReport:
        score = 85 if mappings else 40
        return ConfidenceReport(score=score, explanation="Based on module-to-page mapping match")
