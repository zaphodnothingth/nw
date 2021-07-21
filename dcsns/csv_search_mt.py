# general python 
import time
import sys
import re
import json
import pandas as pd
from datetime import datetime, timedelta
import csv
import random
# from unidecode import unidecode
import traceback
from requests.exceptions import Timeout, ConnectionError

# multithreading
import threading
import queue
global lck 
lck = threading.Lock()


def doi_proc(doi):
    with open('MAG/Papers.txt', 'r') as csvfile:
        # return map(lambda x: x if x.startswith(doi + ',') else None, csvfile) # iterates through text looking for match
        resp = [x if x.startswith(doi + ',') else None for x in csvfile] # iterates through text looking for match
    return resp


class Worker(threading.Thread):


    def __init__(self, q, i, *args, **kwargs):
        self.q = q
        self.i = i
        super().__init__(*args, **kwargs)


    def run(self):
        while True:
            try:
                j, receive_dict, csv_columns = self.q.get(timeout=3)  # 3s timeout
                i = self.i
            except queue.Empty:
                return

            doi = receive_dict['DOI']
            return_dict = {}
            return_dict['DOI'] = doi

            try:
                return_dict['PaperId'] = doi_proc(doi)

            except:
                traceback.print_exc()
                print('[t{}] {}- error: {}\n\tlink: {}\n\n\n\n\n\n\n'.format(i, j, sys.exc_info()[0], doi))  
                return_dict['response'] = 'unreachable'   


            lck.acquire()
            with open("output.csv", 'a',encoding='utf-8-sig', newline='') as g:
                csv.DictWriter(g, fieldnames=csv_columns).writerow(return_dict)
            lck.release()
            print('[t{}] {}- written\n\tlink: {}'.format(i, j, url))
            self.q.task_done()
            

print('start time: {}'.format(datetime.now().strftime("%Y-%m-%d-%H.%M.%S")))
start_time = time.time()

# n_threads= int(args[0])
n_threads = 30

print('target count: {}'.format(len(df.DOI)))

################### add desired output columns
csv_columns = ['DOI', 'PaperId']
with open("output.csv", 'w',encoding='utf-8-sig', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()

q = queue.Queue()
for k, row in enumerate(df.itertuples()):
    dictRow = row._asdict()
    q.put_nowait((k, dictRow, csv_columns))
for _ in range(n_threads):
    Worker(q, _).start()
    time.sleep(1)
q.join()

print('finished. end time: {}'.format(datetime.now().strftime("%Y-%m-%d-%H.%M.%S")))
print('completed in {}'.format(timedelta(seconds=int(time.time() - start_time))))