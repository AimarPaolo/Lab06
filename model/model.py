from database import vendita_DAO
from database import retailer_DAO
from database import prodotto_DAO
class Model:
    def __init__(self):
        self.date_vendite = set()
        self.prodotti = {}
        self.vendite = []
        self.results = []

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

    def get_vendita(self, anno, retailer, brand):
        self.vendite = vendita_DAO.get_all_vendite()
        result = []
        sorted_list = sorted(self.vendite, key=lambda x: x.ricavo(), reverse=True)
        for v in sorted_list:
            brand_prodotto = self.prodotti[v.product_number].product_brand
            if (anno is None or int(anno) == v.date.year) and (brand is None or brand == brand_prodotto) and (retailer is None or int(retailer) == v.retailer_code):
                result.append(v)
                if len(result) == 5:
                    break

        return result

    def get_vendite_for_analisi(self, anno, retailer, brand):
            self.vendite = vendita_DAO.get_all_vendite()
            self.results = []
            for v in self.vendite:
                brand_prodotto = self.prodotti[v.product_number].product_brand
                if (anno is None or int(anno) == v.date.year) and (brand is None or brand == brand_prodotto) and (
                        retailer is None or int(retailer) == v.retailer_code):
                    self.results.append(v)
            return self.results


    def get_numero_prodotti(self):
        vendita = self.results
        prod = set()
        for item in vendita:
            prod.add(item.product_number)
        return len(prod)

    def get_numero_retailer(self):
        retailer = self.results
        ret = set()
        for item in retailer:
            ret.add(item.retailer_code)
        return len(ret)

    def get_numero_vendite(self):
        return len(self.results)

    def giro_affari(self):
        vendita = self.results
        somma = 0
        for item in vendita:
            somma += item.ricavo()
        return somma
