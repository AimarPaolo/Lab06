from database.DB_connect import DBConnect
from model.vendita import Vendita

def get_date_dao(date):
    """funzione che legge tutto il database e prende le date distinte presenti"""
    cnx = DBConnect.get_connection()
    if cnx is not None:
        cursor = cnx.cursor()
        cursor.execute("""select distinct(year(date))
                        from go_daily_sales""")
        for row in cursor:
            date.add(row)
        cursor.close()
        cnx.close()
        return date
    else:
        print("Could not connect")


def get_all_vendite():
    """funzione che legge tutto il database e prende le vendite distinte presenti"""
    cnx = DBConnect.get_connection()
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("""select *
                           from go_daily_sales""")
        result = []
        for row in cursor:
            result.append(Vendita(row["Retailer_code"], row["Product_number"], row["Order_method_code"], row["Date"],
                              row["Quantity"], row["Unit_price"], row["Unit_sale_price"]))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
