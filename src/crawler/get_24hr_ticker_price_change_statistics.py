from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model import *
import pandas as pd
import time
import os
from binance.client import Client
import csv

i = 0
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

client = Client(api_key, api_secret)
#client.API_URL = 'https://testnet.binance.vision/api'
timestamp = client._get_earliest_valid_timestamp('DOGEUSDT', '1d')
doge = client.get_historical_klines('DOGEUSDT', '1d', timestamp, limit=1000)
#btc_df = pd.DataFrame(btc)
doge_df = pd.DataFrame(doge, columns=['openTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numTrades', 'takerBuyBaseAssetVolume', 'takerBuyQuoteAssetVolume', 'ignore'])
doge_df.set_index('openTime', inplace=True)
print(doge_df.head())
doge_df.to_csv('DOGEUSDT_t1d.csv')






# Generate API Object for Download Kline
#request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)



# 設定參數
'''symbol = 'BNBUSDT'
start_time = 1626429600000  # 開始:    2021年7月16日 10:00:00
end_time = 1626459600000  # 結束:      2021年7月16日 18:20:00  以Endtime為基準到回去跑
min_diff = 60000
times = 1500
times_diff = end_time-start_time
start_time = start_time-(times_diff*(times-1))
end_time = start_time+times_diff


# 印出Kline載下來的資料統整

def print_obj(obj):
    if not obj:
        return -1
    dict_r = {}
    members = [attr for attr in dir(obj) if not callable(
        attr) and not attr.startswith("__")]
    for member_def in members:
        val_str = str(getattr(obj, member_def))
        dict_r[member_def] = val_str
        #print(member_def + ":" + val_str)
    return dict_r


# 循環爬取過往資料

for i in range(0, times, 1):
    print(start_time, end_time)
    result_list = []
    r = request_client.get_candlestick_data(
        symbol=symbol, startTime=start_time, endTime=end_time, limit=500, interval=CandlestickInterval.MIN1)

    print('temp', len(r))
    if((start_time != r[0].openTime) or (end_time != r[-1].openTime)):
        print(i, len(r))
        break
    time.sleep(1)
    for index, row in enumerate(r):
        temp = print_obj(row)
        result_list.append(temp)

    df = pd.DataFrame(result_list)

    if(i == 0):
        df.to_csv('BNBUSDT_m7d16_.csv')
    else:
        df.to_csv('BNBUSDT_m7d16_.csv', mode='a', header=False)

    if(len(r) != 500):
        print(i, len(r))
        break

    start_time = end_time+min_diff        #調整時間從一開始跑8小時500筆資料
    end_time = start_time+times_diff
    print(df.shape, i)'''

# df.head()
# df.tail()


# dftemp=df.drop(columns=['json_parse'])
# dftemp.to_csv('t3.csv')


# PrintMix.print_data(result)
