from django.test import TestCase
from django.core.urlresolvers import reverse
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

	def test_homepage(self):
		"""
		homepage exists and contains a form
		"""
		response = self.client.get(reverse("home"))
		self.assertEqual(response.status_code, 200)
		self.assertIn("form", response.context)