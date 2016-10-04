import os

#Config
MYSQL_HOST = os.environ.get('MYSQL_HOST', 'mdss.mengsky.net')
MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
MYSQL_USER = os.environ.get('MYSQL_USER', 'ss')
MYSQL_PASS = os.environ.get('MYSQL_PASS', 'ss')
MYSQL_DB = os.environ.get('MYSQL_DB', 'shadowsocks')

MANAGE_PASS = 'ss233333333'
#if you want manage in other server you should set this value to global ip
MANAGE_BIND_IP = '127.0.0.1'
#make sure this port is idle
MANAGE_PORT = 23333