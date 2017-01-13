# Используйте команду sips
#
# Документация:
# https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man1/sips.1.html
#
# Пример использования для нашей задачи:
# sips --resampleWidth 200 myphoto.jpg

import os
import glob
import subprocess
import time


# Решил замерить время исполнения
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))


with Profiler() as p:
    source = 'Source'

    files = glob.glob(os.path.join(source, "*.jpg"))

    for file in files:
        subprocess.run(['sips', '--resampleWidth', '200', file, '--out', 'Result'])
