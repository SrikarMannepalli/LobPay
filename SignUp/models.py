from django.db import models

class phoneModel(models.Model):
    Mobile = models.IntegerField(blank=False)
    isVerified = models.BooleanField(blank=False, default=False)
class Meta:
        app_label = 'LobPay'
def __str__(self):
        return str(self.Mobile)
