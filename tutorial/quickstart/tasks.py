from celery import shared_task, task
from collections import Counter

from .models import Job


@task()
def del_words(job_id):
    '''delete in file, all the words which have higher 
    frequency than the parameter given in url'''
    job = Job.objects.get(id=job_id)
    job.status = job.WORKING
    job.save()
    data = job.file.data

    l = data.split()
    count_dict = Counter(l)
    new_l = [x for x in l if count_dict[x] <= job.freq]
    new_data = ' '.join(new_l)

    job.status = job.DONE
    job.file.data = new_data
    job.save()

        
