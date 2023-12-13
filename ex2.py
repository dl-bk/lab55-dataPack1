# При старті програми з’являється меню з наступними
# пунктами:
# 1. Завантаження даних;
# 2. Збереження даних;
# 3. Додавання даних;
# 4. Видалення даних.
# Використайте список цілих як сховища даних. Також
# застосуйте стиснення/розпакування даних

import pickle
import gzip

nums = []

def add_data(lst, data):
    lst.append(data)

def save_data(obj, file):
    try:
        existing_data = load_data(file)
    except FileNotFoundError:
        existing_data = []
    with gzip.open(file, "wb") as wfile:
        pickle.dump(existing_data + obj, wfile)
    
    print("data saved")

def load_data(file):
    try:
        with gzip.open(file, "rb") as rfile:
            return pickle.load(rfile)
    except FileNotFoundError:
        print("File not found")

def remove_data(file, rm_data):
    try:
        existing_data = load_data(file)
        updated_data = [num for num in existing_data if num not in rm_data]
        with gzip.open(file, "wb") as wfile:
            pickle.dump(updated_data, wfile)
        
        print("data updated")

    except FileNotFoundError:
        print("File not found")



# add_data(nums, 2)
# add_data(nums, 2)
# add_data(nums, 4)
# add_data(nums, 8)
# add_data(nums, 23)

save_data(nums, "compressed_nums.pkl.gz")
nums = load_data("compressed_nums.pkl.gz")

remove_data("compressed_nums.pkl.gz", [2, 34])

nums = load_data("compressed_nums.pkl.gz")

print(nums)