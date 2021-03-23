"""Aggregate ticker mentions and upvote-weighted sentiment scores."""

import math
from collections import defaultdict
from typing import Any, Dict, List

from extractor import extract_tickers
from sentiment import score_text


def rank_tickers(posts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    stats: Dict[str, Dict[str, float]] = defaultdict(lambda: {'mentions': 0, 'hype': 0.0, 'sentiment': 0.0})
    for post in posts:
        title = post.get('title', '')
        weight = math.log1p(max(0, int(post.get('upvotes', 1))))
        sent = score_text(title)
        for ticker in set(extract_tickers(title)):
            stats[ticker]['mentions'] += 1
            stats[ticker]['hype'] += weight
            stats[ticker]['sentiment'] += sent
    ranked = []
    for ticker, s in stats.items():
        avg_sent = round(s['sentiment'] / s['mentions'], 3)
        ranked.append({
            'ticker': ticker,
            'mentions': int(s['mentions']),
            'hype_score': round(s['hype'], 2),
            'avg_sentiment': avg_sent,
        })
    return sorted(ranked, key=lambda item: item['hype_score'], reverse=True)
