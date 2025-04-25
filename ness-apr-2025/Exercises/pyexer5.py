def format_phone_number(number_str):
    if len(number_str) == 10 and number_str.isdigit():
        return f"{number_str[:3]}-{number_str[3:6]}-{number_str[6:]}"
    else:
        return "Invalid input"

format = format_phone_number("6304247374")
print(format)