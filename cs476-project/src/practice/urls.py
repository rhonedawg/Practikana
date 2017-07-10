from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Home, name='home'), #r means regular expression & ^ means the beginning of the expression

    #This will setup /home/0-9 so create different webpages from that main page.
    #url(r'^(?P<practice_id>[0-9])$')

    #url(r'^admin/', admin.site.urls),
]
