from Code.domain.class_db_connector import DBConnector
from Code.network.class_server import Server


if __name__ == '__main__':
    conn = DBConnector()
    conn.create_tables()
    server = Server(conn)
    server.start()
