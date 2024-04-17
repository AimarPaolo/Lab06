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

    def get_vendita(self, anno, retailer, brand):
        print(retailer)
        print(type(retailer))
        self.vendite = vendita_DAO.get_all_vendite()
        result = []
        count = 0
        sorted_list = sorted(self.vendite, key=lambda x: x.ricavo(), reverse=True)
        for v in sorted_list:
            brand_prodotto = self.prodotti[v.product_number].product_brand
            if (anno is None or int(anno) == v.date.year) and (brand is None or brand == brand_prodotto) and (retailer is None or int(retailer) == v.retailer_code):
                count += 1
                result.append(v)
                if count == 5:
                    break
        print(result)

        return result
