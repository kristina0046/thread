import threading
import time
import random

class BankAccount:

    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                new_balance = self.balance - amount
                time.sleep(0.0001)
                self.balance = new_balance

def client(account):
    amount = random.randint(10, 100)
    account.withdraw(amount)

account = BankAccount(5000)
threads = []

for i in range(10):
    t = threading.Thread(target=client, args=(account,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("zostatok:", account.balance)