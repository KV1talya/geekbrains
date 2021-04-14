import re

FILE_FOR_PARSE = "nginx_logs.txt"


def parse_file(filename: str):
    """
    raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
    parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
    """
    ip_address_parse = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    date_parse = re.compile(r'\d{1,2}\/[A-Za-z]{1,3}\/\d{4}\:\d{2}\:\d{2}\:\d{2}\s\+\d{4}')
    get_parse = re.compile(r'GET')
    link_parse = re.compile(r'\/[a-z]+\/[a-z]+\_\d')
    code_parse = re.compile(r'[234]\d{2}\s\d{1,4}\s')
    file_open = open(filename, "r", encoding="utf-8")
    for f in file_open.readlines():
        try:
            code, byte, _ = code_parse.findall(f)[0].split(" ")
            yield ip_address_parse.findall(f)[0], date_parse.findall(f)[0], get_parse.findall(f)[0], link_parse.findall(f)[0], code, byte
        except:
            pass
    file_open.close()

if __name__ == '__main__':
    for output in parse_file(FILE_FOR_PARSE):
        print(output)
