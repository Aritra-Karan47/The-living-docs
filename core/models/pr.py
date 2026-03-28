import hashlib
from typing import Literal
from pydantic import BaseModel, Field

class PREvent(BaseModel):
    pr_number: int
    repo: str
    action: Literal["opened", "synchronize", "closed"]
    author: str
    diff: str = ""
    description: str | None = None
    diff_hash: str = ""

class ProcessedDiff(BaseModel):
    files: list[str]
    impacted_modules: list[str]
    architecture_components: list[str]

class NotionMapping(BaseModel):
    page_id: str
    title: str
    relevance_score: float
    match_reason: str = ""

class ConfidenceReport(BaseModel):
    score: int
    factors: dict[str, float] = {}
    explanation: str = ""

class ContentPlan(BaseModel):
    action: Literal["update_block", "append_block", "create_page", "flag_review"]
    target_page_id: str | None = None
    blocks: list[dict] | None = None
    new_page_title: str | None = None
    reason: str = ""
