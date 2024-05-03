from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)


def home(request):

    html = """
        <h1>Добро пожаловать на мой первый Django-сайт!</h1>
        <p>Привет, я Кирилл.</p>
        <a href="/about/">Обо мне</a>
        <a href="/lesson2/">Д/з 2 - 6</a>
        """
    logger.info("Пользователь посетил страницу 'главная'")

    return HttpResponse(html)

def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Меня зовут Кирилл, начинающий Python-разработчик, изучаю с нуля Django, пытаюсь его освоить.</p>
    <a href="/">На главную</a>
    """

    logger.info("Пользователь посетил страницу 'о себе'")
    
    return HttpResponse(html)
