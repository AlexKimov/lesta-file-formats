# Описание
Описание форматов игровых ресурсов и инструменты для их просмотра для игр Lesta Studio.

### Краткое ввдение в форматы файлов 

##### Антанта 

###### Архив игровых ресурсов
Часть игровых файлов помещена в архив с раширением .les. Для сжатия применен DEFLATE.

###### Графика  
В игре используется двухмерная изометрическая графика на основе изображений, полученных из 
трехмерных моделей. Для хранения создано несколько форматов (.egr, .ogr, .ugr и другие), некоторые из которых используют
сжатие данных на основе RLE.  

### Задачи:  

##### Антанта  
- Анализ форматов    

    [+] Архив ресурсов  
    [+] Изображения (.egr, .ogr, .ugr и т.д.)  

- Инструменты для просмотра файлов  

    [+] Изображения объектов  
    [+] Распаковка игровых архивов  
      
### Вопросы/Ответы    
  1. Как открыть файлы из игры Антанта (2003)?  
    Распаковать с помощью скрипта ([ссылка](#quickbms)). Открыть нужный файл с помощью плагина ([ссылка](#noesis)).
      
## Форматы  

**1. Антанта (2003)**  

| № | Формат файла       | Шаблон (010Editor)     |   Описание |
| :--- | :--------- | :----------- |  :---------- | 
| 1 | .egr  | [EGR.bt](https://github.com/AlexKimov/lesta-file-formats/blob/main/templates/010%20editor/EGR.bt) | изображения эффектов |
| 2 | .img  | [IMG.bt](https://github.com/AlexKimov/lesta-file-formats/blob/main/templates/010%20editor/IMG.bt) | изображения зданий |
| 3 | .les  | [LES.bt](https://github.com/AlexKimov/lesta-file-formats/blob/main/templates/010%20editor/LES.bt) | архив игровых ресурсов |
| 4 | .ogr  | [OGR.bt](https://github.com/AlexKimov/lesta-file-formats/blob/main/templates/010%20editor/OGR.bt) | изображения объектов |
| 5 | .ugr  | [UGR.bt](https://github.com/AlexKimov/lesta-file-formats/blob/main/templates/010%20editor/UGR.bt) | изображения юнитов |

## Инструменты

### Quickbms

| № | Формат  | Инструмент |    Описание |
| :--- | :--------- | :----------- | :---------- | 
| 1 | .les | [antanta_unpack_les.bms](https://github.com/AlexKimov/lesta-file-formats/tree/main/scripts/bms/antanta_unpack_les.bms)  | quickbms | Распаковка архива игровых ресурсов |


    Как использовать quickbms скрипты
    1. Нужен quickbms https://aluigi.altervista.org/quickbms.htm
    2. Для запуска в репозитории лежит bat файл с настройками, нужно открыть его и задать свои пути: до места, где находится quickbms, папки с игрой и места куда нужно сохранить результат.
    3. Запустить процесс через bat файл или вручную (задав свои параметры для запуска quickbms, документация на английском есть здесь https://aluigi.altervista.org/papers/quickbms.txt ). 


### Noesis

| № | Формат  | Инструмент |     Описание |
| :--- | :--------- | :----------- | :---------- | 
| 2 | .444 | [fmt_ant_444.py](https://github.com/AlexKimov/lesta-file-formats/tree/main/plugins/noesis/fmt_ant_444.py)  | Просмотр .444 файлов |
| 3 | .egr | [fmt_ant_egr.py](https://github.com/AlexKimov/lesta-file-formats/tree/main/plugins/noesis/fmt_ant_egr.py)  | Просмотр изображений эффекторв .egr |
| 4 | .img | [fmt_ant_img.py](https://github.com/AlexKimov/lesta-file-formats/tree/main/plugins/noesis/fmt_ant_img.py)  | Просмотр изображений зданий .img |
| 5 | .ogr | [fmt_ant_ogr.py](https://github.com/AlexKimov/lesta-file-formats/tree/main/plugins/noesis/fmt_ant_ogr.py)  | Просмотр изображений объектов  .ogr |
| 6 | .ugr | [fmt_ant_ugr.py](https://github.com/AlexKimov/lesta-file-formats/tree/main/plugins/noesis/fmt_ant_ugr.py)  | Просмотр изображений юнитов .ugr |

    Как использовать Noesis плагины
    1. Скачать Noesis https://richwhitehouse.com/index.php?content=inc_projects.php&showproject=91 .
    2. Скопировать скрипт в папку ПапкасNoesis/plugins/python.
    3. Открыть Noesis.
    4. Открыть файл через File-Open.