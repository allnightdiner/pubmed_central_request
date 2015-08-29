from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic import DetailView, FormView, ListView
from django.views.generic.edit import FormMixin

from pmc_request.forms import PMCRequestForm, PMCRequestAcceptForm
from pmc_request.models import PMCArticle, Request 

class PMCRequestForm(FormView):
    template_name = 'request.html'
    form_class = PMCRequestForm
    success_url = "/"

    def form_valid(self, form):
        form_pmc_id = form.cleaned_data['pmc_id']
        try:
            pmc_article = PMCArticle.objects.get(pmc_id=form_pmc_id)
        except ObjectDoesNotExist:
            pmc_article = PMCArticle(pmc_id = fomr_pmc_id)
            pmc_article.save()
        
        request = Request(pmc_article = pmc_article, article_accepted = False)
        request.save()
        
        self.success_url = reverse_lazy('request_detail', kwargs = {'pk': request.id})
        return super(PMCRequestForm, self).form_valid(form)

class RequestDetail(FormMixin, DetailView):
    model = Request
    form_class = PMCRequestAcceptForm
    succes_url = "/"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        #set request objects article_accepted field
        #send email to author
        return super(ReqestDetail, self).form_valid(form)

