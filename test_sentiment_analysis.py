from SentimentAnalysis.sentiment_analysis import sentiment_analyzer 
import unittest 

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        self.assertEqual(sentiment_analyzer('i love working with python')['label'], 'SENT_POSITIVE')
        self.assertEqual(sentiment_analyzer('i hate working with python')['label'], 'SENT_NEGATIVE')
        self.assertEqual(sentiment_analyzer('i am neutral on python')['label'], 'SENT_NEUTRAL')


unittest.main()