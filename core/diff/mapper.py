from core.models.pr import ProcessedDiff

class ArchitectureMapper:
    def map(self, processed_diff: ProcessedDiff) -> ProcessedDiff:
        # Load from architecture_map.yaml in production
        return processed_diff  # placeholder