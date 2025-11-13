import os

# If you run this file in Windows, you need to check your python is running in UTF8 mode.
with os.popen('git ls-files -z') as pf:
    paths = pf.read()

paths = [p for p in paths.split('\x00') if p and os.path.exists(p)]
print(paths)

mtime_ns_s = [os.stat(p).st_mtime_ns for p in paths]
#print(mtime_ns_s)

import time

def mtime_ns_to_mystr(mtime_ns: int) -> str:
    s, ns = divmod(mtime_ns, 1000000000)
    return time.strftime(f'%Y/%m/%d[U%z]T%H:%M:%S.{ns:09d}', time.localtime(s))
mtime_strs = [mtime_ns_to_mystr(mtime_ns) for mtime_ns in mtime_ns_s]

import csv
with open('.record_mtime', 'w', newline='') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n')
    w.writerows((r for r in zip(mtime_strs, paths)))

print(len(paths), 'records')
