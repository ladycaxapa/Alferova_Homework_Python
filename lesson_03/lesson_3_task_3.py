from address import Address
from mailing import Mailing


to_addr = Address("627350", "Аромашево", "Ленина", "166", "2")


from_addr = Address("630000", "Новосибирск", "Ленина", "5", "12")


mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=550,
    track="RA123456789RU"
    )


print(
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
