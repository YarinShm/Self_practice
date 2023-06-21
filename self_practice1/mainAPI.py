##-----------run in the Terminal-----------
##pip3 install pytest--- for download pytest
# pip3 install requests - for download requests
import requests



def send_http_requests(url):
    res = requests.get(url)
    return res

def code_side(url):
    code = send_http_requests(url).status_code
    return code

def Check_status_code(code):
    if 199 < code < 400:
        return True
    else:
        return False


def response_headers_contain(url, valu):
    content_type = send_http_requests(url).headers.get('content-type')
    if valu == content_type:
        return True
    else:
        return False


def does_it_valu(url, inside, dictionary):
    valeus = send_http_requests(url).json()
    if inside == valeus[dictionary]:
        return True
    else:
        return False


def does_it_valu_empty(url, dictionary):
    valeus = send_http_requests(url).json()
    if dictionary == "":
        return True
    else:
        return False