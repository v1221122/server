#!/usr/bin/python3
# -*- coding: utf-8 -*- импортируем 
# модуля языка, которые 
# используются в этом 
# скрипте
import os, sys, site
# подключаем наш проект в 
# путь python, если django.wsgi 
# находится не в корне 
# проекта, то надо 
# указывать полный путь 
# до каталога проекта
sys.path.insert(0, os.path.dirname(__file__))
# подключаем виртуальное 
# окружение проекта
site.addsitedir('/home/httpd/env/djbookru/lib/python2.6/sitepackages')
# указываем через 
# переменную окружения 
# название модуля с 
# конфигурацией проекта
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
# передаём управление 
# нашему проекту
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
