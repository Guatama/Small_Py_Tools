import requests
import csv
from lxml.html import fromstring


def get_title(url):
    try:
        r = requests.get(url, headers={ 'User-Agent' : 'Mozilla'})
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
    scheme = ['http://', 'https://']
    if url.find(scheme[0]) == 0 or url.find(scheme[1]) == 0:
        scheme = [""]

    for i in scheme:
        url_with_scheme = i + url
        try:
            title, code = get_title(url_with_scheme)
            if len(scheme) > 1:
                code = str(code) + " (scheme add: " + i + ")"
            else:
                code = str(code)
            break
        except Exception as e:
            if len(scheme) > 1:
                code = "< url unavailable > (scheme add: " + i + ") "
            else:
                code = "< url unavailable > "
            title = "< none >"
            continue

    return title, code


if __name__ == '__main__':
    input = []
    
    with open('input.tsv', 'r', encoding='utf-8') as input_file:
        for line in input_file:
            input.append(line.strip())


    with open('result.tsv', 'w', encoding="utf-8", newline="") as file:
        res_writer = csv.writer(file, delimiter='\t')
        res_writer.writerow(["url", "url_title", "url_code"])
        counter = 0
        for url in input:
            title, code = get_title_noscheme(url)
            counter += 1
            print("{:2} |  {:3} {}".format(str(counter), str(code), url))
            res_writer.writerow([code, url, title])
