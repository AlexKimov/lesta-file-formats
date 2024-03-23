# Описание
Форматы и плагины для просмотра файлов игр Lesta Studio.

## Игры и форматы

**1. Антанта (2003)**

| № | Формат файла       | Шаблон (010Editor)     |   Описание |
| :--- | :--------- | :----------- |  :---------- | 
| 1 | .egr  | [EGR.bt](https://github.com/AlexKimov/lesta-file-formats/tree/main/templates/010%20editor/EGR.bt) | изображения эффектов |
| 2 | .img  | [IMG.bt](https://github.com/AlexKimov/lesta-file-formats/tree/main/templates/010%20editor/IMG.bt) | изображения зданий |
| 3 | .les  | [LES.bt](https://github.com/AlexKimov/lesta-file-formats/tree/main/templates/010%20editor/LES.bt) | архив игровых ресурсов |
| 4 | .ogr  | [OGR.bt](https://github.com/AlexKimov/lesta-file-formats/tree/main/templates/010%20editor/OGR.bt) | изображения объектов |
| 5 | .ugr  | [UGR.bt](https://github.com/AlexKimov/lesta-file-formats/tree/main/templates/010%20editor/UGR.bt) | изображения юнитов |

## Инструменты

| № | Формат  | Инструмент |  Программа   |   Описание |
| :--- | :--------- | :----------- | :---------- | :---------- | 
| 1 | .les | [antanta_unpack_les.bms](https://github.com/AlexKimov/lesta-file-formats/tree/main/scripts/bms/antanta_unpack_les.bms)  | quickbms | Распаковка архива игровых ресурсов |
| 2 | .444 | [fmt_ant_444.py](https://github.com/AlexKimov/lesta-file-formats/tree/main/plugins/noesis/fmt_ant_444.py)  | noesis | Просмотр .444 файлов |
| 3 | .egr | [fmt_ant_egr.py](https://github.com/AlexKimov/lesta-file-formats/tree/main/plugins/noesis/fmt_ant_egr.py)  | noesis | Просмотр изображений эффекторв |
| 4 | .img | [fmt_ant_img.py](https://github.com/AlexKimov/lesta-file-formats/tree/main/plugins/noesis/fmt_ant_img.py)  | noesis | Просмотр изображений зданий |
| 5 | .ogr | [fmt_ant_ogr.py](https://github.com/AlexKimov/lesta-file-formats/tree/main/plugins/noesis/fmt_ant_ogr.py)  | noesis | Просмотр изображений объектов |
| 6 | .ugr | [fmt_ant_ugr.py](https://github.com/AlexKimov/lesta-file-formats/tree/main/plugins/noesis/fmt_ant_ugr.py)  | noesis | Просмотр изображений юнитов |

    Как использовать quickbms скрипты
    1. Нужен quickbms https://aluigi.altervista.org/quickbms.htm
    2. Для запуска в репозитории лежит bat файл с настройками, нужно открыть его и задать свои пути: до места, где находится quickbms, папки с игрой и места куда нужно сохранить результат.
    3. Запустить процесс через bat файл или вручную (задав свои параметры для запуска quickbms, документация на английском есть здесь https://aluigi.altervista.org/papers/quickbms.txt ). 
