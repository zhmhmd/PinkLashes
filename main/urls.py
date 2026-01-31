from django.urls import path
from .views import (
    HomeTemplate,
    AboutUsTemplate,
    ServiceTemplate,
    MastersTemplate,
    MasterDetailTemplate,
    SignUpCreate,
)

urlpatterns = [
    path("", HomeTemplate.as_view(), name="home"),
    path("about-us/", AboutUsTemplate.as_view(), name="aboutus"),
    path("service/", ServiceTemplate.as_view(), name="service"),
    path("masters/", MastersTemplate.as_view(), name="masters"),
    path("about-master/<int:id>/", MasterDetailTemplate.as_view(), name="aboutmaster"),
    path("signup/", SignUpCreate.as_view(), name="signup"),
]