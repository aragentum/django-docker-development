import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_FILE = os.path.join(BASE_DIR, 'settings', 'secret_key.txt')

try:
    SECRET_KEY = open(SECRET_FILE).read().strip()
except IOError:
    SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
    if not SECRET_KEY:
        try:
            import random
            SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz'
                                                               '0123456789!@#$%^&*(-_=+)') for i in range(50)])
            with open(SECRET_FILE, 'w') as file:
                file.write(SECRET_KEY)
        except IOError:
            Exception('Please create a %s file or set the environment variable `DJANGO_SECRET_KEY` with '
                      'random characters to generate your secret key!' % SECRET_FILE)
