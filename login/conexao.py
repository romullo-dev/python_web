import mysql.connector

class conexao:
    
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "mydb"
        )

        self.cursor = self.conn.cursor()

    def execultar (self, sql, valores=None):
        self.cursor.execute(sql, valores)
        self.conn.commit()

    def buscar (self, sql, valores=None):
        self.cursor.execute(sql,valores)
        return self.cursor.fetchall()
    
    def fechar (self):
        self.cursor.close()
        self.conn.close()