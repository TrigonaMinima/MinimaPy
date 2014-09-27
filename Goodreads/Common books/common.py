from goodreads import GoodReadsClient as gclient

key = 'App-key'
secret = 'App-secret'
uid1 = '12149311'
uid2 = '18654747'

goodreads_client = gclient(key, secret)


def get_books(user_id, shelf_name):
    return goodreads_client.get_shelf(user_id, shelf_name)

u2_books = [book['title'] for book in get_books(uid2, 'to-read')]
for book in get_books(uid2, 'read'):
    u2_books.append(book['title'])
for book in get_books(uid2, 'currently-reading'):
    u2_books.append(book['title'])
u2_books.sort()

u1_books = [book['title'] for book in get_books(uid1, 'to-read')]
for book in get_books(uid1, 'read'):
    u1_books.append(book['title'])
for book in get_books(uid1, 'currently-reading'):
    u1_books.append(book['title'])
u1_books.sort()


#unicode(book['title']).encode("utf-8")


'''common = []
for i in u1_books:
    if i in u2_books:
        common.append(i)'''

f = open('u1.txt', 'w')

for i in u1_books:
    f.write(i)
    f.write('\n')

f.close()

f = open('u2.txt', 'w')

for i in u2_books:
    f.write(unicode(i).encode("utf-8"))
    f.write('\n')

f.close()
