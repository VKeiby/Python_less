import pickle

data = {'1': (1,2,3), '2':['a','b','c'], '3': {0,1,2,0}}
print(data)

# ������������
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# ��������������
with open('data.pickle', 'rb') as f:
    data_load = pickle.load(f)

print(data_load)
