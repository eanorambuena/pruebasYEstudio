import webview # pip install pywebview

URL = 'index_py.html'

TITLE = URL

webview.create_window(TITLE, URL)

webview.start()
help(webview)
while True:
    webview.wait_load()
