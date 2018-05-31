# coding=utf-8
# Spyre Скрипт, позволяющий выбирать из списка файл для отображения в табличном виде и на гистограмме в веб-браузере
# https://docs.python.org/3.1/library/csv.html
# https://www.gradient-animator.com/

import pandas as pd
from spyre import server

server.include_df_index = True


class SpyreSelectVHI(server.App):
    # заголовок
    title = "Spyre Select VHI"

    # выпадающий список с файлами из директории .csv (объявлено далее в getData())
    inputs = [{
        "type": "dropdown",
        "id": "file",
        "key": 'file',

        "options": [
            {"label": "2017 | Киевская", "value": '2017-id09-kiev.csv'},
            {"label": "2018 | Киевская", "value": '2018-id09-kiev.csv'},
            {"label": "2017-2018 | Киевская", "value": '2017-2018-id09-kiev.csv'},

            {"label": "Cherkasy | Черкасская", "value": 'new_id_22_2018-05-27_14-33.csv'},
            {"label": "Chernihiv | Черниговская", "value": "new_id_24_2018-05-27_14-33.csv"},
            {"label": "Chernivtsi | Черновицкая", "value": "id_23"},
            {"label": "Crimea | АР Крым", "value": "id_25"},
            {"label": "Dnipropetrovsk | Днепропетровская", "value": "id_03"},
            {"label": "Donetsk | Донецкая", "value": "id_04"},
            {"label": "Ivano-Frankivsk | Ивано-Франковская", "value": "id_08"},
            {"label": "Kharkiv | Харьковская", "value": "id_19"},
            {"label": "Kherson | Херсонская", "value": "id_20"},
            {"label": "Khmelnytskyy | Хмельницкая", "value": "id_21"},
            {"label": "Kiev | Киевская", "value": "id_09"},
            {"label": "Kirovohrad | Кировоградская", "value": "id_10"},
            {"label": "Luhansk | Луганская", "value": "id_11"},
            {"label": "Lviv | Львовская", "value": "id_12"},
            {"label": "Mykolayiv | Николаевская", "value": "id_13"},
            {"label": "Odessa | Одесская", "value": "id_14"},
            {"label": "Poltava | Полтавская", "value": "id_15"},
            {"label": "Rivne | Ровенская", "value": "id_16"},
            {"label": "Sumy | Сумская", "value": "id_17"},
            {"label": "Ternopil | Тернопольская", "value": "id_18"},
            {"label": "Transcarpathia | Закарпатская", "value": "id_06"},
            {"label": "Vinnytsya | Винницкая", "value": "id_01"},
            {"label": "Volyn | Волынская", "value": "id_02"},
            {"label": "Zaporizhzhya | Запорожская", "value": "id_07"},
            {"label": "Zhytomyr | Житомирская", "value": "id_05"},
        ],

        # значение по умолчанию
        "value": "2018-id09-kiev.csv",
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
            "body {  "
            "width: 100wh;"
            "height: 90vh;"
            "color: #fff;"
            "background: linear-gradient(-45deg, #23D5AB, #23A6D5, #ece71b, #36caa4);"
            # "background: linear-gradient(-45deg, #EE7752, #E73C7E, #23A6D5, #23D5AB);"
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
    app = SpyreSelectVHI()

    # запуск приложения http://127.0.0.1:9094
    app.launch(port=9094)
