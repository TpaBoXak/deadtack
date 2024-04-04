from datetime import datetime
from datetime import date

def isostr_to_datetime(time_str: str) -> date:
    try:
        res_date: datetime = date.fromisoformat(time_str)
        return res_date
    except:
        return None
    
def date_to_dateiso(time: date) -> date:
    try:
        res_str: str = time.isoformat()
        return res_str
    except:
        return None
