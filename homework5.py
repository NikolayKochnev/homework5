my_list = ['apple', 'banana', 'arange', 'kiwi']
print('list:',my_list)
print('First element:', my_list[0])
print('Last element:', my_list[3])
print('Sublist', my_list[3:5])
my_list[2] = 'grape'
print('Modified list', my_list)


my_dict = {'apple': 'яблоко', 'banana': 'банан', 'orange': 'апельсин'}
print(my_dict)
print('Translation:', my_dict.get('orange'))
my_dict['kiwi'] = 'киви'
print('Modified dictionary:', my_dict)