from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse

from campaign.views import homepage as campaign_homepage
from campaign.sitemaps import CampaignSitemap
from portfolio.views import homepage as portfolio_homepage
from portfolio.sitemaps import PortfolioSitemap


def domain_homepage(request):
    host = request.get_host().split(":")[0].lower()

    if host == "campaign.blakerichardson.dev" or host.startswith("campaign."):
        return campaign_homepage(request)

    if host == "portfolio.blakerichardson.dev" or host.startswith("portfolio."):
        return portfolio_homepage(request)

    return portfolio_homepage(request)


def dynamic_sitemap(request, *args, **kwargs):
    host = request.get_host().split(":")[0].lower()

    if host == "campaign.blakerichardson.dev" or host.startswith("campaign."):
        sitemaps = {"campaign": CampaignSitemap}
    else:
        sitemaps = {"portfolio": PortfolioSitemap}

    return sitemap(request, sitemaps, *args, **kwargs)


def robots_txt(request):
    scheme = "https" if request.is_secure() else "http"
    host = request.get_host()
    lines = [
        "User-agent: *",
        "Allow: /",
        f"Sitemap: {scheme}://{host}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
