<<<<<<< HEAD
from menu_item import MenuItem

class Food(MenuItem):
    def __init__(self, name, price, calorie_count):
        super().__init__(name, price)
        self.calorie_count = calorie_count

    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.calorie_count) + 'kkal)'

    def calorie_info(self):
        print('kcal: ' + str(self.calorie_count))
=======
from menu_item import MenuItem

class Food(MenuItem):
    def __init__(self, name, price, calorie_count):
        super().__init__(name, price)
        self.calorie_count = calorie_count

    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.calorie_count) + 'kkal)'

    def calorie_info(self):
        print('kcal: ' + str(self.calorie_count))
>>>>>>> 735431c38aea59856703bd378cd33239bbed596f
