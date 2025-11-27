# Hoàng Văn Giang, mssv 245752021610114

# nhập 1 chuỗi từ bàn phím, loại bỏ các chữ số và in ra nội dung mới
s = input("nhập chuỗi số: ")
moi = ' '
for ch in s:
    if not ch.isalpha():
        moi += ch
print("chuỗi mới:",moi)
