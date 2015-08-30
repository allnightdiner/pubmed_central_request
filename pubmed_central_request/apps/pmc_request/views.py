from xml.etree import ElementTree
import urllib.request

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
            pmc_article = PMCArticle(pmc_id = form_pmc_id)
            pmc_article.save()
        
        request = Request(pmc_article = pmc_article, article_accepted = False)
        request.save()
        
        self.success_url = reverse_lazy('request_detail', 
                                        kwargs = {'pk': request.id})
        return super(PMCRequestForm, self).form_valid(form)

class RequestDetail(FormMixin, DetailView):
    model = Request
    form_class = PMCRequestAcceptForm
    succes_url = "/"

    def get_context_data(self, **kwargs):
        context = super(RequestDetail, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        
        url = settings.REQUEST_URL.format(pmc_id=self.object.pmc_article.pmc_id)
        url_file = urllib.request.urlopen(url)
        if url_file == None:
            #set error message
            pass
        tree = ElementTree.parse(url_file)
        root = tree.getroot()
        
        article_title = root.find('.//article-title').text
        
        article_authors = []
        article_authors_xml = root.findall(".//contrib[@contrib-type='author']"\
                                           "/name")
        for author in article_authors_xml:
            surname = author.find("surname").text
            given_names = author.find("given-names").text
            article_authors.append(surname + ", " + given_names)
        
        context['article_title'] = article_title
        context['article_authors'] = article_authors
        context['article_url'] = url
        
        url_file.close()
        
        return context

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

