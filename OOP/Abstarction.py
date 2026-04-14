#Hiding the complex implentation details and showing only the necessary feature to the user

from abc import ABC, abstractmethod


class RemoteControl(ABC):
    @abstractmethod
    def toggle_power(self):
        pass

class TVRemote(RemoteControl):
    def toggle_power(self):
        print("turn on TV")

tv1 = TVRemote()
tv1.toggle_power()


class Payment(ABC):
    @abstractmethod
    def pay_process(self, amount):
        pass

class Gpay(Payment):
    def pay_process(self, amount):
        print(f"payment process via gpay ",{amount})

class Ppay(Payment):
    def pay_process(self, amount):
        print(f"payment process via ppay ",{amount})

def checkout(payment_method, amount):
    payment_method.pay_process(amount)


payobj = Gpay()
checkout(payobj, 100)