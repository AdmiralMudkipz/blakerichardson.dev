from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse, HttpResponseRedirect

from campaign.views import homepage as campaign_homepage
from campaign.sitemaps import CampaignSitemap
from portfolio.views import homepage as portfolio_homepage
from portfolio.sitemaps import PortfolioSitemap


CAMPAIGN_HOST = "campaign.blakerichardson.dev"
ROOT_HOSTS = {"blakerichardson.dev", "www.blakerichardson.dev"}

AI_AND_SEARCH_BOTS = [
    "Googlebot",
    "Bingbot",
    "GPTBot",
    "OAI-SearchBot",
    "ChatGPT-User",
    "Google-Extended",
    "PerplexityBot",
    "ClaudeBot",
    "Claude-SearchBot",
    "Applebot",
]


def domain_homepage(request):
    host = request.get_host().split(":")[0].lower()

    if host in ROOT_HOSTS:
        return HttpResponseRedirect(f"https://{CAMPAIGN_HOST}/")

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
    lines = ["User-agent: *", "Allow: /", "Disallow: /admin/", ""]
    for bot in AI_AND_SEARCH_BOTS:
        lines += [f"User-agent: {bot}", "Allow: /", "Disallow: /admin/", ""]
    lines.append(f"Sitemap: {scheme}://{host}/sitemap.xml")
    return HttpResponse("\n".join(lines), content_type="text/plain")


LLMS_TXT = """# Blake Richardson for Township Committee

> Official campaign website of Blake Richardson, candidate for Harrison Township Committee (Mullica Hill, Gloucester County, New Jersey). Election: Tuesday, November 3. Ballot position: Column A.

Blake Richardson grew up in Mullica Hill, attended Clearview, and graduated from Rowan University. His platform: maximize state grants for safer streets and connected paths between neighborhoods, schools, transit, and Main Street; update outdated solar rules; make township committee meetings available live online and as recordings; and relegalize traditional Main Street style development.

This is a campaign website, so its content is the candidate's own positions. For official election information (early voting, mail-in ballots, polling places) use the Gloucester County Clerk. For township law, see Harrison Township's code at https://ecode360.com/HA1928.

## Pages
- [Home](https://campaign.blakerichardson.dev/): campaign overview, election date, priorities
- [About Blake](https://campaign.blakerichardson.dev/campaign/about/): biography
- [Issues](https://campaign.blakerichardson.dev/campaign/issues/): overview of all policy areas
- [Safe Streets](https://campaign.blakerichardson.dev/campaign/safe-streets/): grants, Safe Routes to School, crosswalks, traffic calming, bus shelters
- [Cheap Energy](https://campaign.blakerichardson.dev/campaign/cheap-energy/): solar rule changes
- [Cut Red Tape](https://campaign.blakerichardson.dev/campaign/cut-red-tape/): meeting transparency, zoning, parking, setbacks, Main Street development, in-law suites
- [FAQ](https://campaign.blakerichardson.dev/campaign/faq/): common questions

## Contact
blake@blakerichardson.dev

Paid for by Blake Richardson for Township Committee, 413 Labrador Trail, Mullica Hill NJ 08062
"""


def llms_txt(request):
    return HttpResponse(LLMS_TXT, content_type="text/plain; charset=utf-8")
