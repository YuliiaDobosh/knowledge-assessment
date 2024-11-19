#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Запуск адміністративних задач Django."""
    # Встановлюємо налаштування за замовчуванням для Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assessment.settings')

    try:
        # Імпортуємо функцію для виконання команд
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не вдалося імпортувати Django. Ви впевнені, що він встановлений та "
            "доступний у вашій змінній середовища PYTHONPATH? Можливо, ви забули "
            "активувати віртуальне середовище?"
        ) from exc

    # Виконуємо команду з командного рядка
    execute_from_command_line(sys.argv)

# Перевіряємо, чи цей файл виконується як основний, і запускаємо main()
if __name__ == '__main__':
    main()
