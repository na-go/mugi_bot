# coding: utf-8
import os
# botアカウントのトークンを指定
API_TOKEN = os.environ["Mugi_Slack_API"]
# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
#DEFAULT_REPLY = "日本語で喋ってクレメンス～"
DEFAULT_REPLY = "日本語で喋ってくれメンス～～！"
# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']