
class ClienteRepository:
    def __init__(self, connection):
        self.connection = connection

    def save_client(self, cliente):
        client_cursor = self.connection.cursor()
        client_cursor.execute(
            "INSERT INTO cliente (nome, email, placa_carro) VALUES (?, ?, ?)",
            (cliente["nome"], cliente["email"], cliente["placa_carro"])
        )
        self.connection.commit()

    def get_all_clients(self):
        client_cursor = self.connection.cursor()
        client_cursor.execute("SELECT * FROM cliente")
        return client_cursor.fetchall()

    def get_client_by_id(self, client_id):
        client_cursor = self.connection.cursor()
        client_cursor.execute("SELECT * FROM cliente WHERE id = ?", (client_id,))
        row = client_cursor.fetchone() 
        return {"id": row[0], "nome": row[1], "email": row[2], "placa_carro": row[3]} if row else None
    
    def update_client(self, client_id, cliente):
        client_cursor = self.connection.cursor()
        client_cursor.execute(
            "UPDATE cliente SET nome = ?, email = ?, placa_carro = ? WHERE id = ?",
            (cliente["nome"], cliente["email"], cliente["placa_carro"], client_id)
        )
        self.connection.commit()

    def delete_client(self, client_id):
        client_cursor = self.connection.cursor()
        client_cursor.execute("DELETE FROM cliente WHERE id = ?", (client_id,))
        self.connection.commit()
