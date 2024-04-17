from database import vendita_DAO
from database import retailer_DAO
from database import prodotto_DAO
class Model:
    def __init__(self):
        self.date_vendite = set()
        self.prodotti = {}
        self.vendite = []

    def get_prodotto(self):
        self.prodotti = prodotto_DAO.get_all_products()
        prodotto = set()
        for item in self.prodotti.values():
            prodotto.add(item.product_brand)
        return prodotto

    def get_retailers(self):
        return retailer_DAO.RetailerDAO.get_all_retailers()

    def get_year(self):
        vendita_DAO.get_date_dao(self.date_vendite)
        return self.date_vendite

    def get_vendita(self):
        self.vendite = vendita_DAO.get_all_vendite()
        return self.vendite