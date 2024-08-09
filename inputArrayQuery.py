def count_occurrences(input_array, query_array):
    result = []
    
    for query in query_array:
        # Hitung jumlah kemunculan query dalam input_array
        count = input_array.count(query)
        result.append(count)
    
    return result

# Meminta input dari pengguna
input_array = input("Masukkan array INPUT (pisahkan dengan koma): ").split(',')
query_array = input("Masukkan array QUERY (pisahkan dengan koma): ").split(',')

# Menghapus spasi berlebih di setiap elemen
input_array = [word.strip() for word in input_array]
query_array = [word.strip() for word in query_array]

output = count_occurrences(input_array, query_array)
print("OUTPUT =", output)