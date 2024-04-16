from database.DB_connect import DBConnect


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
