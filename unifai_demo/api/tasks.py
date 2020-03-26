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
    content = job.file.content
    if isinstance(content, memoryview):
        content = content.tobytes()
    content = content.decode('utf-8')
    l = content.split()
    count_dict = Counter(l)
    new_l = [x for x in l if count_dict[x] <= job.freq]
    new_content = ' '.join(new_l)

    job.result = new_content
    job.status = job.DONE
    job.save()

        
