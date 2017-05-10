import psycopg2

class dbconnection:
    def __init__(self):
        self.name = 'postgres'

    def startconn():
        try:
            conn = psycopg2.connect(
                host=localhost,
                port="5432",
                database="bigtooth",
                user=bigtooth,
                password=bigtooth)
            return(conn)
        except:
            print ("\n_________CONNECTION FAILURE_________\n")
