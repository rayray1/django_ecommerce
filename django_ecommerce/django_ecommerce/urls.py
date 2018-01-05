from django.conf.urls import url, include
from django.contrib import admin

admin.autodiscover()

from main import views as main_views
from contact import views as contact_views






urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.index, name='home'),

    url(r'^pages/', include('django.contrib.flatpages.urls')), # about page
    url(r'^contact/', contact_views.contact, name='contact'),  # contact page
]
