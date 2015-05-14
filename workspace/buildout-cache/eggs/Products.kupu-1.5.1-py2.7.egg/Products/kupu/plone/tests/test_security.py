import unittest
from Products.kupu.python.spellcheck import SpellChecker


class MockSpellChecker(SpellChecker):

	def __init__(self):
		self.lines = []

	def __del__(self):
		pass

	def write_line(self, line):
		self.lines.append(line)

	def read_line(self):
		return ''


class TestAttackVector(unittest.TestCase):
    
    def test_spellcheck_input_is_sanitized(self):
        checker = MockSpellChecker()
        checker.check('*foo')
        self.assertEqual(['^*foo'], checker.lines)
