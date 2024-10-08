import pyodbc

class DBUtil:
    @staticmethod
    def getDBConn():
        """
        Establish a connection to the SQL Server database and return the connection object.
        """
        try:
            conn = pyodbc.connect(
                r'Driver={SQL Server};'
                r'Server=LAPTOP-R0NMQQC9\SQLEXPRESS;'
                r'Database=OMS;'
                r'Trusted_Connection=yes;'
            )
            print('Connection done')  # Print after successful connection
            return conn  # Return the connection object
        except pyodbc.Error as e:
            print("Connection failed:", e)
            return None  # Return None on failure

if __name__ == "__main__":
    # Test the DBUtil class
    connection = DBUtil.getDBConn()
    if connection:
        connection.close()  # Close the connection if it was successful
