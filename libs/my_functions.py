#import requests
#from bs4 import BeautifulSoup
#import pandas as pd

"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

@respond_to("ほめて")
def erai(message):
    message.send("えら～～い！")


@respond_to("バス")
def bus_time_table(message):
    dt_today = datetime.datetime.now()
    dt_now = dt_today.hour
    message.send("次のバスの時間ですか？むぎが教えてあげますよ～！")
    url = "http://bus.shibaura-it.ac.jp/ts/today_sheet.php"
    fetched_dataframes = pd.io.html.read_html(url)
    bus_df = pd.DataFrame(fetched_dataframes[0])
    dt_today = datetime.datetime.now()
    dt_now = dt_today.hour
    message.send("駅前発バスは")
    message.send(str(dt_now) + "時は「"+ bus_df.loc[dt_now-7,"駅前発バス"] +"」で、")
    message.send(str(dt_now+1) + "時は「"+ bus_df.loc[dt_now-6,"駅前発バス"] +"」ですよ！")
    message.send("校舎発バスは")
    message.send(str(dt_now) + "時は「"+ bus_df.loc[dt_now-7,"校舎発バス"] +"」で、")
    message.send(str(dt_now+1) + "時は「"+ bus_df.loc[dt_now-6,"校舎発バス"] +"」ですよ！")
"""