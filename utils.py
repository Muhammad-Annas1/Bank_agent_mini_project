# utils.py
import re

def input_guardrails(user_input: str):
    """Check input validity: not empty, not too short, and no long digit sequences (possible account numbers)."""
    s = (user_input or "").strip()
    if not s:
        return False, "Empty input"
    if len(s) < 3:
        return False, "Too short"
    if re.search(r"\d{6,}", s):
        return False, "Contains long digit sequence (possible account number)"
    return True, None

def mask_digits(text: str):
    """Mask any digit sequences length >=4 with asterisks to avoid leaking PII."""
    return re.sub(r"\d{4,}", lambda m: "*" * len(m.group(0)), text)

def output_guardrails(raw_text: str, max_len: int = 250):
    """Sanitize model output: mask digits, trim length, remove excessive whitespace."""
    if raw_text is None:
        return "Sorry, I couldn't fetch information right now."
    text = str(raw_text).strip()
    text = mask_digits(text)
    # normalize spaces
    text = " ".join(text.split())
    if len(text) > max_len:
        text = text[:max_len].rstrip() + "..."
    return text
