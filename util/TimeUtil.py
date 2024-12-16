import datetime

def get_today():
    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d")
    return today