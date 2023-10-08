import json
import allure
from allure_commons.types import AttachmentType
from requests import sessions
from curlify import to_curl


def api_request(method, url, **kwargs):
    base_url = 'https://reqres.in/api'
    new_url = base_url + url
    with allure.step(f"{method.upper()} {new_url}"):
        with sessions.Session() as session:
            response = session.request(method=method, url=new_url, **kwargs)
            message = to_curl(response.request)
            allure.attach(body=message.encode("utf-8"), name="Curl", attachment_type=AttachmentType.TEXT, extension='txt')
            if not response.content:
                allure.attach(body='empty response',
                              name='Empty Response',
                              attachment_type=AttachmentType.TEXT,
                              extension='txt')
            else:
                allure.attach(body=json.dumps(response.json(), indent=4).encode("utf-8"),
                              name="Response Json",
                              attachment_type=AttachmentType.JSON,
                              extension='json')
    return response
