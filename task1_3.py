
from datetime import datetime
from datetime import timedelta

def days_to_NY():
    now = datetime.today()
    NY = datetime(now.year+1, 1, 1, 0, 0, 0)
    delta = (NY - now).days
    return delta

full_days = days_to_NY()
print('There are {} full days until New Year'.format(full_days))
