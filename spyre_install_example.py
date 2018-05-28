# coding=utf-8
# Создать веб-приложение с использованием модуля Spyre, который позволит:
# выбрать временной ряд VCI, TCI, VHI для набора данных с GetDataVHI (выпадающий список)
# выбрать область, для которой будет выполняться анализ (выпадающий список)
# отметить интервал недель, за которые отбираются данные
# создать несколько вкладок для отображения таблицы с данными на графике изменения индексов

# Spyre - Web Application framework for Python - фреймворк веб-приложений (Python)
# http://dataspyre.readthedocs.io/en/latest/
# https://github.com/adamhajari/spyre
# https://youtu.be/NPV2hHV6hxY

# Требования для запуска приложения:
# Python, cherrypy, jinja2, pandas, matplotlib
# pip install dataspyre
# http://127.0.0.1:8080/

from spyre import server


class SpyreVHI(server.App):
    title = "Spyre VHI"
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


app = SpyreVHI()
app.launch()
