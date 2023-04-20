from typing import List, Dict

def function(names: List[str]) -> Dict[str, int]:
    counts = {}
    for name in names:
        if name not in counts:
            counts[name] = 0
        counts[name] += 1
    return counts
