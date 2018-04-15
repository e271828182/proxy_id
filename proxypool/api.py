from flask import Flask, g

from .db import RedisClient
import requests
import re

__all__ = ['app']

app = Flask(__name__)


def get_conn():
    """
    Opens a new redis connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'redis_client'):
        g.redis_client = RedisClient()
    return g.redis_client


@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/get')
def get_proxy():
    """
    Get a proxy
    """
    conn = get_conn()
    if conn.pop():
        html = requests.get('http://ip.chinaz.com/%s' % str(conn.pop())).text
        ip_adress = re.compile("""<span class="Whwtdhalf w50-0">(.*?)</span>""")
        re_ip_adress = ip_adress.findall(html)
    return conn.pop()+'<br/>'+str(re_ip_adress)


@app.route('/count')
def get_counts():
    """
    Get the count of proxies
    """
    conn = get_conn()
    return str(conn.queue_len)


if __name__ == '__main__':
    app.run()
