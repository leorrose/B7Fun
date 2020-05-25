# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from django.urls import resolve, reverse
from adminStats.views import show_stats

@tag('unit-test')
class AdminStatsUrlsTest(TestCase):
    def test_show_stats_resolved_no_year(self):
        #Act
        url = reverse('adminStats:show_stats_no_year')
        #Assert
        self.assertEqual(resolve(url).func, show_stats)

    def test_show_stats_resolved(self):
        #Act
        url = reverse('adminStats:show_stats', kwargs={'year':2020})
        #Assert
        self.assertEqual(resolve(url).func, show_stats)
