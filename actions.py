from config import MIN_RAND, MAX_RAND, API_KEY

from random import uniform, randint
from time import sleep, time
from datetime import datetime
from fake_useragent import UserAgent, FakeUserAgentError
from anticaptchaofficial.hcaptchaproxyless import *


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


def resolve_hcaptcha(SITE_KEY):
    solver = hCaptchaProxyless()
    solver.set_verbose(1)
    solver.set_key(API_KEY)
    solver.set_website_url("https://website.com")
    solver.set_website_key(SITE_KEY)

    g_response = solver.solve_and_return_solution()
    if g_response != 0:
        print("g-response: " + g_response)
    else:
        print("task finished with error " + solver.error_code)

def get_proxy():
    pass