# Connection parameters, yours will be different
import psycopg2

param_dic = {
    "host"      : "localhost",
    "database"  : "Violencia intrafamiliar",
    "user"      : "postgres",
    "password"  : "1002034780"
}
def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn

print(connect(param_dic))