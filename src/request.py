from urllib.parse import urlparse, unquote, parse_qs


class Request:
    def __init__(self, raw_request):
        self.method = raw_request.split(b' ')[0].decode()
        self.headers = self.__extract_headers(raw_request)
        self.host = self.headers.get('Host', '')
        self.url, self.path, self.query_params = self.__parse_url(raw_request)
        self.data = raw_request.split(b'\r\n\r\n')[1]

    def __parse_url(self, raw_request):
        raw_url = self.host + raw_request.split(b' ')[1].decode()
        if '://' not in raw_url:
            raw_url = '//' + raw_url
        parsed_url = urlparse(raw_url)
        return parsed_url.geturl(), unquote(parsed_url.path), parse_qs(unquote(parsed_url.query))

    def __extract_headers(self, raw_request):
        headers = raw_request.split(b'\r\n\r\n')[0]
        headers = headers.split(b'\r\n')[1:]
        headers_dict = {}
        for header in headers:
            header = header.decode().split(': ')
            headers_dict.update({header[0]: header[1]})
        return headers_dict

    def __extract_query(self):
        query = ''
        temp_list = self.url.split('?', 1)
        if len(temp_list) > 1:
            query = temp_list[1]
        return query

    def __extract_query_params(self):
        query_params = {}
        parameters_list = self.query.split('&')
        for param in parameters_list:
            param = param.split('=')
            values_set = query_params.get(param[0], set())
            values_set.add(param[1])
            query_params.update({param[0]: values_set})
        return query_params
