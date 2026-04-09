from django.shortcuts import redirect
from campaign.views import homepage as campaign_homepage
from portfolio.views import homepage as portfolio_homepage


def domain_homepage(request):
    host = request.get_host().split(":")[0].lower()

    if host == "campaign.blakerichardson.dev" or host.startswith("campaign."):
        return campaign_homepage(request)

    if host == "portfolio.blakerichardson.dev" or host.startswith("portfolio."):
        return portfolio_homepage(request)

    return redirect("https://portfolio.blakerichardson.dev")


def error_redirect(request, *args, **kwargs):
    return redirect("https://portfolio.blakerichardson.dev")
