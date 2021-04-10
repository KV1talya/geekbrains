from requests import get


def get_response():
    response_text = get(
        "https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs").text
    for gen in response_text.split("\n"):
        yield gen


def processing_response():
    for data_in_response in get_response():
        try:
            _ip_address, _request, code_response, _, _, user_agent, _ = data_in_response.split('"')
            ip_address = _ip_address.split(" ")[0]
            type_request, link_request, http_protocol = _request.split(" ")
            yield ip_address, type_request, link_request
        except ValueError:
            pass


def find_spammer():
    pass


for data in processing_response():
    print(data)
