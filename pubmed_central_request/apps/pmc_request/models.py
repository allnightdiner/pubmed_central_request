from django.db import models

class pmc_article(models.Model):
    pmc_id = models.IntegerField()
    author_email = models.EmailField()

class request(models.Model):
    pmc_article = models.ForeignKey('pmc_article')
    article_accepted = models.BooleanField()
    request_timestamp = models.DateTimeField(auto_now=True)
    email_sent_timestamp = models.DateTimeField()
