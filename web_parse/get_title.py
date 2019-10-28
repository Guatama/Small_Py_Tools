from getweb import get_title_noscheme
import csv


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
