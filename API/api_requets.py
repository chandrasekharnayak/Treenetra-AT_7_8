import requests

url = 'https://jsonplaceholder.typicode.com/todos'


# response = requests.get(url)
#
# if response.status_code == 200:
#     print('Requests Successful')
#     data = response.text
#     for i in data:
#         print(i)
#     with open('todos_json.txt','w') as file:
#         file.write(data)
# else:
#     print('Failed')

# li = []
# if response.status_code == 200:
#     data = response.json()
#     # print(data)
#     for i in data:
#         if i['userId']==2:
#             li.append(i['id'])
# print(len(li),li)


#---------------Post---------------

# def print_response(response):
#     print(f'Status code {response.status_code}')
#     print(response.json())

# new_todo = {
#     "userId": 1,
#     "id": 201,
#     "title": "New Todo added",
#     "completed": True
# }
#
# post_response = requests.post(url,json=new_todo)
# print_response(post_response)

#---------------------------------------- Patch-----------------------------------------
# update_data = {
#     'completed':True
# }
#
# patch_response = requests.patch(f'{url}/2',json=update_data)
# print_response(patch_response)

#---------------------------------- Put-----------------------------------
# upadted_data_put = {
#     "userId": 11,
#     "title": "New Todo added put",
#     "completed": False
# }
#
# put_response = requests.put(f'{url}/201',json=upadted_data_put)
# print_response(put_response)

#---------------------------------Delete-------------------------------------
# delete_response = requests.delete(f'{url}/1')
# print_response(delete_response)

#------------------------get ------------------------

# def print_response_data(response):
#     return response.json()
#
# get_response = requests.get(url)
# data = print_response_data(get_response)
# # print(data)
# for list_data in data:
#     if list_data['id']==2:
#         print(list_data['userId'],list_data)

