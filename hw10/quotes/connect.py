from mongoengine import connect
from hw10.settings import config


mongo_user = config.MONGO_USER
mongodb_pass = config.MONGO_PASS
db_name = config.MONGO_DB_NAME
domain = config.MONGO_DOMAIN

# connect to cluster on AtlasDB with connection string

connect(
    host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""",
    ssl=True,
)
