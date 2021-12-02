from tkinter import StringVar
from Tkinter_MiniWorkEnvironment.src.GUI import GUI
from bs4 import BeautifulSoup
import requests


class WebScraper:

    def __init__(self):
        gui = GUI.get_gui()
        self.gold_price_gram = StringVar()
        self.silver_price_gram = StringVar()
        self.rounded_result = StringVar()
        self.search_button = GUI.add_button(gui, "Search for metal prices at bullionbypost.eu!",
                                            self.search_for_gold_price, "orange", "blue", 9, 1, 2, 5)
        self.check_box = GUI.add_checkbox(gui, "rounded", self.rounded_result, "#3c0f6b", 9, 2)
        self.gold_price_label_gram = GUI.add_label(gui, "", self.gold_price_gram, 2, 10, 1, 5, 5)
        self.silver_price_label_gram = GUI.add_label(gui, "", self.silver_price_gram, 2, 11, 1, 5, 5)

    # get HTML text, use parser lxml on url, search for the first class which contains the metal_prices
    # in the metal_prices search for the gold_price and get the value, same for silver
    def search_for_gold_price(self):
        html_text = requests.get("https://www.bullionbypost.eu/gold-price/current-gold-price/").text
        soup = BeautifulSoup(html_text, "lxml")
        metal_prices = soup.find("div", class_="small-box grey-background metal-prices-box")
        gold_price = metal_prices.find("td", class_="gold-price-per-gram").get_text()
        silver_price = metal_prices.find("td", class_="silver-price-per-gram").get_text()
        if self.rounded_result.get() == "YES":
            gold_price = self.rounding_result(gold_price)
            silver_price = self.rounding_result(silver_price)
        self.gold_price_gram.set("current gold price per gram : " + gold_price)
        self.silver_price_gram.set("current silver price per gram : " + silver_price)

    # round the price and make it look nice
    def rounding_result(self, price):
        old_price = price.split()[0]
        print(old_price.strip().replace(",", "."))
        old_price = float(old_price.strip().replace(",", "."))
        new_price = "%.2f" % old_price
        new_price = new_price + "€"
        return new_price.replace(".", ",")
