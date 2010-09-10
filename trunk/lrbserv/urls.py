from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^lrbserv/', include('lrbserv.foo.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^profiles/', include('profiles.urls')),
    (r'^avatar/', include('avatar.urls')),
##
##    Request URL:  	http://127.0.0.1:8000/accounts/
##
##    Using the URLconf defined in lrbserv.urls, Django tried these URL patterns, in this order:
##
##       1. ^admin/doc/
##       2. ^admin/
##       3. ^accounts/ ^activate/complete/$
##       4. ^accounts/ ^activate/(?P<activation_key>\w+)/$
##       5. ^accounts/ ^register/$
##       6. ^accounts/ ^register/complete/$
##       7. ^accounts/ ^register/closed/$
##       8. ^accounts/ ^login/$
##       9. ^accounts/ ^logout/$
##      10. ^accounts/ ^password/change/$
##      11. ^accounts/ ^password/change/done/$
##      12. ^accounts/ ^password/reset/$
##      13. ^accounts/ ^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$
##      14. ^accounts/ ^password/reset/complete/$
##      15. ^accounts/ ^password/reset/done/$
##
##          ^profiles/ ^create/$
##          ^profiles/ ^edit/$',
##          ^profiles/ ^(?P<username>\w+)/$
##          ^profiles/ ^$
##
)
