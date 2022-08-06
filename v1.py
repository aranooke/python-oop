class Father(object):
    def __init__(self,name):
        self.name = name;
    def gamble(self):
        print("%s Играет в карты"%self.name);
    def eat(self):
        print("%s Жует очень быстро"%self.name);

class Musician():
    def __init__(self,name):
        self.name = name;
    def play_piano(self):
        print("%s play piano "%self.name);
    def eat(self):
        print("%s eat slowly as cultural person"%self.name);
class Monk():
    def __init__(self,name):
        self.name = name;
    def singing(self):
        print("%s singing all time"%self.name);

class Son(Father,Musician,Monk):
    def __init__(self,name):
        Father.__init__(self,name);
        Musician.__init__(self,name);
        Monk.__init__(self,name);

son = Son("Артём");
son.eat();
son.gamble();
son.singing();
son.play_piano();