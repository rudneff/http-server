class Request:
    def __init__(self, data):
        self.method = data.split(b' ')[0].decode()
        self.headers = self.__extract_headers(data)
        self.host = self.headers.get('Host', '')
        self.url = self.host + data.split(b' ')[1].decode()
        self.query = self.__extract_query()
        self.query_params = self.__extract_query_params()
        self.data = data.split(b'\r\n\r\n')[1]

    def __extract_headers(self, data):
        headers = data.split(b'\r\n\r\n')[0]
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
            values_set = query_params.get(param[0], set());
            values_set.add(param[1])
            query_params.update({param[0]: values_set})
        return query_params
