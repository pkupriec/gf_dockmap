from flask import escape
import helpers
import urllib.request

def get_url_content(request):
    if request.args and 'url' in request.args:
        page = urllib.request.urlopen (request.args.get('url'))
        content = helpers.strip_html(page.read())
        return content
    else:
        return f'No url in request'