from django.conf.urls import url, include
from django.contrib import admin

admin.autodiscover()

from main import views as main_views
from contact import views as contact_views
from payments import views as payment_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.index, name='home'),

    url(r'^pages/', include('django.contrib.flatpages.urls')), # about page
    url(r'^contact/', contact_views.contact, name='contact'),  # contact page

    # user registration/authentication
    url(r'^sign_in$', payment_views.sign_in, name='sign_in'),
    url(r'^sign_out$', payment_views.sign_out, name='sign_out'),
    url(r'^register$', payment_views.register, name='register'),
    url(r'^edit$', payment_views.edit, name='edit'),
]
