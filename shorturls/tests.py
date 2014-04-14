from django.test import TestCase
from .models import Link

class ShortenerText(TestCase):
	def test_shortens(self):
		"""
		URLs get shorter
		"""
		url = "http://example.com"
		l = Link(url=url)
		short_url = Link.shorten(l)
		self.assertLess(len(short_url), len(url))

	def test_recover_link(self):
		"""
		expanded short link is the same as original
		"""
		url = "http://example.com"
		l = Link(url=url)
		short_url = Link.shorten(l)
		l.save()
		exp_url = Link.expand(short_url)
		self.assertEqual(url, exp_url)
