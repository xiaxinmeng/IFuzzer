# -*- coding: utf-8 -*-
import os
job_name = os.environ['a']
print(job_name)
print(isinstance(job_name, str))
print(type(job_name))
with open('name.txt', 'w', encoding='utf-8')as fw:
    fw.write(job_name)