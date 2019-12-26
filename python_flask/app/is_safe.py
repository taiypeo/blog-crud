from werkzeug.urls import url_parse


def is_safe(url):
    return url and url_parse(url).netloc == ""
