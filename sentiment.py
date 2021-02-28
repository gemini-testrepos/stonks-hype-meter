"""Domain-adapted lexicon sentiment scorer for retail stock chatter."""

import re

BULLISH_TERMS = {
    'moon': 1.5, 'bullish': 1.4, 'diamond': 1.2, 'breakout': 1.2,
    'surge': 1.1, 'solid': 0.8, 'growth': 0.9, 'holding': 0.7, 'strong': 0.9,
}
BEARISH_TERMS = {
    'crash': -1.6, 'bearish': -1.4, 'dump': -1.3, 'overvalued': -1.1,
    'volatility': -0.6, 'risk': -0.5, 'concerned': -0.7, 'sell': -0.8,
}


def score_text(text: str) -> float:
    tokens = re.findall(r'[a-z]+', text.lower())
    if not tokens:
        return 0.0
    total = sum(BULLISH_TERMS.get(t, 0.0) + BEARISH_TERMS.get(t, 0.0) for t in tokens)
    return round(max(-5.0, min(5.0, total)), 3)
