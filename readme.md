# NFTree

![logo](https://cdn.discordapp.com/attachments/1023980844731342908/1225743114535309312/NFTree_github.png?ex=66223d3b&is=660fc83b&hm=f18744c5a8253226c62c1063d58dc0395ddd4967b313795693c8787bc0e94902&)

![Static Badge](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Static Badge](https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Static Badge](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Static Badge](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Static Badge](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Static Badge](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)
![Static Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Static Badge](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)


# | Оглавление:

- [Общая информация](#введение)
- [Организация разработки](#организация-разработки)
- [Работа с ботом](#работа-с-ботом)

## Введение

### NFTree - объединение людей, которые связывают новые технологии и заботу о природе.

## Организация разработки

> [!NOTE]
> Раздел находится в разработке и может содержать неточности

- Ветка release (добавить ссылку) - текущая полность рабочая версия готового продукта.
- Ветка master (добавить ссылку) - пред-релизная версия бота с новыми функциями, которую нужно будет протестировать, перед добавлением в ветку release.
- Ветка add-function (добавить ссылку и переименовать в tg-bot) - ветка предназначенная полностью для разработки и тестирования функционала бота.
- Ветка add-function (добавить ссылку и переименовать в tg-bot-test) - ветка предназначена для новых экспериментальных функций и алгоритмов.
- Ветка web (добавить ссылку и переименовать в web-app) - ветка предназначенная полность  для разработки веб интерфейса приложения.
- Ветка web-test (Добавить ссылку и переименовать в web-app-test) - ветка предназначенная для новых экспериментальных лендингов и страниц.



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
