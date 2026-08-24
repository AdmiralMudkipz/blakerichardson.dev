from django.urls import path
from . import views

app_name = "campaign"

urlpatterns = [
    path("homepage/", views.homepage, name="homepage"),
    path("about/", views.about, name="about"),
    path("issues/", views.issues, name="issues"),
    path("contact/", views.contact, name="contact"),
    path("faq/", views.faq, name="faq"),
    path("cut-red-tape/", views.cut_red_tape, name="cut_red_tape"),
    path("cheap-energy/", views.cheap_energy, name="cheap_energy"),
    path("safe-streets/", views.safe_streets, name="safe_streets"),
    path("sitemap/", views.sitemap_html, name="sitemap"),
]
