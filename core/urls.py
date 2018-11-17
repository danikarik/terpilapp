from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.jinja')),
    path('profile/', TemplateView.as_view(template_name='authboss/profile.jinja'), name='profile'),
    path('authboss/', include('authboss.urls')),
    path('admin/', admin.site.urls),
]
