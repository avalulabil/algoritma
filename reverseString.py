def reverse_string_with_number(input_string):
    # Pisahkan huruf dan angka
    letters = input_string[:-1]
    number = input_string[-1]

    # Balikkan urutan huruf
    reversed_letters = letters[::-1]

    # Gabungkan hasilnya dengan angka di akhir
    return reversed_letters + number

input_string = "NEGIE1"
result = reverse_string_with_number(input_string)
print(result)
