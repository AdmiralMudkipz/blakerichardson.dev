from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class CampaignSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return [
            ("/", 1.0),
            (reverse("campaign:homepage"), 0.8),
            (reverse("campaign:about"), 0.7),
            (reverse("campaign:issues"), 0.8),
            (reverse("campaign:contact"), 0.7),
            (reverse("campaign:faq"), 0.6),
            (reverse("campaign:cut_red_tape"), 0.8),
            (reverse("campaign:cheap_energy"), 0.8),
            (reverse("campaign:safe_streets"), 0.8),
        ]

    def location(self, item):
        return item[0]

    def priority(self, item):
        return item[1]
