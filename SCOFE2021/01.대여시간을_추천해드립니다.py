# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())
import datetime as dt
# from dateutil.parser import parse

str_times = []
end_times = []
for _ in range(user_input):
    tmp_times = input().split()
    tmp_strt = dt.datetime.strptime(tmp_times[0], "%H:%M")
    tmp_endt = dt.datetime.strptime(tmp_times[-1], "%H:%M")
    str_times.append(tmp_strt)
    end_times.append(tmp_endt)

str_times.sort()
end_times.sort()

if str_times[-1] < end_times[0]:
    print(str_times[-1].strftime("%H:%M") + " ~ " + end_times[0].strftime("%H:%M"))
else:
    print('-1')