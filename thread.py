import threading

numbers = []

user_input = input("Zadajte čísla oddelene medzerou: ")
numbers = list(map(int, user_input.split()))


def find_max(nums):
    max_value = max(nums)
    print("Najväčšia hodnota:", max_value)

def find_min(nums):
    min_value = min(nums)
    print("Najmenšia hodnota:", min_value)

thread1 = threading.Thread(target=find_max, args=(numbers,))
thread2 = threading.Thread(target=find_min, args=(numbers,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()