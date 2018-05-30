# coding=utf-8
# Spyre Скрипт, позволяющий выбирать из списка файл для отображения в табличном виде и на гистограмме в веб-браузере
# https://docs.python.org/3.1/library/csv.html

import os
import pandas as pd
from spyre import server

server.include_df_index = True


class SpyreSelectVHI(server.App):
    # путь к директории с файлами
    path = "csv"

    # заголовок
    title = "Spyre Select VHI"

    # выпадающий список с файлами из директории path (объявлено выше)
    inputs = [{
        "type": "dropdown",
        "id": "file",
        "key": 'file',

        "label": "Область",
        "options": [
            {"label": filename, "value": filename} for filename in os.listdir(path)
        ],

        # значение по умолчанию
        "value": "new_id.csv",
        "action_id": "update_data"
    }]

    # кнопка ("Get Data | Загрузить данные")
    controls = [{
        "type": "button",
        "id": "update_data",
        "label": "Get Data | Загрузить данные"
    }]

    # вкладки
    tabs = ["Table", "Plot", "Info"]

    # выходные данные
    outputs = [
        {
            "type": "plot",
            "id": "plot",
            "control_id": "update_data",
            "tab": "Plot"},
        {
            "type": "table",
            "id": "table_id",
            "control_id": "update_data",
            "tab": "Table",
            "on_page_load": True
        },
        {
            "type": "html",
            "id": "custom_html",
            "tab": "Info"
        }

    ]

    def getData(self, params):
        filename = params["file"]
        df = pd.read_csv("csv/" + filename,
                         delimiter='\,\s+|\,|\s+',
                         engine='python',
                         index_col=False,
                         names=["year", "week", "SMN", "SMK", "VCI", "TCI", "VHI"]
                         )
        return df

    #  функция построения графика
    def getPlot(self, params):
        df = self.getData(params).drop(['SMN', 'SMK'], axis=1).set_index(['week', 'year'])
        plt_obj = df.plot()
        plt_obj.set_ylabel("y - indexes, %")
        plt_obj.set_xlabel("x - selected period (week | year)")
        plt_obj.set_title("Weekly display of Data for the selected period")
        plt_obj.grid()
        fig = plt_obj.get_figure()
        return fig

    # метод стилизации
    def getCustomCSS(self):
        css = (
            "body { background: "
            "linear-gradient(141deg, #0fb8ad 0%, #1fc8db 51%, #2cb5e8 75%) no-repeat fixed; }"
        )
        return css

    # метод выводит информацию на страницу INFO
    def getHTML(self, params):
        return "<b>О приложении: </b><br/><br/><h1>Создать веб-приложение с использованием модуля Spyre:</h1> <ul><li>выбрать временной ряд VCI, TCI, VHI для набора данных с GetDataVHI (выпадающий список)</li><li>выбрать область, для которой будет выполняться анализ (выпадающий список)</li><li>отметить интервал недель, за которые отбираются данные</li><li>создать несколько вкладок для отображения таблицы с данными на графике изменения индексов</li></ul>"


if __name__ == '__main__':
    app = SpyreSelectVHI()

    # запуск приложения http://127.0.0.1:9095
    app.launch(port=9095)