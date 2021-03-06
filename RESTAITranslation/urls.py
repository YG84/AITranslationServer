"""RESTAITranslation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from RESTAITranslation import views

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^translations/$',
        views.TranslationList.as_view(),
        name='translation-list'),
    url(r'^translations/(?P<pk>[0-9]+)/$',
        views.TranslationDetail.as_view(),
        name='translation-detail'),
    url(r'^algorithms/$',
        views.AlgorithmList.as_view(),
        name='algorithm-list'),
    url(r'^algorithms/(?P<pk>[0-9]+)/$',
        views.AlgorithmDetail.as_view(),
        name='algorithm-detail')
])

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]