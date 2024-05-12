from requests.auth import HTTPBasicAuth


class RequestBuilder:

    def __init__(self, url) -> None:
        self.url = url

    def _build_endpoint(self,
                        endpoint: str | None,
                        query_string: dict | None) -> str:

        url = url = self.url + (endpoint or "")

        if query_string:
            encoded_query = '&'.join([
                f"{key}={value}" for key, value in query_string.items()
                ])

            url = '{}{}'.format(url, f'?{encoded_query}')

        return url

    def _build_headers(self, data: str | None) -> dict:
        headers = {'Accept': 'application/json'}

        if data:
            headers.update({
                'Content-Type': 'application/x-www-form-urlencoded'
                })
        else:
            headers.update({'Content-Type': 'application/json'})

        return headers

    def build_request(self,
                      method: str,
                      endpoint: str = None,
                      query_string: dict = None,
                      access_token: str = None,
                      username: str = None,
                      password: str = None,
                      **kwargs) -> dict:

        headers = self._build_headers(kwargs.get('data', None))

        if access_token:
            headers.update({
                'Authorization': f'Bearer {access_token}'
                })

        elif username and password:
            kwargs['auth'] = HTTPBasicAuth(username, password)

        kwargs['method'] = method
        kwargs['headers'] = headers
        kwargs['url'] = self._build_endpoint(endpoint, query_string)

        return kwargs
