from django.db import models

class File(models.Model):
    name = models.TextField(blank=False, null=False)
    file = models.FileField(upload_to='uploads/%Y/%m/%d')
    filesize = models.IntegerField(null=None)

class Job(models.Model):
    IDLE = 'IDLE'
    WORKING = 'WORKING'
    DONE = 'DONE'
    STATUS_CHOICES = [
        (IDLE, 'Idle'),
        (WORKING, 'Working'),
        (DONE, 'Done'),
    ]

    file = models.ForeignKey(File, on_delete=models.CASCADE)
    freq = models.IntegerField(null=False)
    result = models.TextField(blank=False, null=True, default=None)
    status = models.CharField(
            max_length=max([len(x) for x, _ in STATUS_CHOICES]),
            choices=STATUS_CHOICES,
            default=IDLE,
        )

    
