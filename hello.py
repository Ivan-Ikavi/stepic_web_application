def wsgi_app(env, start_responce):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    data = environ['QUERY_STRING'].split('&')
    body = '\r\n'.join(data).encode('utf-8')
    start_responce(status, headers)
    return [body]
