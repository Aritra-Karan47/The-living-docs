import re
from unidiff import PatchSet
from core.models.pr import ProcessedDiff

class DiffPreprocessor:
    def process(self, diff_text: str) -> ProcessedDiff:
        patch = PatchSet(diff_text)
        files = []
        for patched_file in patch:
            if any(x in patched_file.path for x in ["tests/", "__tests__", ".lock", "generated"]):
                continue
            files.append(patched_file.path)
        
        # Simple module extraction
        modules = list(set(f.split('/')[0] for f in files if '/' in f))
        return ProcessedDiff(
            files=files,
            impacted_modules=modules,
            architecture_components=modules  # can be enhanced with mapper.py
        )