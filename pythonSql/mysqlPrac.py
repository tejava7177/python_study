import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='root1234', db='hanbitDB', charset='utf8')

# 커서 생성
cur = conn.cursor()
