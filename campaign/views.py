from django.shortcuts import render


def homepage(request):
    return render(request, "campaign/homepage.html")


def cut_red_tape(request):
    return render(request, "campaign/cut_red_tape.html")


def cheap_energy(request):
    return render(request, "campaign/cheap_energy.html")


def safe_streets(request):
    return render(request, "campaign/safe_streets.html")
