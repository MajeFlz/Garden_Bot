import re
import logging
# Путь к файлу html где будет список
# Список задач для сада лежит в переменной tasks
HTML_FILE_PATH = "index.html"  

def update_tasks_in_html(tasks):
    with open(HTML_FILE_PATH, "r") as html_file:
        content = html_file.read()

    # Находим содержимое переменной tasks с помощью регулярного выражения
    pattern = r"const tasks = \[[^\]]*];"
    match = re.search(pattern, content)

    if match:
        old_tasks = match.group(0)
        new_tasks = f'const tasks = [\n'
        for task in tasks:
            new_tasks += f'    "{task}",\n'
        new_tasks += f'];'

        # Заменяем содержимое переменной tasks в HTML-файле
        new_content = content.replace(old_tasks, new_tasks)

        # Записываем обновленный HTML-код обратно в файл
        with open(HTML_FILE_PATH, "w") as html_file:
            html_file.write(new_content)
    else:
        logging.error("Не удалось найти переменную tasks в файле index.html.")