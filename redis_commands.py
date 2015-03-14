from redis import Redis
from dateutil import parser

ttl = 60*60*1


def _get_connection():
    redis = Redis()
    p = redis.pipeline()
    return p


def set_value(key, value):
    p = _get_connection()
    p.set(key, value, ex=ttl)
    p.execute()


def get_value(key):
    p = _get_connection()
    p.get(key)
    value = p.execute()
    return value[0]


def fix_dates(list):
    for i in list:
        i['date'] = parser.parse(i['date'])
    return list
