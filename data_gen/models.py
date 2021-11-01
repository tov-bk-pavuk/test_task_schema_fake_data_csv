from django.db import models


class DataSetFile(models.Model):
    ready = 'RD'
    processing = 'PR'

    status_choices = [
        (ready, 'Ready'),
        (processing, 'Processing')
    ]

    created = models.DateField(auto_now=True)
    status = models.CharField(max_length=2, choices=status_choices, default=processing)
    url = models.URLField(max_length=200, default='static/media/default.csv')

    def __str__(self):
        return 'file'
