import os
import smtplib
import urllib.request
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from xml.etree import ElementTree

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy
from django.forms.forms import NON_FIELD_ERRORS
from django.forms.util import ErrorList
from django.views.generic import DetailView, FormView, ListView
from django.views.generic.edit import FormMixin

from pmc_request.forms import PMCRequestForm, PMCRequestAcceptForm
from pmc_request.models import PMCArticle, PMCAuthor, Request 

def get_authors(root):
    authors = []
    authors_xml = root.findall(
            ".//contrib[@contrib-type='author']/name"
    )
    for author_xml in authors_xml:
        surname = author_xml.find("surname").text
        given_names = author_xml.find("given-names").text
        author = surname + ", " + given_names
        authors.append(author)
    return authors

def get_article_title(root):
    article_title = root.find('.//article-title').text
    return article_title

def get_corresp_email(root):
    corresp_email_xml = root.find(".//corresp/email")
    corresp_email = corresp_email_xml.text
    return corresp_email

class PMCRequestForm(FormView):
    template_name = 'request.html'
    form_class = PMCRequestForm
    success_url = "/"

    def form_valid(self, form):
        form_pmc_id = form.cleaned_data['pmc_id']
        try:
            pmc_article = PMCArticle.objects.get(pmc_id=form_pmc_id)
        except ObjectDoesNotExist:
            url = settings.REQUEST_URL.format(pmc_id=form_pmc_id)
            
            url_file = urllib.request.urlopen(url)
            if url_file == None:
                form._errors[NON_FIELD_ERRORS] = ErrorList([
                                "Unable to access URL generated: " + url
                            ])
                self.form_invalid(form)
            
            tree = ElementTree.parse(url_file)
            root = tree.getroot()
            
            error = root.find(".//Reply")
            if error is not None:
                form._errors[NON_FIELD_ERRORS] = ErrorList([
                                error.attrib['error']
                            ])
                return self.form_invalid(form)
            
            article_title = get_article_title(root)
            corresp_email = get_corresp_email(root)
            authors = get_authors(root)
            
            url_file.close()
            
            pmc_article = PMCArticle(
                pmc_id = form_pmc_id,
                title = article_title,
                corresp_email = corresp_email,
                url = url
            )
            pmc_article.save()
            
            for author in authors:
                pmc_author = PMCAuthor(
                    author = author
                )
                pmc_author.save()
                pmc_author.pmc_article.add(pmc_article)
         
        request = Request(pmc_article = pmc_article, article_accepted = False)
        request.save()
        
        self.success_url = reverse_lazy('request_detail', 
                                        kwargs = {'pk': request.id})
        return super(PMCRequestForm, self).form_valid(form)

class RequestDetail(FormMixin, DetailView):
    model = Request
    form_class = PMCRequestAcceptForm
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(RequestDetail, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        ''' send email to author
        
        msg = MIMEMultipart('alternative')

        msg['Subject'] = "Article Access Notification"
        msg['From'] = settings.SENDING_EMAIL
        msg['To'] = self.object.pmc_article.author_email
        
        email_template = "Hello {name},\nThis is a notification that your "\
                         "article {article_title} has been searched for "\
                         "in PubMed Central\n"
        text = email_template.format(
                name = self.object.pmc_article.author,
                article_title = self.object.pmc_article.title
        )
        mime_text = MIMEText(text, 'plain')

        username = os.environ['MANDRILL_USERNAME']
        password = os.environ['MANDRILL_PASSWORD']

        msg.attach(mime_text)

        s = smtplib.SMTP('smtp.mandrillapp.com', 587)

        s.login(username, password)
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()
        '''
        
        self.object.article_accepted = form.cleaned_data['accept_article']
        self.object.email_sent_timestamp = datetime.now()
        self.object.save()
        return super(RequestDetail, self).form_valid(form)

class RequestList(ListView):
    model = Request

