"""test_server URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from testweb import views as view1
from adminpage import views as view2

from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^testweb/', view1.index),
    url(r'^adminpage/', view2.index, name='index_faq'),
    url(r'^list_faqs/', view2.listfaqs, name='list_faqs'),
    url(r'^list_logs/', view2.listlogs, name='list_logs'),
    url(r'^statistics_logs/', view2.statisticslogs, name='statistics_logs'),
    url(r'^chart/', view2.chart, name='chart'),
    url(r'^create/', view2.FaqCreateView.as_view(), name='create_faq'),
    path('update/<int:pk>', view2.FaqUpdateView.as_view(), name='update_faq'),
    path('delete/<int:pk>', view2.FaqDeleteView.as_view(), name='delete_faq'),
    # path('adminpage/delete/<int:pk>', view2.FaqDeleteView.as_view(), name='delete_faq'),
    # url(r'^update/<int:pk>', view2.FaqUpdateView.as_view(), name='update_faq'),
    # url(r'^delete/<int:pk>', view2.FaqDeleteView.as_view(), name='delete_faq'),
]
