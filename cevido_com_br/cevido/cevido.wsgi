import os, sys
sys.path.append('/home/cevido/apps_wsgi')
sys.path.append('/home/cevido/www/site-cevido/cevido_com_br/')
sys.path.insert(0,'/home/cevido/apps_wsgi/.site-packages/')

os.environ['PYTHON_EGG_CACHE'] = '/home/cevido/apps_wsgi/.python-eggs'
os.environ['DJANGO_SETTINGS_MODULE'] = 'cevido.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

