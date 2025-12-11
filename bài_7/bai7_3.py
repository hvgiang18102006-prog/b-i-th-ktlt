# Hoàng Văn Giang, mssv 245752021610114

# Mở file ở chế độ đọc
with open('D:a.txt', 'r', encoding='utf-8') as file:
    content = file.read()  # Đọc toàn bộ nội dung
    print(content)         # In ra màn hình
