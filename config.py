import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="project3kienntdbsever.postgres.database.azure.com"  #TODO: Update value #DONE
    POSTGRES_USER="project3kiennt" #TODO: Update value #DONE
    POSTGRES_PW="Kazoku1:d"   #TODO: Update value #DONE
    POSTGRES_DB="techconfdb"   #TODO: Update value #DONE
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://project3-kiennt-service-bus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=erdTibGEsMGyLYhmZQX20DvFlsqXs1arf+ASbGQhshw=' #TODO: Update value #DONE
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    SENDGRID_API_KEY = '' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False