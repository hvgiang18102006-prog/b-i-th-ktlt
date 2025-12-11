# Hoàng Văn Giang, mssv 245752021610114

class Hinhchunhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    def dientich(self):
        return self.dai*self.rong
hcn = Hinhchunhat(5,3)
print("Diện tích hình chữ nhật là:", hcn.dientich())
