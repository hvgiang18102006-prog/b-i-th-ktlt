# Hoang Van Giang, mssv 245752021610114
def get_sum(*num):
 tmp = 0
 # duyet cac tham so
 for i in num:
  tmp += i
 return tmp
result = get_sum(1, 2, 3, 4, 5)
print(result)
