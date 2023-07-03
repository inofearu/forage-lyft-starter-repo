from datetime import date
from dateutil.relativedelta import relativedelta


def add_years(_date, years_to_add):
    return _date + relativedelta(years=years_to_add)
    
def get_time():
    return date.today()
