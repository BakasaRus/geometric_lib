def get_inaccuracy(value, expected):
    return abs(value - expected) / max(1, abs(expected))