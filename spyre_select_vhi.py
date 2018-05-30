# coding=utf-8
# Spyre Скрипт, позволяющий выбирать из списков параметры для отображения в табличном виде и гистограмме в веб-браузере

import pandas as pd
from spyre import server
from googlefinance.client import get_price_data

server.include_df_index = True


class SpyreVHI(server.App):
    # заголовок
    title = "Spyre VHI"

    # выпадающий список с областями
    inputs = [{
        "type": "dropdown",
        "label": "Область",
        "options": [
            {"label": "Cherkasy | Черкасская", "value": "id_22"},
            {"label": "Chernihiv | Черниговская", "value": "id_24"},
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
            {"label": "Amazon", "value": "AMZN"},
            {"label": "Apple", "value": "AAPL"}],
        # "value": "id_12",
        "value": "AMZN",
        "key": 'ticker',
        "action_id": "update_data"
    }]

    # кнопка
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

    # метод получения данных данные
    def getData(self, params):
        ticker = params['ticker']
        if ticker == 'empty':
            ticker = params['custom_ticker'].upper()

        xchng = "NASD"
        param = {
            'q': ticker,  # Stock symbol (ex: "AAPL")
            'i': "86400",  # Interval size in seconds ("86400" = 1 day intervals)
            'x': xchng,  # Stock exchange symbol on which stock is traded (ex: "NASD")
            'p': "3M"  # Period (Ex: "1Y" = 1 year)
        }
        df = get_price_data(param)
        return df

    # метод построения графика
    def getPlot(self, params):
        df = self.getData(params).drop(['Volume'], axis=1)
        plt_obj = df.plot()
        plt_obj.set_ylabel("Price")
        plt_obj.set_xlabel("Date")
        plt_obj.set_title(params['ticker'])
        return plt_obj.get_figure()

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
    app = SpyreVHI()

    # запуск приложения http://127.0.0.1:9096
    app.launch(port=9096)
