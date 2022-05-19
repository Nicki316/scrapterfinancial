import requests
import json

res = requests.get('https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=20220518&selectType=30&_=1652947363427')
print(res.json()['data'])