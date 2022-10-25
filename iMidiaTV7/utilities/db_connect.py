import mysql.connector
from mysql.connector import errorcode

from iMidiaTV7.utilities.driver_chrome import logging

# Obtain connection string information from the portal

config = {
    'host': '104.198.21.88',
    'user': 'phpread',
    'password': 'CztRcMCTTO',
    'database': 'imidiatv'
}
try:
    conn = mysql.connector.connect(**config)
    logging.info("Conexão estabelecida com o banco de dados")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = conn.cursor()

'''
def ConsultaBancoInsercao(self, id_midia):

  id_mid = int(id_midia)
  print("id midia:", + id_mid)
  queryzinha = ("SELECT ID_STATUS_PROCESSAMENTO FROM GM_FILA_INSERCAO_DINAMICA WHERE ID_MIDIA = " + id_midia)
  cursor.execute(queryzinha)
  rows = cursor.fetchall()
  if cursor.rowcount >= 1:
    print("Read", cursor.rowcount, "row(s) of data.")
    id_processamento = rows[1]
    id_processamento = str(id_processamento[0])
    return id_processamento, rows
  else:
    return False

'''

"""

  # Read data
  cursor.execute("SELECT * FROM inventory;")
  rows = cursor.fetchall()
  print("Read",cursor.rowcount,"row(s) of data.")

  # Print all rows
  for row in rows:
  	print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))

  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")

"""
