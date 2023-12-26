import re

def barcode_validator(barcode):
    """Returns if a barcode is valid or not."""
    pattern = r"@[#]+[A-Z][A-Za-z0-9]{4,}[A-Z]@[#]+"
    match = re.match(pattern, barcode)
    if match:
        return True
    return "Invalid barcode"

def groups_in_barcode(valid_barcode):
    """Returns the how many digits are in the barcode i.e. groups"""
    number = ""
    for symbol in valid_barcode:
        if symbol.isdigit():
            number += symbol
    if len(number) > 0:
        return f"Product group: {int(number)}"
    return "Product group: 00"


number_of_barcodes = int(input())

for _ in range(number_of_barcodes):
    string = input()
    checked_barcode = barcode_validator(string)
    if checked_barcode == True:
        group_number = groups_in_barcode(string)
        print(group_number)
    else:
        print(checked_barcode)


