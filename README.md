# SpyreVHI
### Spyre - Web Application framework for Python | фреймворк веб-приложений (Python)

 http://dataspyre.readthedocs.io/en/latest/
 
 https://github.com/adamhajari/spyre
 
 https://youtu.be/NPV2hHV6hxY
 
 https://github.com/adamhajari/spyre/tree/master/examples
 

#### Requirements | Требования для запуска приложения:

* Python
* cherrypy
* jinja2
* pandas
* matplotlib

```
# pip install dataspyre
```
spyre_install_example.py

 http://127.0.0.1:9090
 
 
spyre_upload_vhi.py

http://127.0.0.1:9091
 
 
spyre_select_file1.py

http://127.0.0.1:9095


spyre_select_region1.py

http://127.0.0.1:9094


spyre_select_region2.py

http://127.0.0.1:9096


spyre_select_region3.py

http://127.0.0.1:9097


spyre_select_region4.py

http://127.0.0.1:9098



------
 
    Create a web application using the Spyre module, which will:
    - select the time series VCI, TCI, VHI for the data set with GetDataVHI (drop-down list)
    - select the area for which the analysis will be performed (drop-down list)
    - note the interval of weeks for which data are selected
    - create multiple tabs to display the table with data on the index change graph
    

------
 
 
    Создать веб-приложение с использованием модуля Spyre, который позволит:
    - выбрать временной ряд VCI, TCI, VHI для набора данных с GetDataVHI (выпадающий список)
    - выбрать область, для которой будет выполняться анализ (выпадающий список)
    - отметить интервал недель, за которые отбираются данные
    - создать несколько вкладок для отображения таблицы с данными на графике изменения индексов


Python2 🐍 + Spyre + Pandas DataFrame = script for Data data processing of indexes (**SMN, SMT, VCI, TCI, VHI**) from the website https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/vh_browseByCountry.php

    VHI (Vegetation Health Index) - вегетационный индекс, основанный на отражении видимого света растительным покровом, которое характеризует степень здоровья растительности

    TCI (Temperature Condition Index)- индекс температурного режима

    VCI (Vegetation Condition Index) - описывает степень подавленности растительного покрова

    SMT (No noise Brightness Temperature)- сглаженная разница растительности

    SMN (No noise Normalized Difference Vegetation Index) - сглаженная яркость температуры
    
    
    
        VHI = 0.5*VCI + 0.5*TCI
    
    
    Содержание VHI-индекса:
    
    VHI <40 - стрессовые условия;
    
    VHI> 60 - благоприятные условия;
    
    VHI <15 - засуха, интенсивность которой зависит от средней до чрезвычайной;
    
    VHI <35 - засуха, интенсивность которой зависит от умеренной до чрезвычайной.