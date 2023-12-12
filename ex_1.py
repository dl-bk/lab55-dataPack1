# Користувач заповнює з клавіатури список цілих.
# Стисніть отримані дані та збережіть їх у файл. Після цього
# завантажте дані з файлу в новий список.

import pickle

nums = [int(num) for num in input("Enter numbers by space: ").split()]

with open("nums.pkl", "wb") as wfile:
    pickle.dump(nums, wfile)

print(pickle.dumps(nums))

with open("nums.pkl", "rb") as rfile:
    numbers = pickle.load(rfile)

print(numbers)