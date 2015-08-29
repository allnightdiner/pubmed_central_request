from django.conf.urls import patterns, url

from pmc_request.views import PMCRequestForm, RequestDetail

urlpatterns = patterns('',
    url(r'^request/(?P<pk>\d+)$', RequestDetail.as_view(),
      name='request_detail'),
    url(r'^$', PMCRequestForm.as_view(), name='request_create'),
)
