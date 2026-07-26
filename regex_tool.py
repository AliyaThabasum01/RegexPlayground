import re

def find_matches(pattern, text):
    try:
        return re.findall(pattern, text)
    except re.error as e:
        print(f"Invalid regex: {e}")
        return []
