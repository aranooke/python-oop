from abc import ABCMeta,abstractmethod;
class Employee(object,metaclass = ABCMeta):
    
    def __init__(self, name):  # инициализируем класс
        self._name = name  # задаем значение атрибута, принятого от аргумента

    @property  # геттер
    def name(self):
        return self._name

    @abstractmethod  # геттер
    def get_salary(self):
        pass


class Manager(Employee):  # определяем класс, наследуем от класса Employee

    # Подумайте об этом: что произойдет, если вы не определите метод построения
    def __init__(self, name):  # инициализируем класс
        # Подумайте: что произойдет, если вы не вызовете конструктор родительского класса
        super().__init__(name)

    def get_salary(self):  # геттер
        return 12000;
class Programmist(Employee):
    def __init__(self,name):
        super().__init__(name);
    def working_hour(self,hour):
        self.hour = hour;
    def get_salary(self):
        return self.hour * 100;

class Salesman(Employee):
    def __init__(self,name):
        super().__init__(name);
    def bonus(self,selling):
        self.selling = selling*0.05;  

    def get_salary(self):
        return 1500 + self.selling;
    
workers = [Manager('Иван'),Programmist('Артем'),Salesman('Игорь')];
for itr in workers:
    if isinstance(itr,Programmist):
        working_hour = int(input("Введите кол-во рабочих часов"));
        itr.working_hour(working_hour);
        print("Кол-во заработанныых денег про граммистом за {0} часов работы".format(working_hour),itr.get_salary());
    elif isinstance(itr,Salesman):
        sales = int(input("На сколько денег продала товара?"));
        itr.bonus(sales);
        print("Кол-во заработанных денег продавщицой в этом году {0}".format(itr.get_salary()));
        pass;  
    

