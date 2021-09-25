A = [1,1,2,3,5,8,13,21,34,55,88]
B = [1,3,5,4,7,88,66,59,40,54]
print("List A:",A)
print("List B:",B)
C = list(set (A) & set (B))
print("các phần tử trùng nhau trong 2 mảng là:", C)
D = list(set (A) ^ set(B))
print("các phần tử A không trùng với B la:", D)
E = list(set (B) ^ set(C))
print("các phần tử b không trùng với C là:", E)
