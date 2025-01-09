import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True # En despliegue esto pasa a FALSE
#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
#SQLALCHEMY_TRACK_MODIFICATIONS = False

# Ejemplo basico de postgresql
# Comparalo con ejemplo de Mysql
SQLALCHEMY_DATABASE_URI= 'postgresql://postgredb_zcdm_user:yoeHdYiGVfOznyYEBcmUYY6pQXlAvj5q@dpg-ctvp12qj1k6c73dpmkjg-a.frankfurt-postgres.render.com/postgredb_zcdm'
SQLALCHEMY_TRACK_MODIFICATIONS=False

