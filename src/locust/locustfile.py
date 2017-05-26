#!/usr/bin/env python
from locust import HttpLocust, TaskSet, task
 
class UserBehavior(TaskSet):
        @task
        def getfile(l):
           l.client.get("/")

class WebsiteUser(HttpLocust):
   task_set = UserBehavior
   min_wait=500
   max_wait=500
