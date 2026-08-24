from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .views import PROJECTS


class PortfolioSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        items = ["/", reverse("portfolio:homepage")]
        items += [reverse("portfolio:project_detail", args=[slug]) for slug in PROJECTS]
        return items

    def location(self, item):
        return item
