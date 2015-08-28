from django.db import models

class request(models.Model):
    pmd_id = models.IntegerField()
    # URLField subclasses CharField whose max length defaults to 200
    accessed_url = models.URLField(max_length=2048)
    request_timestamp = models.DateTimeField(auto_now=True)
    article_accepted = models.BooleanField()
    author_email = models.EmailField()
    email_sent_timestamp = models.DateTimeField()
