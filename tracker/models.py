from django.db import models


class IntentVisitor(models.Model):
    session_id = models.CharField(max_length=100)
    keyword = models.CharField(max_length=255)
    source = models.CharField(max_length=50)
    page_url = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=45)
    user_agent = models.TextField()
    intent_level = models.CharField(max_length=20, default='LOW')
    flipkart_clicked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.session_id
