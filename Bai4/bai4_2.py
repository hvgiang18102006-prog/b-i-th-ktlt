# Hoàng Văn Giang, mssv 245752021610114

# Không in ra những ký tự "không nhìn thấy"
S = input('Nhập chuỗi:')
for ch in S:
    if ch not in [' ', '\t']:
        print(ch)
