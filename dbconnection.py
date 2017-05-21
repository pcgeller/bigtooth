import psycopg2

class database:
    def __init__(self):
        self.name = 'postgres'
    def startconn(self):
        try:
            self.conn = psycopg2.connect(
                host='localhost',
                port="5432",
                database="bigtooth",
                user='bigtooth',
                password='bigtooth')
            return(self.conn)
        except:
            print ("\n_________CONNECTION FAILURE_________\n")


# conn = psycopg2.connect(
#     host='localhost',
#     port="5432",
#     database="bigtooth",
#     user='bigtooth',
#     password='bigtooth')
# return(conn)
