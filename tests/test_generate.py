import unittest
from generate import BANK, generate

class WorksheetTests(unittest.TestCase):
    def test_all_topics_and_answer_keys(self):
        for topic, bank in BANK.items():
            output = generate(topic, len(bank))
            for word, meaning in bank:
                self.assertIn(meaning, output)
                self.assertIn(f'<li>{word} —', output)
            self.assertEqual(output.count('<li>'), 2 * len(bank))

    def test_validation_and_escape(self):
        for count in (0, -1, 99):
            with self.assertRaises(ValueError):
                generate(count=count)
        self.assertIn('&lt;script&gt;', generate(title='<script>'))
        self.assertEqual(generate(seed=8), generate(seed=8))

if __name__ == '__main__':
    unittest.main()
