import re

def is_valid_barcode(barcode):
    """Returns True if a barcode is valid, otherwise False."""
    pattern = r"@[#]+[A-Z][A-Za-z0-9]{4,}[A-Z]@[#]+"
    return bool(re.match(pattern, barcode))

DEFAULT_PRODUCT_GROUP = "00"

def extract_product_group(valid_barcode):
    """Extracts the product group from a valid barcode."""
    number = "".join(filter(str.isdigit, valid_barcode))
    return f"Product group: {int(number)}" if number else f"Product group: {DEFAULT_PRODUCT_GROUP}"

number_of_barcodes = int(input())

for _ in range(number_of_barcodes):
    string = input().strip()
    if is_valid_barcode(string):
        group_number = extract_product_group(string)
        print(group_number)
    else:
        print("Invalid barcode")

