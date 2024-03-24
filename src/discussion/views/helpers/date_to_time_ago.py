from django.utils import timezone

def to_time_ago(date):
    time_now = timezone.now()
    time_created = timezone.make_aware(date)
    time_difference = time_now - time_created

    seconds =   time_difference.seconds
    minutes = seconds // 60
    hours = minutes // 60
    days = time_difference.days
    weeks =  days // 7
    months = days // 30
    years =  days // 365
    time_value = 0
    time_unit = ""
    if years > 0 :
        time_value, time_unit = years, "year"
    elif months > 0 :
        time_value, time_unit = months, "month"
    elif weeks > 0 :
        time_value, time_unit = weeks, "week"
    elif days > 0 :
        time_value, time_unit = days, "day"
    elif hours > 0 :
        time_value, time_unit = hours, "hour"
    elif minutes > 0 :
        time_value, time_unit = minutes, "minute"
    else :
        time_value, time_unit = seconds, "second"
    time_plural = "s" if time_value > 1 else ""
    return f"{time_value} {time_unit + time_plural} ago"