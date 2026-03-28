from core.config import settings

class DecisionGate:
    def evaluate(self, score: int) -> str:
        if score >= settings.confidence_threshold:
            return "auto_write"
        elif score >= 50:
            return "create_page"
        return "flag_review"