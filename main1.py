from dry_cleaning import DryCleaning
from service_type import ServiceType

dry_cleaning = DryCleaning()
dry_cleaning.add_service_type(
    ServiceType(
        code=dry_cleaning.service_types.get_next_code(),
        name="Blanket Cleaning",
        type="Textile Cleaning",
        price=25,
    )
)
dry_cleaning.add_service_type(
    ServiceType(
        code=dry_cleaning.service_types.get_next_code(),
        name="Tuxedo Cleaning",
        type="Clothes Cleaning",
        price=25,
    )
)

for code, service_type in dry_cleaning.service_types.item_dict.items():
    print(f"{code}: {service_type}")

dry_cleaning.service_types.remove_item_by_code(0)

if not dry_cleaning.service_types.item_dict:
    print("No items")
else:
    for code, service_type in dry_cleaning.service_types.item_dict.items():
        print(f"{code}: {service_type}")

print(f"Next code: {dry_cleaning.service_types.get_next_code()}")
