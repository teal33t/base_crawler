from config import MIN_RAND, MAX_RAND

from random import uniform, randint
from time import sleep, time
from datetime import datetime
from fake_useragent import UserAgent, FakeUserAgentError


def wait_between(a=MIN_RAND, b=MAX_RAND):
    rand = uniform(a, b)
    sleep(rand)


def log(s, t=None):
    now = datetime.now()
    if not t:
        t = "Main"
    msg = "%s :: %s -> %s " % (str(now), t, s)
    print(msg)


def random_useragent():
    try:
        ua = UserAgent()
        return ua.random
    except FakeUserAgentError:
        return "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0"
