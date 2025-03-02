def is_valid_binary(input):
    S = {"00", "10", "010", "01001"}  # Himpunan S yang berisi substring valid
    queue = [0]  # Queue posisi pengecekan, posisi awal pada index 0
    
    while queue:
        pos = queue.pop(0) # Ambil nilai pertama dari queue dan menghapusnya
        if pos == len(input):
            return True # Return true jika pengecekan sudah mencapai akhir string
        
        # For loop untuk setiap substring valid
        for s in S:
            if input.startswith(s, pos):  # Cek setiap substring apakah cocok dengan bagian awal string dari posisi 'pos'
                queue.append(pos + len(s))  # Tambahkan posisi baru ke queue
    
    return False  # Return false jika tidak dapat mencapai posisi akhir string menggunakan semua substring dari S

binInput = input("Masukkan string biner: ").strip() # Input string biner fungsi strip() digunakan untuk menghilangkan whitespace di awal dan akhir string

if is_valid_binary(binInput):
    print("VALID")
else:
    print("TIDAK VALID")