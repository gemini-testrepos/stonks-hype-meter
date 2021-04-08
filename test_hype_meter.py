import unittest
from analyzer import rank_tickers
from extractor import extract_tickers


class TestHypeMeter(unittest.TestCase):
    def test_extract_filters_stopwords(self):
        self.assertEqual(extract_tickers('$GME and $YOLO on $AMC'), ['GME', 'AMC'])

    def test_rank_orders_by_hype(self):
        posts = [
            {'title': '$GME to the moon', 'upvotes': 5000},
            {'title': '$AMD solid growth', 'upvotes': 100},
        ]
        ranked = rank_tickers(posts)
        self.assertEqual(ranked[0]['ticker'], 'GME')
