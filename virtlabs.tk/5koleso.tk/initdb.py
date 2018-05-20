import json
from pony.orm import Database, PrimaryKey, Required, Optional

# Reading config file.  
with open('/srv/http/virtlabs.tk/5koleso.tk/db_config/config.json') as config_file:
    _config = json.loads(config_file.read())
    

_PostgresDb = Database()
class Worker(_PostgresDb.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    car = Required(str)
    color = Required(str)
    number = Required(int)
    
class Auth(_PostgresDb.Entity):
    id = PrimaryKey(int, auto=True)
    login = Required(str)
    password = Required(str)
    worker_id = Required(int)
    
class Online(_PostgresDb.Entity):
    id = PrimaryKey(int, auto=True)
    worker_id = Required(int)
    queue_number = Required(int)
   
class Taxi_order(_PostgresDb.Entity):
    id = PrimaryKey(int, auto=True)
    phone = Required(str)
    address_from = Required(str)
    address_to = Optional(str)
    comment = Optional(str)
    worker_id = Optional(int)
    time = Optional(int)
    w_confirm = Optional(bool)
    p_confirm = Optional(bool)
    
_PostgresDb.bind(**_config)
_PostgresDb.generate_mapping(check_tables = True, create_tables = False)