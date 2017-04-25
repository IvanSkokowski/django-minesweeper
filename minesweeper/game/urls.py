from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^new/', views.new),
    url(r'^game/(?P<game_id>\d+)/?$', views.details),
    url(r'^game/(?P<game_id>\d+)/move/?$', views.move),
]
