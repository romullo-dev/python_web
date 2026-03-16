from conexao import conexao

class Login:
    def __init__(self):
        self.db = conexao()

    def autenticar(self, userName, password):
        sql = "SELECT * FROM user WHERE userName = %s AND password = %s"
        valores = (userName, password)

        result = self.db.buscar(sql, valores)

        if result:
            return result[0]
        return None
        
    def fechar_conexao(self):
        self.db.fechar()
