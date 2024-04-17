import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_top_vendite(self, e):
        self._view.controls.clear()
        anno = self._view.dd_anno.value
        brand = self._view.dd_brand.value
        retailer = self._view.dd_retailer.value
        lista = self._model.get_vendita(anno, retailer, brand)
        if len(lista) == 0:
            self._view.txt_result.controls.append(ft.Text(f"La ricerca non ha riportato alcun risultato", color="red"))
            self._view.update_page()
            return
        for vendita in lista:
            self._view.txt_result.controls.append(ft.Text(f"{vendita}"))
        self._view.update_page()


    def handle_analizza_vendite(self, e):
        pass

    def populate_dd_anno(self):
        self._view.dd_anno.options.append(ft.dropdown.Option(key="None", text="Nessun Filtro"))
        for anno in self._model.get_year():
            self._view.dd_anno.options.append(ft.dropdown.Option(anno[0]))
        self._view.update_page()

    def populate_dd_prodotto(self):
        self._view.dd_brand.options.append(ft.dropdown.Option(key="None", text="Nessun Filtro"))
        for prodotto in self._model.get_prodotto():
            self._view.dd_brand.options.append(ft.dropdown.Option(prodotto))
        self._view.update_page()

    def populate_dd_retailer(self):
        self._view.dd_retailer.options.append(ft.dropdown.Option(key="None", text="Nessun Filtro"))
        retailers = self._model.get_retailers()
        for r in retailers:
            retailer = r
            self._view.dd_retailer.options.append(ft.dropdown.Option(key=retailer.retailer_code,
                                                                     text=retailer.retailer_name,
                                                                     data=retailer, on_click=self.read_retailer))
        self._view.update_page()
        self._view.update_page()

    def read_retailer(self, e):
        self._retailer = self._view.dd_retailer.value
