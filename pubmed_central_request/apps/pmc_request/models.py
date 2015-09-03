from django.db import models

class PMCArticle(models.Model):
    pmc_id = models.IntegerField()
    corresp_email = models.EmailField()
    title = models.TextField()
    url = models.URLField(max_length=2048)

class PMCAuthor(models.Model):
    author = models.TextField()
    pmc_article = models.ManyToManyField('PMCArticle')

class Request(models.Model):
    pmc_article = models.ForeignKey('PMCArticle')
    article_accepted = models.BooleanField()
    request_timestamp = models.DateTimeField(auto_now=True)
    email_sent_timestamp = models.DateTimeField(null = True)
