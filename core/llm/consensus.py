class ConsensusEngine:
    def vote(self, results):
        # Simple majority vote for confidence boost
        return max(set(results), key=results.count) if results else None