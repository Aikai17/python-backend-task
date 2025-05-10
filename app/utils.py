import hashlib

def generate_short_url(url: str) -> str:
    return hashlib.sha256(str(url).encode()).hexdigest()[:8]