# загрузка образа python
FROM python:3.9


# установка рабочей директории
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

# создание пользователя
RUN addgroup app && useradd -g app app

# установка переменных окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# установка пакетов python
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY run.sh .

# копирование проекта в рабочую директорию
COPY . .

EXPOSE 8080
# права на запуск файла
RUN chmod a+x run.sh
# изменение пользователя
USER app

# запуск приложения
CMD ["./run.sh"]

