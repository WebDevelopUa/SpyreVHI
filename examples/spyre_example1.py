# coding=utf-8
# Spyre - a web application framework for Python - фреймворк веб-приложений (Python) http://127.0.0.1:8080/
# http://dataspyre.readthedocs.io/en/latest/
# https://github.com/adamhajari/spyre
# https://youtu.be/NPV2hHV6hxY

# Требования для запуска приложения:
# Python, cherrypy, jinja2, pandas, matplotlib
# pip install dataspyre

from spyre import server


class SimpleApp(server.App):
    title = "Simple App"
    inputs = [{
        "type": "text",
        "key": "words",
        "label": "write words here",
        "value": "hello world",
        "action_id": "simple_html_output"
    }]

    outputs = [{
        "type": "html",
        "id": "simple_html_output"
    }]

    def getHTML(self, params):
        words = params["words"]
        return "Here's what you wrote in the textbox: <b>%s</b>" % words


app = SimpleApp()
app.launch()
