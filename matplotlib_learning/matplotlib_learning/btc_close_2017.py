import json
import pygal
import math

from itertools import groupby

#
filename = 'btc_close_2017_request.json'
with open(filename) as f:
    btc_data = json.load(f)

#
dates = []
months = []
weeks = []
weekdays = []
closes = []
#
for btc_dict in btc_data:
    date = btc_dict['date']
    dates.append(date)
    month = int(btc_dict['month'])
    months.append(month)
    week = int(btc_dict['week'])
    weeks.append(week)
    weekday = btc_dict['weekday']
    weekdays.append(weekday)
    close = int(float(btc_dict['close']))
    closes.append(close)
    #print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = 'Closing Price (￥)'
line_chart.x_labels = dates
N = 20 # show X scale label per 20days
line_chart.x_labels_major = dates[::N]
line_chart.add('Closing Price', closes)
line_chart.render_to_file('images\Line Chart for Closing Price (￥).svg')

line_chart_logTrans = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart_logTrans.title = 'Log Transformation for Closing Price (￥)'
line_chart_logTrans.x_labels = dates
N = 20 # show X scale label per 20days
line_chart_logTrans.x_labels_major = dates[::N]
closes_log = [math.log10(_) for _ in closes]
line_chart_logTrans.add('Log Closing Price', closes_log)
line_chart_logTrans.render_to_file('images\Log Transformation Chart for Closing Price (￥).svg')

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart_mean = pygal.Line()
    line_chart_mean.title = title
    line_chart_mean.x_labels = x_unique
    line_chart_mean.add(y_legend, y_mean)
    
    # ^^
    folder = 'images\ '
    line_chart_mean.render_to_file(folder.rstrip()+title+'.svg')

    return line_chart_mean

#
idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], closes[:idx_month], 'Month Mean Value Of Closing Price (￥)', 
    'Month mean value')
line_chart_month

#
idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week], closes[1:idx_week], 'Week Mean Value Of Closing Price (￥)', 
    'Week mean value')
line_chart_week

#
idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int, closes[1:idx_week], 'Weekday Mean Value Of Closing Price (￥)', 
    'Weekday mean value')
line_chart_weekday.x_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
line_chart_weekday.render_to_file('images\Weekday Mean Value Of Closing Price (￥).svg')

#
with open('images\ClosingPriceDashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write('<html><head><title>Closing Price Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [
            'Line Chart for Closing Price (￥).svg', 'Log Transformation Chart for Closing Price (￥).svg', 'Month Mean Value Of Closing Price (￥).svg', 
            'Week Mean Value Of Closing Price (￥).svg', 'Weekday Mean Value Of Closing Price (￥).svg'
    ]:
        html_file.write('   <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
    html_file.write('</body></html>')

