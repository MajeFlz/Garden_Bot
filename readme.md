# NFTree

![logo](https://cdn.discordapp.com/attachments/1023980844731342908/1245788996244869200/NFTree_github.png?ex=665a06ea&is=6658b56a&hm=5f964d06f219a30a7ff305f406364b34e18424b9d8a92df2326b4bc727b20875&)

![Static Badge](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Static Badge](https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Static Badge](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Static Badge](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Static Badge](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Static Badge](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)
![Static Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Static Badge](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)


# | Оглавление:

- [Общая информация](#общая-информация)
- [Организация разработки](#организация-разработки)
- [Текущие задачи](#текущие-задачи)
- [Работа с ботом](#работа-с-ботом)

## Общая информация

### NFTree - объединение людей, которых связывают новые технологии и забота о природе.

Данный проект призван вызвать интерес к волонтерству и заботе о природе посредством необычной системы геймефикации с наградами в эко-системе парка.

## Текущие задачи
  - [x] Разработать прототип бота
    - [x] Создать прототип базы данных для пользователей
  - [x] Разработать дизайн NFTree коллекции
  - [x] Разработать бренд-бук для веб-приложения
    - [x] Создать пробную версию интерфейса приложения
    - [ ] Подготовить страницы сайта
    - [ ] Хостинг готового веб приложения
  - [x] Разработать алгоритм системы геймификации

## Организация разработки

> [!NOTE]
> Раздел находится в разработке и может содержать неточности

- Ветка release - текущая полность рабочая версия готового продукта.
- Ветка master - пред-релизная версия бота с новыми функциями, которую нужно будет протестировать, перед добавлением в ветку release.
- Ветка [tg_bot](https://github.com/MajeFlz/Garden_Bot/tree/tg_bot) - ветка предназначенная полностью для разработки и тестирования функционала бота.
- Ветка [web_app](https://github.com/MajeFlz/Garden_Bot/tree/web_app) - ветка предназначенная полность  для разработки веб интерфейса приложения.
- Ветка [web_app_test](https://github.com/MajeFlz/Garden_Bot/tree/web_app_test) - ветка предназначенная для новых экспериментальных лендингов и страниц.



## Работа с ботом

Создать файл config с токеном бота

1) Настроить venv окружение // легче просто открыть его в IDE в terminal
Создать окружение
python -m venv venv
Включить окружение
linux: source venv/bin/activate
win: venv\Scripts\activate.bat

2) Загрузить необходимые зависимости библиотек
pip install -r requirements.txt

3) Запустить бота
python main.py
