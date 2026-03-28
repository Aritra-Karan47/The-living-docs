import hashlib

def compute_diff_hash(diff: str) -> str:
    return hashlib.sha256(diff.encode()).hexdigest()
