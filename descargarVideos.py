import webbrowser

url = "https://www.youtube.com/watch?v=WnwKXXfFnvM"

download=url[:12]+"ss"+url[12:]

webbrowser.open(download)