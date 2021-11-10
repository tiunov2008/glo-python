class Storage:
    def append(self, user_data):
        file = open('./db.txt', 'a')
        file.write(user_data + '\n')
        file.close()
    def read(self):
        file = open('./db.txt', 'r')
        results = file.readlines()
        for i in results:
            print(i, end='')
        file.close()
    def write(self, user_data):
        file = open('./db.txt', 'w')
        file.write(user_data)
        file.close()

bd = Storage()
bd.write('')
bd.append('123')
bd.append('456')
bd.append('789')
bd.read()
bd.write('123456789')
bd.read()