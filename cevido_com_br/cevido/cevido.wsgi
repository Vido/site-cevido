import os, sys
sys.path.append('/home/cevido/apps_wsgi')
sys.path.append('/home/cevido/www/site-cevido/cevido_com_br/')
os.environ['PYTHON_EGG_CACHE'] = '/home/cevido/apps_wsgi/.python-eggs'
os.environ['DJANGO_SETTINGS_MODULE'] = 'cevido.settings'

# Solve KingHost's problems
sys.path += [
    '/home/cevido/apps_wsgi/.site-packages/South-1.0-py2.6.egg',
#    '/home/cevido/apps_wsgi/.site-packages/django_model_utils-2.0.3-py2.6.egg'
    '/home/cevido/apps_wsgi/.site-packages/pip-1.5.6-py2.6.egg',
#    '/home/cevido/apps_wsgi/.site-packages/django_photologue-2.8.2-py2.6.egg'
#    '/home/cevido/apps_wsgi/.site-packages/django_sortedm2m-0.7.0-py2.6.egg'
    '/home/cevido/apps_wsgi/.site-packages/django_filer-0.9.7-py2.6.egg',
    '/home/cevido/apps_wsgi/.site-packages/django_polymorphic-0.5.6-py2.6.egg'
    '/home/cevido/apps_wsgi/.site-packages/django_mptt-0.6.1-py2.6.egg',
    '/home/cevido/apps_wsgi/.site-packages/easy_thumbnails-2.1-py2.6.egg',
]

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# # Useful for sys.path debugging
# with open('/home/cevido/apps_wsgi/sys_path.txt', 'w') as fp:
#     fp.write(str(sys.path))
