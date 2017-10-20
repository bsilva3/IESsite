#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bruno Silva, Fabio Santos, Marco Ventura, Rui Jesus, Gon\xe7alo Almeida'
SITENAME = u'Diabetes: control and management'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'EG'

#theme of the site
THEME = 'attila-02dcad911ba1eb2d797a79ec008a810d89a2fde1'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS_WIDGET_NAME = 'Semanas'

SOCIAL_WIDGET_NAME = 'Projeto'

# Semanas
LINKS = (('Semana 1', '#'),
         ('Semana 2', '#'),
         ('Semana 3', '#'),
         ('Semana 4', '#'),
	 ('Semana 5', '#'),
	 ('Semana 6', '#'),)

# Social widget
SOCIAL = (('Contactos/membros', '/pages/equipa-e-contactos.html'),
          ('Repositório code.ua', 'http://code.ua.pt/projects/ies2017-2018_g102/wiki'))

DEFAULT_PAGINATION = False

# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU = False

# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (
    	('Home', '../index.html'),
    	('Cliente', '/pages/cliente.html'),
    	('Utilizador', '/pages/utilizador.html'),
    	('Especificações', '#'),
    	('Semana 1', '#'),
    	('Semana 2', '#'),
    	('Semana 3', '#'),
        ('Semana 4', '#'),
	('Semana 5', '#'),
	('Semana 6', '#'),
    	)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True



HEADER_COVER = 'https://i.imgur.com/BSoXXC7.jpg'

