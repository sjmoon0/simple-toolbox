'''
Program that that plots Facebook friend search history data as a bar graph.
X axis: Year-Month
Y axis: # of searches for given friends

Personal Facebook data will need to be downloaded. The file that this program
references is facebook-username\search_history\your_search_history.json
File should be in the same directory as this program when executed.

External Dependencies: matplotlib
'''

import json
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import time

def get_search_dict(f_name):
    with open(f_name,"r") as f:
        data = json.load(f)
        return data

def utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset

def get_search_list(search_dict):
    data = {}
    for search in search_dict["searches"]:
        search_time = datetime.utcfromtimestamp(search["timestamp"])
        search_time = utc_to_local(search_time)
        year_month = str(search_time.year)+"-"+str(search_time.month)
        search_string = search["title"][17:]
        try:
            data[year_month].append(search_string)
        except:
            data[year_month] = [search_string]
    return data
    
def get_person_count_per_month(gf_name,search_list):
    data = ([],[])
    for month in search_list:
        data[0].append(month)
        data[1].append(search_list[month].count(gf_name))
    return data

def plot_person(name,ax,x_pos):
    result = get_person_count_per_month(name,search_list)
    result[0].reverse()
    result[1].reverse()
    ax.bar(x_pos,result[1],label=name)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(result[0],rotation=90)

search_dict = get_search_dict("your_search_history.json")
search_list = get_search_list(search_dict)
x_pos = np.arange(len(search_list))
fig,ax = plt.subplots()
plot_person("Firstname0 Lastname0",ax,x_pos)
plot_person("Firstname1 Lastname1",ax,x_pos)
ax.legend()
plt.show()
