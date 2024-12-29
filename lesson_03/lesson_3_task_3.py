from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "10", "15")
from_address = Address("654321", "Санкт-Петербург", "Невский", "20", "30")

mailing = Mailing(to_address, from_address, 5000, "Путь №8954649")

print(mailing)
