'''
������ � ���������� �������
'''

# ������� ����������/ �������� ����� � ������ ������
# f = open('data')
# content  = f.read()
# print(content)
# f.close()

# ������� ���� � ������ ������ (���������� ���������)
# f = open('data', 'w')
# content  = f.read()
# print(content)
# f.close()

# ���������� ����� ���������
# f = open('data')
# for line in f:
#     print(line)
# f.close()


# �������� ���������
with open('data') as f:
    line = f.readline() # ���������� ����� ������
    print(line)
  # for line in f:
  #     print(line)

# ���������� ��������

with open('data','r') as f:
    data = f.read(10) # ���������� ����� ������
    print(data, type(data))


# ������ � ����

# with open('data_new', 'w') as f:
#   f.writeline('This is new file!')


# ������ � �������
data = ['1\n','2 \n','3 \n'] # '\n' - ������� ������

with open('data_new', 'w') as f:
  f.writelines(data)
