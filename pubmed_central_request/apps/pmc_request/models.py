from django.db import models

class PMCArticle(models.Model):
    pmc_id = models.IntegerField()
    author_email = models.EmailField()

class Request(models.Model):
    pmc_article = models.ForeignKey('PMCArticle')
    article_accepted = models.BooleanField()
    request_timestamp = models.DateTimeField(auto_now=True)
    email_sent_timestamp = models.DateTimeField()
