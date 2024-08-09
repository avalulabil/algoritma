def longest_word(sentence):
    # Pisahkan kalimat menjadi daftar kata
    words = sentence.split()

    # Temukan kata terpanjang
    longest_word = max(words, key=len)
    
    # Output kata terpanjang dan jumlah karakternya
    return f"{longest_word}: {len(longest_word)} character{'s' if len(longest_word) > 1 else ''}"

# Meminta input dari pengguna
sentence = input("Masukkan sebuah kalimat: ")
result = longest_word(sentence)
print(result)
