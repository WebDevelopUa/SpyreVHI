# coding=utf-8
# Spyre Скрипт, загружающий .csv файл для отображения в табличном виде и гистограмме в веб-браузере
# Spyre - Web Application framework for Python - фреймворк веб-приложений (Python)

# Требования для запуска приложения:
# Python, cherrypy, jinja2, pandas, matplotlib
# pip install dataspyre

# http://127.0.0.1:9091

import pandas as pd
from spyre import server

server.include_df_index = True


class SpyreUploadVHI(server.App):
    # заголовок
    title = "Spyre Upload .csv file with VHI Data"

    # кнопки (для загрузки файла, загрузки данных)
    controls = [{
        "type": "upload",
        "id": "ubutton"
    }, {
        "type": "button",
        "id": "update_data",
        "label": "Get Data | Загрузить данные"
    }
    ]

    # вкладки (для таблицы, графика, инфо)
    tabs = ["Table", "Plot", "Info"]

    # выходные данные (для таблицы, графика, инфо)
    outputs = [
        {
            "type": "table",
            "id": "table_id",
            "control_id": "update_data",
            "tab": "Table",
            "on_page_load": False
        },
        {
            "type": "plot",
            "id": "plot",
            "control_id": "update_data",
            "tab": "Plot",
            "on_page_load": False
        },
        {
            "type": "html",
            "id": "custom_html",
            "tab": "Info"
        }

    ]

    # метод __init__() – конструктор объектов класса
    # self – ссылка на сам только что созданный объект
    # def - инструкция, с помощью которой определяется функция
    # функция в python - объект, принимающий аргументы и возвращающий значение
    # return - инструкция указывающая на то, что нужно вернуть значение
    def __init__(self):
        self.upload_data = None
        self.upload_file = None

    # функция загружает файл .csv, метод read() читает весь файл целиком
    def storeUpload(self, file):
        self.upload_file = file
        self.upload_data = file.read()

    # функция загружает данные из файла .csv в DataFrame
    def getData(self, params):
        df = None
        if self.upload_file is not None:
            self.upload_file.seek(0)
            df = pd.read_csv(self.upload_file,
                             delimiter='\,\s+|\,|\s+',
                             engine='python',
                             index_col=False,
                             names=["year", "week", "SMN", "SMT", "VCI", "TCI", "VHI"])
        return df

    #  функция построения графика
    def getPlot(self, params):
        df = self.getData(params).drop(['SMN', 'SMT'], axis=1).set_index(['week', 'year'])
        plot_obj = df.plot()
        plot_obj.set_ylabel("y - indexes, %")
        plot_obj.set_xlabel("x - selected period (week | year)")
        plot_obj.set_title("Weekly display of Data for the selected period")
        plot_obj.grid()
        line_plot = plot_obj.get_figure()
        return line_plot

    #  функция CSS стилизации страницы в веб-браузере (задается фон)
    def getCustomCSS(self):
        css = (
            "body { background: "
            "linear-gradient(141deg, #0fb8ad 0%, #1fc8db 51%, #2cb5e8 75%) no-repeat fixed; }"
        )
        return css

    #  функция выводит информацию на страницу INFO
    def getHTML(self, params):
        return "<b>О приложении: </b><br/><br/><h1>Создать веб-приложение с использованием модуля Spyre:</h1> <ul><li>выбрать временной ряд VCI, TCI, VHI для набора данных с GetDataVHI (выпадающий список)</li><li>выбрать область, для которой будет выполняться анализ (выпадающий список)</li><li>отметить интервал недель, за которые отбираются данные</li><li>создать несколько вкладок для отображения таблицы с данными на графике изменения индексов</li></ul>"


if __name__ == '__main__':
    app = SpyreUploadVHI()

    # запуск приложения http://127.0.0.1:9091
    app.launch(port=9091)
