class Father:
    def skill1(self):
        print("Programming")

class Mother:
    def skill2(self):
        print("Teaching")

class Child(Father, Mother):
    pass

c = Child()

c.skill1()
c.skill2()