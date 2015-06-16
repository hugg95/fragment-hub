from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'fragment_hub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'fragment_hub.views.index'),

    # for user signup and login
    url(r'^user/login/', 'fragment_hub.views.login'),
    url(r'^user/signup/', 'fragment_hub.views.signup'),
    url(r'^user/change_password/', 'fragment_hub.views.change_password'),
]
