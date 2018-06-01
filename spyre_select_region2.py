# coding=utf-8
# Spyre Скрипт, позволяющий выбирать из списка регион и год для отображения в табличном виде и на гистограмме
# https://docs.python.org/3.1/library/csv.html
# https://jeffdelaney.me/blog/useful-snippets-in-pandas/

import pandas as pd
from spyre import server

server.include_df_index = True


class SpyreSelectYear(server.App):
    # заголовок
    title = "Spyre Select Year"

    # выпадающий список с файлами из директории .csv ("csv/" - объявлено далее в getData())
    inputs = [

        # выпадающий список (регионы)
        {
            "type": "dropdown",
            "id": "file",
            "label": "Область",
            "key": 'file',

            "options": [
                {"label": "2017 | Киевская", "value": '2017-id09-kiev.csv'},
                {"label": "2018 | Киевская", "value": '2018-id09-kiev.csv'},
                {"label": "2017-2018 | Киевская", "value": '2017-2018-id09-kiev.csv'},

                {"label": "Cherkasy | Черкасская", "value": 'new_id_22_2018-05-27_14-33.csv'},
                {"label": "Chernihiv | Черниговская", "value": "new_id_24_2018-05-27_14-33.csv"},
                {"label": "Chernivtsi | Черновицкая", "value": "new_id_23_2018-05-27_14-33.csv"},
                {"label": "Crimea | АР Крым", "value": "new_id_25_2018-05-27_14-33.csv"},
                {"label": "Dnipropetrovsk | Днепропетровская", "value": "new_id_03_2018-05-27_14-33.csv"},
                {"label": "Donetsk | Донецкая", "value": "new_id_04_2018-05-27_14-33.csv"},
                {"label": "Ivano-Frankivsk | Ивано-Франковская", "value": "new_id_08_2018-05-27_14-33.csv"},
                {"label": "Kharkiv | Харьковская", "value": "new_id_19_2018-05-27_14-33.csv"},
                {"label": "Kherson | Херсонская", "value": "new_id_20_2018-05-27_14-33.csv"},
                {"label": "Khmelnytskyy | Хмельницкая", "value": "new_id_21_2018-05-27_14-33.csv"},
                {"label": "Kiev | Киевская", "value": "new_id_09_2018-05-27_14-33.csv"},
                {"label": "Kirovohrad | Кировоградская", "value": "new_id_10_2018-05-27_14-33.csv"},
                {"label": "Luhansk | Луганская", "value": "new_id_11_2018-05-27_14-33.csv"},
                {"label": "Lviv | Львовская", "value": "new_id_12_2018-05-27_14-33.csv"},
                {"label": "Mykolayiv | Николаевская", "value": "new_id_13_2018-05-27_14-33.csv"},
                {"label": "Odessa | Одесская", "value": "new_id_14_2018-05-27_14-33.csv"},
                {"label": "Poltava | Полтавская", "value": "new_id_15_2018-05-27_14-33.csv"},
                {"label": "Rivne | Ровенская", "value": "new_id_16_2018-05-27_14-33.csv"},
                {"label": "Sumy | Сумская", "value": "new_id_17_2018-05-27_14-33.csv"},
                {"label": "Ternopil | Тернопольская", "value": "new_id_18_2018-05-27_14-33.csv"},
                {"label": "Transcarpathia | Закарпатская", "value": "new_id_06_2018-05-27_14-33.csv"},
                {"label": "Vinnytsya | Винницкая", "value": "new_id_01_2018-05-27_14-33.csv"},
                {"label": "Volyn | Волынская", "value": "new_id_02_2018-05-27_14-33.csv"},
                {"label": "Zaporizhzhya | Запорожская", "value": "new_id_07_2018-05-27_14-33.csv"},
                {"label": "Zhytomyr | Житомирская", "value": "new_id_05_2018-05-27_14-33.csv"},
            ],

            # значение по умолчанию
            "value": "2018-id09-kiev.csv",
            "action_id": "update_data"
        },

        # выпадающий список (годы)
        {
            "type": "dropdown",
            "id": "year",
            "label": "Год",
            "options": [
                {"label": year, "value": year} for year in range(1981, 2019)
            ],
            "key": "year",
            "action_id": "update_data"
        }

    ]

    # кнопка ("Get Data | Загрузить данные")
    controls = [{
        "type": "button",
        "id": "update_data",
        "label": "Get Data | Загрузить данные"
    }]

    # вкладки  (таблица, график, инфоблок)
    tabs = ["Table", "Plot", "Info"]

    # выходные данные (в таблицу, на график, в инфоблок)
    outputs = [

        {
            "type": "table",
            "id": "table_id",
            "control_id": "update_data",
            "tab": "Table",
            "on_page_load": True
        },

        {
            "type": "plot",
            "id": "plot",
            "control_id": "update_data",
            "tab": "Plot"},

        {
            "type": "html",
            "id": "custom_html",
            "tab": "Info"
        }

    ]

    #  функция считывания данных из файла (в DataFrame)
    def getData(self, params):
        filename = params["file"]
        year = int(params["year"])

        df = pd.read_csv("csv/" + filename,
                         delimiter='\,\s+|\,|\s+',
                         engine='python',
                         index_col=False,
                         names=["year", "week", "SMN", "SMT", "VCI", "TCI", "VHI"]
                         )
        # метод Pandas .ix (и .loc, iloc) позволяет выбрать конкретное значение «ячейки» (в DataFrame)
        df = df.ix[df.year == year]
        return df

    #  функция построения графика
    def getPlot(self, params):
        df = self.getData(params).drop(['year', 'SMN', 'SMT'], axis=1).set_index(['week'])
        plot_obj = df.plot()
        plot_obj.set_ylabel("y - indexes, %")
        plot_obj.set_xlabel("x - selected period (week | year)")
        plot_obj.set_title("Weekly display of Data for the selected period")
        # plot_obj.grid()
        line_plot = plot_obj.get_figure()
        return line_plot

    # метод стилизации
    def getCustomCSS(self):
        css = (
            "body {  "
            "width: 100wh;"
            "height: 90vh;"
            "color: #29298c;"
            "background: linear-gradient(-45deg, #23D5AB, #23A6D5, #ece71b, #36caa4);"
            "background-size: 400% 400%;"
            "-webkit-animation: Gradient 15s ease infinite;"
            "-moz-animation: Gradient 15s ease infinite;"
            "animation: Gradient 15s ease infinite;"
            "}"
            "@-webkit-keyframes Gradient {"
            "	0% {"
            "		background-position: 0% 50%"
            "	}"
            "	50% {"
            "		background-position: 100% 50%"
            "}"
            "100% {"
            "background-position: 0% 50%"
            "}"
            "}"
            "@-moz-keyframes Gradient {"
            "0% {"
            "background-position: 0% 50%"
            "}"
            "50% {"
            "background-position: 100% 50%"
            "}"
            "100% {"
            "background-position: 0% 50%"
            "}"
            "}"
            "@keyframes Gradient {"
            "0% {"
            "background-position: 0% 50%"
            "}"
            "	50% {"
            "background-position: 100% 50%"
            "}"
            "100% {"
            "background-position: 0% 50%"
            "}"
            "}"

        )
        return css

    # метод выводит информацию на страницу INFO
    def getHTML(self, params):
        return "<b>О приложении: </b><br/><br/><h1>Создать веб-приложение с использованием модуля Spyre:</h1> <ul><li>выбрать временной ряд VCI, TCI, VHI для набора данных с GetDataVHI (выпадающий список)</li><li>выбрать область, для которой будет выполняться анализ (выпадающий список)</li><li>отметить интервал недель, за которые отбираются данные</li><li>создать несколько вкладок для отображения таблицы с данными на графике изменения индексов</li></ul>"


if __name__ == '__main__':
    app = SpyreSelectYear()

    # запуск приложения http://127.0.0.1:9096
    app.launch(port=9096)
