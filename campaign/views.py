from django.shortcuts import render


def homepage(request):
    return render(request, "campaign/homepage.html")


def about(request):
    return render(request, "campaign/about.html")


def issues(request):
    return render(request, "campaign/issues.html")


def contact(request):
    return render(request, "campaign/contact.html")


def faq(request):
    return render(request, "campaign/faq.html")


def cut_red_tape(request):
    return render(request, "campaign/cut_red_tape.html")


def cheap_energy(request):
    return render(request, "campaign/cheap_energy.html")


def safe_streets(request):
    return render(request, "campaign/safe_streets.html")


def sitemap_html(request):
    return render(request, "campaign/sitemap.html")
