import os
MYSQL_URL = f'mysql://{os.getenv("MYSQL_USER")}:{os.getenv("MYSQL_PASSWORD")}@{os.getenv("MYSQL_HOST")}:3306/{os.getenv("MYSQL_DATABASE")}'
TORTOISE_MODELS = ['models.User', 'models.Token']
TORTOISE_CONFIG = {
    'connections':{'default':MYSQL_URL},
    'apps':{
        'models':{
            'models':TORTOISE_MODELS,
            'default_connection':'default'
        }
    }
}