# How to Use
Here are the example commands for recording:
```
git add some_file
python record_mtime.py
git add .record_mtime
git commit -m "some messages"
```
The example commands for restoring:
```
git checkout a_commit_or_branch
python restore_mtime.py
```
# See Also
https://docs.python.org/3/library/os.html#os.stat_result.st_mtime_ns \
https://docs.python.org/3/library/os.html#os.utime \
https://docs.python.org/3/library/os.html#os.popen \
https://docs.python.org/3/library/time.html#time.strftime \
https://docs.python.org/3/library/time.html#time.strptime \
https://docs.python.org/3/library/time.html#time.struct_time.tm_gmtoff \
https://docs.python.org/3/library/datetime.html#datetime.datetime.timestamp \
https://docs.python.org/3/library/datetime.html#datetime.timezone \
https://git-scm.com/docs/git-ls-files#_output



