"""Ticker extraction from social media headlines and comments."""

import re
from typing import List

TICKER_STOPWORDS = {'THE', 'AND', 'FOR', 'YOLO', 'FOMO', 'IMO', 'USA', 'CEO', 'DD', 'EPS'}
CASHTAG_RE = re.compile(r'\$([A-Z]{1,5})\b')


def extract_tickers(text: str) -> List[str]:
    found = []
    for match in CASHTAG_RE.findall(text.upper()):
        if match not in TICKER_STOPWORDS:
            found.append(match)
    return found
