from database.DB_connect import DBConnect
from model.prodotto import Prodotto


def get_all_products():
    """funzione che legge tutto il database e prende i prodotti presenti"""
    dizionario = {}
    cnx = DBConnect.get_connection()
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("""select *
                        from go_products""")
        for row in cursor:
            prod = Prodotto(row["Product_number"], row["Product_line"], row["Product_type"], row["Product"],
                                                         row["Product_brand"], row["Product_color"], row["Unit_cost"], row["Unit_price"])
            dizionario[row["Product_number"]] = prod
        cursor.close()
        cnx.close()
        return dizionario
    else:
        print("Could not connect")
