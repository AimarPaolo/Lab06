import _mysql_connector
from model.retailer import Retailer
from database.DB_connect import DBConnect


class RetailerDAO:
    @staticmethod
    def get_all_retailers():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT r.*
                            FROM go_retailers r"""
            cursor.execute(query)
            for row in cursor:
                result.append(Retailer(row["Retailer_code"],
                                       row["Retailer_name"],
                                       row["Type"],
                                       row["Country"]))
            cursor.close()
            cnx.close()
            return result