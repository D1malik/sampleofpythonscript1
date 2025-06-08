import requests
import tkinter as tk
from tkinter import ttk, messagebox

class CurrencyConverter:
    def __init__(self):
        self.rates = self.get_rates()

    def get_rates(self):
        codes = ['USD', 'EUR', 'SEK']
        rates = {'UAH': 1.0}
        for code in codes:
            url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={code}&json"
            response = requests.get(url)
            data = response.json()
            rates[code] = data[0]['rate']
        return rates

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            raise ValueError("Валюты не должны совпадать.")
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Неподдерживаемая валюта.")
        amount_in_uah = amount * self.rates[from_currency]
        return round(amount_in_uah / self.rates[to_currency], 2)

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()

        # Защита от одинаковых валют
        if from_curr == to_curr:
            if from_curr == "USD":
                to_curr = "UAH"
                to_currency.set("UAH")
            else:
                to_curr = "USD"
                to_currency.set("USD")

        result = converter.convert(amount, from_curr, to_curr)
        result_label.config(text=f"{amount} {from_curr} = {result} {to_curr}")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

converter = CurrencyConverter()

root = tk.Tk()
root.title("Конвертер Валют")

# Сумма
tk.Label(root, text="Сумма:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

# Из валюты
tk.Label(root, text="Из валюты:").pack()
from_currency = ttk.Combobox(root, values=list(converter.rates.keys()))
from_currency.set("UAH")
from_currency.pack()

# В валюту
tk.Label(root, text="В валюту:").pack()
to_currency = ttk.Combobox(root, values=list(converter.rates.keys()))
to_currency.set("USD")
to_currency.pack()

# Кнопка
tk.Button(root, text="Конвертировать", command=convert_currency).pack(pady=5)

# Результат
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
