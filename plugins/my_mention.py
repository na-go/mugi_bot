from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
from libs import my_functions           # 外部関数の読み込み



@respond_to("おはよ")
def today(message):
    today = datetime.datetime.today().strftime("%Y年%m月%d日")
    message.send("おはようございます。今日は" + str(today) + "です。 今日も一日お疲れの出ませんように……。")


@respond_to("ほあよ")
def today(message):
    today = datetime.datetime.today().strftime("%Y年%m月%d日")
    message.send("おはようございます。今日は" + str(today) + "です。 今日も一日お疲れの出ませんように……。")

@respond_to("ほめて")
def erai(message):
    message.send("えら～～い！")

@respond_to("バス")
def bus_time_table(message):
    dt_today = datetime.datetime.now()
    dt_now = dt_today.hour
    url = "http://bus.shibaura-it.ac.jp/ts/today_sheet.php"
    fetched_dataframes = pd.read_html(url)
    bus_df = pd.DataFrame(fetched_dataframes[0])
    dt_today = datetime.datetime.now()
    dt_now = dt_today.hour
    #message.send(dt_now)
    label = dt_now-7
    
    if (label >= 0) & (label < 14):
        message.send("次のバスの時間ですか？むぎが教えてあげますよ～！\n駅前発バスは\n" + str(dt_now) + "時は「"+ bus_df.loc[label,"駅前発バス"] +"」で、\n" + str(dt_now+1) + "時は「"+ bus_df.loc[label + 1,"駅前発バス"] +"」ですよ！\n校舎発バスは\n" + str(dt_now) + "時は「"+ bus_df.loc[label,"校舎発バス"] +"」で、\n" + str(dt_now+1) + "時は「"+ bus_df.loc[label+1,"校舎発バス"] +"」ですよ！")
    elif label == 14:
        message.send("次のバスの時間ですか？むぎが教えてあげますよ～！\n駅前発バスは\n" + str(dt_now) + "時は「"+ bus_df.loc[label,"駅前発バス"] +"」で、\n" + str(dt_now+1) + "時は「"+ bus_df.loc[label + 1,"駅前発バス"] +"」ですよ！\n校舎発バスは\n" + str(dt_now) + "時は「"+ bus_df.loc[label,"校舎発バス"] +"」ですよ！\nこのあとはもうバスないから気をつけてクレメンス～～～ｗ")
    
    else:
        message.send("今は走ってませんよ～！")

@respond_to("ばす")
def bus_time_table(message):
    dt_today = datetime.datetime.now()
    dt_now = dt_today.hour
    url = "http://bus.shibaura-it.ac.jp/ts/today_sheet.php"
    fetched_dataframes = pd.read_html(url)
    bus_df = pd.DataFrame(fetched_dataframes[0])
    dt_today = datetime.datetime.now()
    dt_now = dt_today.hour
    #message.send(dt_now)
    label = dt_now-7
    
    if (label >= 0) & (label < 14):
        message.send("次のバスの時間ですか？むぎが教えてあげますよ～！\n駅前発バスは\n" + str(dt_now) + "時は「"+ bus_df.loc[label,"駅前発バス"] +"」で、\n" + str(dt_now+1) + "時は「"+ bus_df.loc[label + 1,"駅前発バス"] +"」ですよ！\n校舎発バスは\n" + str(dt_now) + "時は「"+ bus_df.loc[label,"校舎発バス"] +"」で、\n" + str(dt_now+1) + "時は「"+ bus_df.loc[label+1,"校舎発バス"] +"」ですよ！")
    elif label == 14:
        message.send("次のバスの時間ですか？むぎが教えてあげますよ～！\n駅前発バスは\n" + str(dt_now) + "時は「"+ bus_df.loc[label,"駅前発バス"] +"」で、\n" + str(dt_now+1) + "時は「"+ bus_df.loc[label + 1,"駅前発バス"] +"」ですよ！\n校舎発バスは\n" + str(dt_now) + "時は「"+ bus_df.loc[label,"校舎発バス"] +"」ですよ！\nこのあとはもうバスないから気をつけてクレメンス～～～ｗ")
    
    else:
        message.send("今は走ってませんよ～！")