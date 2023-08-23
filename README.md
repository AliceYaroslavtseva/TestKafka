## 1. [Описание](#1)
## 2. [Запуск проекта](#2)

---
## 1. Описание <a id=1></a>

Пробный запуск Apache Kafka.
Знакомство с инструментом, его настройками и разворачиванием сразу в докере.

---
## 2. Запуск проекта <a id=2></a>

### Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:AliceYaroslavtseva/test_kafka.git
```
### Cоздать и активировать виртуальное окружение:
```
python -m venv venv # Для Windows
python3 -m venv venv # Для Linux и macOS
```
```
source venv/Scripts/activate # Для Windows
source venv/bin/activate # Для Linux и macOS
```
### Установить зависимости из файла requirements.txt:
```
python.exe -m pip install --upgrade pip # Для Windows
python3 -m pip install --upgrade pip # Для Linux и macOS
```
```
pip install -r requirements.txt
```
### Запустить сборку контейнеров:
```
docker-compose up -d
```
### Запустить поочерёдно:
```
python pusher.py # Для Windows
python consumer.py
python3 pusher.py # Для Linux и macOS
python3 consumer.py
```
### Адрес интерфейса:
```
http://localhost:8080/
```
### Добвить брокера в хосты:
```
sudo su
nano /etc/hosts
127.0.0.1 kafka
```
