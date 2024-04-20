import mysql.connector
import pandas as pd




db = mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="Tarefa1")

if db.is_connected():
        print("Conexão ao banco de dados MySQL estabelecida com sucesso.")

# Criar um cursor para executar consultas
cursor = db.cursor()

# Exemplo de consulta SELECT
cursor.execute("SELECT * FROM Usuario")

records = cursor.fetchall()
# Converter os resultados em um DataFrame do Pandas
df = pd.DataFrame(records, columns=[desc[0] for desc in cursor.description])

# Exibir o DataFrame
print(df)