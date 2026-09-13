from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 18 Pro", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 14 Pro", "+79345678901"))
catalog.append(Smartphone("Google", "Pixel 8", "+79456789012"))
catalog.append(Smartphone("Asus", "Zenfone 10", "+79567890123"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
