from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("compute/<int:value>", views.compute, name="compute"),
    path("isprime/<int:value>", views.is_prime, name="is_prime"),
    path("homepage/", views.homepage, name="homepage"),
    path("kml-shape-generator/", views.kml_shape_generator, name="kml_shape_generator"),
    path("project/<slug:slug>/", views.project_detail, name="project_detail"),
    path("skill/<path:skill>/", views.projects_by_skill, name="projects_by_skill"),
]