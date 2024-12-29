from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S24", "+7 905 734 34 55"),
    Smartphone("Google", "Pixel 8 Pro", "+7 945 768 12 40"),
    Smartphone("iPhone", "15 Pro", "+7 915 858 68 78"),
    Smartphone("Xiaomi", "14 Pro", "+7 987 768 12 56"),
    Smartphone("Huawei", "Pura 70 Ultra", "+7 998 546 45 98")
]

for phone in catalog:
    print(f"{phone.smph_brand} - {phone.smph_model}. {phone.smph_number}")
