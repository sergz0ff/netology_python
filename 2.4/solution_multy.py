import os
import glob
import subprocess
import time
from multiprocessing.dummy import Pool as ThreadPool


# Решил замерить время исполнения
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))


source = 'Source'

files = glob.glob(os.path.join(source, "*.jpg"))


def call_sips(file_name):
    subprocess.run(['sips', '--resampleWidth', '200', file_name, '--out', 'Result'])


# Make the Pool of workers
pool = ThreadPool(4)

with Profiler() as p:
        pool.map(call_sips, files)
