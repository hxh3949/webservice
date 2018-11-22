import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Calendar


# Create your views here.

def index(request, date):
    # 查询所有图书
    date_list = date.split('-')
    date_info = Calendar.objects.filter(date=datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2])))
    # 将图书列表传递到模板中，然后渲染模板
    info = date_info[0]
    dict = {
        'date': info.date,
        'dow': info.dow,
        'year_lunar': info.year_lunar,
        'month_lunar': info.month_lunar,
        'day_lunar': info.day_lunar,
        'year_branch': info.year_branch,
        'zodiac': info.zodiac,
        'leap_month': info.leap_month,
        'month_branch': info.month_branch,
        'day_branch': info.day_branch,
        'solar_period': info.solar_period,
        'solar_period_time': info.solar_period_time,
        'holiday': info.holiday,
        'holiday_lunar': info.holiday_lunar,
        'holiday_special': info.holiday_special,
        'hot_summer_days': info.hot_summer_days,
    }
    return render(request, 'holiday/index.html', {'info': dict})
