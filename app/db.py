import oracledb

# Get connection to the Oracle server which dataset is prepared
def get_connection():
    connection = oracledb.connect(
        user="system",
        password="ozgur2311",
        dsn="localhost:1521/FREEPDB1"
    )
    return connection