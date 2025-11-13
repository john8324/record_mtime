import os
import time
from datetime import datetime, timedelta, timezone

def mystr_to_mtime_ns(mystr: str) -> int:
    ts = time.strptime(mystr[:-9], f'%Y/%m/%d[U%z]T%H:%M:%S.')
    #print(ts)
    #print(ts.tm_zone, ts.tm_gmtoff)
    tz = timezone(timedelta(seconds=ts.tm_gmtoff))
    dt = datetime(ts.tm_year, ts.tm_mon, ts.tm_mday, ts.tm_hour, ts.tm_min, ts.tm_sec, tzinfo=tz)
    return int(dt.timestamp()) * 1000000000 + int(mystr[-9:])

#print(mystr_to_mtime_ns('2025/11/08[U+0800]T03:53:36.204786139'))
#print(mystr_to_mtime_ns('2025/11/08[U-0500]T03:53:36.204786139'))

import csv

# If you run this file in Windows, you need to check your python is running in UTF8 mode.
with open('.record_mtime', newline='') as f:
    r = csv.reader(f, delimiter='\t', lineterminator='\n')
    for rr in r:
        assert len(rr) == 2
        mtime_ns, path = rr
        if os.path.exists(path):
            mtime_ns = mystr_to_mtime_ns(mtime_ns)
            print(mtime_ns, rr[0], path)
            os.utime(path, ns=(mtime_ns, mtime_ns)) # Don't care tf atime_ns
