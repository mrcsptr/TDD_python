# coding: utf-8

import unittest
from mycode import *


class MyFirstTests(unittest.TestCase):

	def testJo(self):
		self.assertEqual(score_calc('Joseph', 15), '66%')

	def testMarie(self):
		self.assertEqual(score_calc('Marie', 33), '50%')

	def testMarc(self):
		self.assertEqual(score_calc('Marc', 60), '43%')

	def testEly(self):
		self.assertEqual(score_calc('Ely', 28), '75%')





