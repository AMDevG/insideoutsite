from django.conf.urls import include, url
from insideoutchi import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    url(r'^home/$', views.home, name="home"),
    url(r'^detail/(?P<num>\d+)$', views.detail, name='detail'),
    url(r'^pubDetail/(?P<num>\d+)$', views.pubDetail, name='pubDetail'),
    url(r'^artwork/$',views.artwork, name="artwork"),
    url(r'^essays/',views.essays, name="essays"),
    url(r'^poetry/$',views.poetry, name="poetry"),
    url(r'^year_three/$',views.three, name="yr_one"),
    url(r'^year_two/$',views.two, name="yr_two"),
    url(r'^year_one/$',views.one, name="yr_one"),
    url(r'^test/$',views.test, name="test"),
    url(r'^about/$',views.about, name="about"),
    url(r'^pdf2/$',views.pdf2, name="pdf2"),
    url(r'^contact/$',views.contact, name="contact"),
    url(r'^success/$',views.success, name="success"),
    url(r'^thinktanks/$', views.thinktank, name="thinktank")



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
