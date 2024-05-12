# NFDoc


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

## Организация разработки

> [!NOTE]
> Раздел находится в разработке и может содержать неточности

- Ветка release - текущая полность рабочая версия готового продукта.
- Ветка master - пред-релизная версия бота с новыми функциями, которую нужно будет протестировать, перед добавлением в ветку release.
- Ветка [tg_bot](https://github.com/MajeFlz/Garden_Bot/tree/tg_bot) - ветка предназначенная полностью для разработки и тестирования функционала бота.
- Ветка [web_app](https://github.com/MajeFlz/Garden_Bot/tree/web_app) - ветка предназначенная полность  для разработки веб интерфейса приложения.
- Ветка [web_app_test](https://github.com/MajeFlz/Garden_Bot/tree/web_app_test) - ветка предназначенная для новых экспериментальных лендингов и страниц.

## Документация

Модуль содержит функции для запуска бота и установки соединения с базой данных.

**Автор:** NFTree
---
# main.py

## Функции

### `async def start_bot(bot: Bot) -> None`

Устанавливает команды бота.

- **Параметры:**
  - `bot`: Экземпляр `aiogram.Bot` для установки команд.

### `async def db_create_pool() -> aiomysql.pool.Pool`

Создает пул соединений с базой данных MySQL.

- **Возвращает:** Пул соединений с базой данных.

### `async def start() -> None`

Запускает бота Telegram и подключается к базе данных.

- **Параметры:** Нет.
- **Возвращает:** Ничего.

## Импорты

```python
import asyncio
import logging
import aiomysql
from aiogram import Bot, Dispatcher
```
---
# index.html

Сайт-Кликер

## Описание
Документация представляет собой описание HTML-страницы для сайта-кликера.

## Структура HTML-файла
HTML-файл содержит следующие основные блоки:
- Заголовок (`<head>`): содержит метаинформацию о документе и ссылки на внешние ресурсы.
- Основное содержимое (`<body>`): содержит основные элементы страницы, такие как шапка, основное содержимое, навигационное меню и т.д.

## Блоки страницы

### Шапка (`<header>`)
- **notification-bell**: Иконка уведомлений.
- **balance**: Отображение баланса.

### Основное содержимое (`<main>`)
- **tree**: Область отображения дерева.
- **counter**: Отображение счетчика.
- **progressbar**: Прогресс-бар.

### Навигационное меню (`<nav>`)
- **aboutGardenBtn**: Кнопка "О саде".
- **tasksBtn**: Кнопка "Задания".
- **payBtn**: Кнопка "Кошелек".
- **aboutUsBtn**: Кнопка "О нас".

## Ресурсы
- **JavaScript**: 
    - `telegram-web-app.js`: Скрипт для работы с Telegram Web.
    - `web_app.js`: Пользовательский JavaScript файл.
- **CSS**:
    - `style.css`: Файл стилей.

## Комментарии
- Падающие листья (в блоке `main`) закомментированы, возможно из-за проблем с отображением в CSS.


# web_app.js

## Обработчики событий

```javascript
// Обработчик события DOMContentLoaded для выполнения кода после загрузки контента
document.addEventListener("DOMContentLoaded", function() {
    // Код обработчика события
});
```

## Функции для отображения контента

### `showAboutGarden()`

Функция для отображения информации о саде. Очищает основной контент и добавляет информацию о саде.

### `showTasks()`

Функция для отображения заданий. Очищает основной контент и подготавливает контейнер для заданий.

### `showPay()`

Функция для отображения информации о платежах. Очищает основной контент и подготавливает контейнер для информации о платежах.

### `showAboutUs()`

Функция для отображения информации о компании. Очищает основной контент и добавляет информацию о компании NFTree.

## Функции для обновления счетчика и прогресса

### `updateCounter()`

Функция для обновления счетчика и прогресса. Увеличивает счетчик на 1, обновляет значение счетчика и прогресс-бар.

### `resetCounter()`

Функция для сброса счетчика и прогресса. Сбрасывает счетчик на 0, обновляет значение счетчика и прогресс-бар.

### `updateProgressBar()`

Функция для обновления прогресса. Вычисляет и обновляет значение прогресса и его отображение.

## Обработчики событий

```javascript
// Обработчики событий для кнопок навигации

aboutGardenBtn.addEventListener('click', showAboutGarden);
tasksBtn.addEventListener('click', showTasks);
payBtn.addEventListener('click', showPay);
aboutUsBtn.addEventListener('click', showAboutUs);

// Добавляем обработчики событий для изображения дерева и счетчика

document.getElementById('tree-image').addEventListener('click', function() {
    updateCounter();
});

document.getElementById('progress').addEventListener('click', resetCounter);
```

```javascript
// Переменная счетчика
var counter = 0;
```

```javascript
// Функции для обновления счетчика и прогресса
```
---
# style.css

## Общие стили

```css
/* Общие стили для всего документа */
body {
    margin: 0; /* Убираем отступы */
    padding: 0; /* Убираем внутренние отступы */
    overflow: hidden; /* Запрещаем прокрутку содержимого */
    font-family: 'Comic Sans MS', cursive, sans-serif; /* Устанавливаем шрифт */
    background: linear-gradient(135deg, #65a65e, #8bc34a); /* Задаем фон с градиентом */
    animation: animateBackground 30s linear infinite; /* Анимация фона */
}

/* Анимация фона */
@keyframes animateBackground {
    0% {
        background-position: 0% 0%;
    }
    100% {
        background-position: 100% 100%;
    }
}
```

## Стили для изображения дерева

```css
/* Стили для изображения дерева */
#tree {
    /* Стили */
}
```

## Стили для счетчика

```css
/* Стили для счетчика */
#counter {
    /* Стили */
}
```

## Стили для прогресс-бара

```css
/* Стили для прогресс-бара */
#progressbar {
    /* Стили */
}

/* Стили для заполнения прогресс-бара */
#progress {
    /* Стили */
}
```

## Стили для листьев

```css
/* Стили для листьев */
.leaf {
    /* Стили */
}

/* Анимация падающих листьев */
@keyframes fallingLeaves {
    /* Анимация */
}

/* Стили для каждого отдельного листа */
.leaf:nth-child(1) {
    /* Стили */
}
```
---
# settings.py

Документация для конфигурационного скрипта

Этот скрипт использует библиотеку Environs для загрузки настроек из файла .env и их представления в виде объектов классов.

## Классы настроек

### `Bots`

Класс для представления настроек ботов.

#### Атрибуты:

- `bot_token` (str): Токен бота.

### `Database`

Класс для представления настроек базы данных.

#### Атрибуты:

- `host` (str): Адрес хоста базы данных.
- `port` (int): Порт базы данных.
- `user` (str): Имя пользователя базы данных.
- `password` (str): Пароль пользователя базы данных.
- `db` (str): Название базы данных.

### `Settings`

Класс для представления всех настроек.

#### Атрибуты:

- `bots` (Bots): Настройки ботов.
- `database` (Database): Настройки базы данных.

## Функции

### `get_settings(path: str)`

Функция для получения настроек из файла .env.

#### Аргументы:

- `path` (str): Путь к файлу .env.

#### Возвращаемое значение:

`Settings`: Объект класса Settings с загруженными настройками.

## Пример использования

```python
# Загрузка настроек из файла .env и сохранение их в переменной settings
settings = get_settings('config')
```
---
# dbconnect.py

Документация для класса Request

Этот класс представляет собой запрос к базе данных для добавления данных о пользователе.

## Атрибуты

- `connector` (`aiomysql.Connection`): Объект подключения к базе данных `aiomysql.Connection`.

## Методы

### `__init__(connector: aiomysql.Connection)`

Инициализация объекта `Request`.

#### Аргументы

- `connector` (`aiomysql.Connection`): Объект подключения к базе данных `aiomysql.Connection`.

### `add_user_data(user_id, user_name)`

Асинхронный метод для добавления данных о пользователе в базу данных.

#### Аргументы

- `user_id`: Идентификатор пользователя.
- `user_name`: Имя пользователя.
---
# commands.py

Документация для функции set_commands

Эта функция устанавливает команды для бота.

## Аргументы

- `bot` (`aiogram.Bot`): Объект бота `aiogram.Bot`.

## Методы

### `set_commands(bot: Bot)`

Устанавливает команды для бота.

#### Аргументы

- `bot` (`aiogram.Bot`): Объект бота `aiogram.Bot`.

---
# dbmiddleware.py

Документация для класса DbSession

Этот класс представляет собой middleware для управления подключением к базе данных в ходе выполнения запросов бота.

## Атрибуты

- `pool` (`aiomysql.pool.Pool`): Пул подключений к базе данных `aiomysql.pool.Pool`.

## Методы

### `__init__(pool: aiomysql.pool.Pool)`

Инициализация объекта `DbSession`.

#### Аргументы

- `pool` (`aiomysql.pool.Pool`): Пул подключений к базе данных `aiomysql.pool.Pool`.

### `__call__(handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], event: TelegramObject, data: Dict[str, Any]) -> Any`

Обработчик вызова, выполняющийся при каждом запросе.

#### Аргументы

- `handler` (`Callable`): Обработчик запроса.
- `event` (`TelegramObject`): Объект события.
- `data` (`Dict[str, Any]`): Данные запроса.

#### Возвращаемое значение

`Any`: Результат выполнения обработчика.

---
# inline_user.py

Документация для функций `inline_user_menu` и `connect_wallet`, которые создают встроенные клавиатуры для меню пользователя и подключения кошелька:


## Документация для функции inline_user_menu

Эта функция создает встроенную клавиатуру для меню пользователя.

## Возвращаемое значение

`InlineKeyboardMarkup`: Встроенная клавиатура с пунктами меню.

## Пример использования

```python
menu_markup = await inline_user_menu()
```
---
# inline_admin.py

Вот документация для объектов `admin_menu` и `web_ui`, которые представляют собой встроенные клавиатуры для меню администратора и интерфейса веб-приложения:

```markdown
# Документация для объекта admin_menu

Этот объект представляет собой встроенную клавиатуру для меню администратора.

## Атрибуты

- `admin_menu` (`InlineKeyboardMarkup`): Встроенная клавиатура для меню администратора.

## Пример использования

```python
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Начислить баллы', url="https://aiogram.readthedocs.io/_/downloads/en/latest/pdf/")],
    [InlineKeyboardButton(text='Добавить задание', url="https://aiogram.readthedocs.io/_/downloads/en/latest/pdf/")]
])
```

## Документация для объекта web_ui

Этот объект представляет собой встроенную клавиатуру для запуска веб-приложения.

## Атрибуты

- `web_ui` (`InlineKeyboardMarkup`): Встроенная клавиатура для запуска веб-приложения.

## Пример использования

```python
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

web_ui = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Запустить приложение', web_app=WebAppInfo(url = "https://127.0.0.1:3000"))]
])
```

## Документация для функции connect_wallet

Эта функция создает встроенную клавиатуру для подключения кошелька.

## Возвращаемое значение

`InlineKeyboardMarkup`: Встроенная клавиатура с кнопками для выбора кошелька.

## Пример использования

```python
wallet_markup = await connect_wallet()
```
---
# user_commands.py

Документация для функции `user_menu`:

## Документация для функции user_menu

Эта функция отвечает на команду /user_menu, отображая пользователю встроенную клавиатуру с меню.

## Аргументы

- `message` (`aiogram.types.Message`): Объект сообщения.

## Возвращаемое значение

`None`

## Пример использования

```python
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command
from app.keyboards.inline_user import inline_user_menu

async def user_menu(message: types.Message):
    text = "Меню:"
    await message.answer(text, reply_markup=await inline_user_menu())

dp = Dispatcher()
dp.register_message_handler(user_menu, Command('user_menu'))
```
# base_commands.py

Вот документация для функций `start_message`, `help_message` и `wallet_message`:


## Документация для функции start_message

Эта функция отправляет приветственное сообщение пользователю при получении команды /start и добавляет данные пользователя в базу данных.

## Аргументы

- `message` (`aiogram.types.Message`): Объект сообщения.
- `request` (`Request`): Объект для выполнения запросов к базе данных.

## Возвращаемое значение

`None`

## Пример использования

```python
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command
from app.utils.dbconnect import Request

async def start_message(message: types.Message, request: Request):
    await request.add_user_data(message.from_user.id, message.from_user.first_name)
    text = (f'Привет, {message.from_user.first_name}!\n'
            'Я бот который будет выдавать тебе награды за волонтерство в прекрасном саду\n\n'
            'Если тебе потребуется помощь, просто введи команду /help')
    await message.answer(text, reply_markup=web_ui)

dp = Dispatcher()
dp.register_message_handler(start_message, Command('start'))
```

## Документация для функции help_message

Эта функция отправляет сообщение о том, что помощь еще в разработке, при получении команды /help.

## Аргументы

- `message` (`aiogram.types.Message`): Объект сообщения.

## Возвращаемое значение

`None`

## Пример использования

```python
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command

async def help_message(message: types.Message):
    text = (f'Ещё в разработке')
    await message.answer(text)

dp = Dispatcher()
dp.register_message_handler(help_message, Command('help'))
```

## Документация для функции wallet_message

Эта функция отправляет сообщение с просьбой выбрать кошелек для подключения, при получении команды /wallet.

## Аргументы

- `message` (`aiogram.types.Message`): Объект сообщения.

## Возвращаемое значение

`None`

## Пример использования

```python
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command

async def wallet_message(message: types.Message):
    await message.answer(text='Выберите кошелек для подключения', reply_markup= await connect_wallet())

dp = Dispatcher()
dp.register_message_handler(wallet_message, Command('wallet'))
```
---
# admin_commands.py


## Документация для функции admin_menu

Эта функция отвечает на команду /admin_menu, отображая администратору встроенную клавиатуру с меню.

## Аргументы

- `message` (`aiogram.types.Message`): Объект сообщения.

## Возвращаемое значение

`None`

## Пример использования

```python
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command

async def admin_menu(message: types.Message):
    text = "Меню:"
    await message.answer(text, reply_markup=admin_menu)

dp = Dispatcher()
dp.register_message_handler(admin_menu, Command('admin_menu'))
```

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
