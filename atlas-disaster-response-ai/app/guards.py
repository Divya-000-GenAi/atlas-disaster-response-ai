import re
BAD=[r"ignore (all |the )?(previous|system) instructions",r"reveal (your |the )?(api key|secret|system prompt)",r"disable (safety|guardrails)"]
def validate_prompt(text):
    return not any(re.search(pattern,text,re.I) for pattern in BAD)
def safe_excerpt(text,limit=380):
    return re.sub(r"(?i)(api[_ -]?key|password)\s*[:=]\s*\S+",r"\1=[REDACTED]",text[:limit])
