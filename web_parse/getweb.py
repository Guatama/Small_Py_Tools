import requests
from lxml.html import fromstring
from bs4 import BeautifulSoup


def get_title(url, url_scheme=None):
    """
    Sends an http-get request and returns text from <title> - tag of the url page.

    Optional keyword arguments:
    url_scheme: str -> 'http://' or 'https://' (defult None)
    """
    try:
        if url_scheme is not None:
            url = url_scheme + url
        r = requests.get(url, headers={ 'User-Agent' : 'Mozilla'})
        # r.encoding = 'UTF-8'
        code = "< " + str(r.status_code) + " >"
        tree = fromstring(r.text)
        title = tree.findtext('.//title')
    except Exception as e:
        code = "< {} >".format(str(e))
        title = "< none >"
    title = title.strip()

    # A rough way to deal with non-utf-8 titles
    try:
        title = title.encode(encoding="ISO-8859-1").decode()
    except:
        pass
    return title, code


def get_title_noscheme(url):
    schemes = ['http://', 'https://']
    if url.find(schemes[0]) == 0 or url.find(schemes[1]) == 0:
        schemes = ['']

    for scheme in schemes:
        try:
            title, code = get_title(url, scheme)
            if len(scheme) > 1:
                code = str(code) + " (scheme add: " + scheme + ")"
            else:
                code = str(code)
            break
        except Exception as e:
            if len(scheme) > 1:
                code = "< url unavailable > (scheme add: " + scheme + ") "
            else:
                code = "< url unavailable > "
            title = "< none >"
            continue

    return title, code