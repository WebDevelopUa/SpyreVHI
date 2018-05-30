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
# http://127.0.0.1:9090

from spyre import server


class SpyreInputDisplay(server.App):
    title = "Spyre Input Data Display"
    inputs = [{
        "type": "text",
        "key": "words",
        "label": "изменить значение + ENTER",
        "value": "значение по умолчанию",
        "action_id": "html_output"
    }]

    outputs = [{
        "type": "html",
        "id": "html_output"
    }]

    def getHTML(self, params):
        words = params["words"]
        return "&nbsp; Вот что вы написали в текстовом поле: <br/><br/><br/><b>&nbsp; %s</b>" % words


if __name__ == '__main__':
    app = SpyreInputDisplay()

    # запуск приложения http://127.0.0.1:9090
    app.launch(port=9090)
