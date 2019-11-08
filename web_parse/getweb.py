import requests
import re
from lxml.html import fromstring


def get_title(url, url_scheme=None):
    """
    Sends an http-get request and returns text from <title> - tag of the url page.

    Optional keyword arguments:
    url_scheme: str -> 'http://' or 'https://' (defult None)
    """
    try:
        if url_scheme is not None:
            url = url_scheme + url
        r = requests.get(url, headers={ 'User-Agent' : 'Mozilla' })        # r.encoding = 'UTF-8'
        code = "< " + str(r.status_code) + " >"
        match = re.search('<(title|Title|TITLE).*?>(.*?)</(title|Title|TITLE)>', r.text)
        title = match.group(2) if match else '< none >'
    except Exception as e:
        code = "< {} >".format(str(e))

    if title is None:
        title = "< none >"
    title = title.strip()

    # A rough way to deal with non-utf-8 titles
    try:
        title = title.encode(encoding="ISO-8859-1").decode()
    except:
        pass
    return title, code


def get_title_lxml(url, url_scheme=None):
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

    if title is None:
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