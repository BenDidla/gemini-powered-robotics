# tests/test_gemini_response.py

import unittest
from nlp_interface.gemini_client import GeminiClient

class TestGeminiClient(unittest.TestCase):

    def setUp(self):
        self.gemini = GeminiClient()

    def test_ask_gemini(self):
        response = self.gemini.ask_gemini("Say hello")
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

if __name__ == '__main__':
    unittest.main()

