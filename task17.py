all_users = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}
# пользователи не в сети
offline_users = {'id3', 'id9', 'id7', 'id2', 'id4', 'id6'}
print(all_users - offline_users)

# all_users = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}
# offline_users = {'id3', 'id9', 'id7', 'id2', 'id4', 'id6'}
# online_user = set()
# for user_a in all_users:
#     if user_a not in offline_users:
#         online_user.add(user_a)
# print(online_user)



#Даны читатели книг
readers_books = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1' }

#Даны читатели газет
readers_magazines = { 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}
print(readers_books & readers_magazines)

# all_readers = set()
# for reader_b in readers_books:
#     for reader_m in readers_magazines:
#         if reader_b in readers_magazines and reader_m in readers_books:
#             all_readers.add(reader_b)
#             all_readers.add(reader_m)
# print(all_readers)
