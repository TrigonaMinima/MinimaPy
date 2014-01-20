from goodreads import GoodReadsClient as gclient

key = 'App-key'
secret = 'App-secret'
uid1 = '12149311'
uid2 = '18654747'

goodreads_client = gclient(key, secret)


def get_books(user_id, shelf_name):
    return goodreads_client.get_shelf(user_id, shelf_name)

u2_books = get_books(uid2, 'to-read')
u1_books = get_books(uid1, 'to-read')

books_u1 = [book['title'] for book in u1_books]
books_u2 = [book['title'] for book in u2_books]

common = []
for i in books_u1:
    if i in books_u2:
        common.append(i)

f = open('common.txt', 'w')
for i in common:
    f.write(i)
    f.write('\n')

f.close()
print common
