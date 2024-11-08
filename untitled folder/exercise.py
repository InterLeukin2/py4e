from bokeh.colors.named import mediumblue


class Dog:  # 父类
    def __init__(self, name, age,color):#构造函数，也可以不构造
        self.name = name  # 公有属性，也可以私有看心情哈哈哈
        self.age = age
        self.__color=color
        self._species = "Canis lupus familiaris"  # 受保护属性，也可以不保护可能

    def get_color(self):  # 提供一个方法来访问私有属性,前提是私有属性也被定义
            return self.__color
    def get_species(self):
            return self._species

    def speak(self):
        print(f"{self.name} says woof!")

# 子类 BigDog 定义了一个私有属性
class BigDog(Dog):#只是定义没有初始化，每个方法和属性都要重写一遍
    def __init__(self, name, age, size,color):
        super().__init__(name, age,color)# 初始化父类的属性，不初始化后面可能报错，啰嗦
        self.__size = size  # 子类的私有属性

    def get_size(self):  # 获取私有属性的方法
        return self.__size

    def speak(self):
        super().speak()  # 调用父类的 speak 方法
        print(f"I'm a big dog of size {self.__size}!")

big_dog_instance = BigDog("Buddy", 5, "Large","white")
print(big_dog_instance.name)  # 输出: Buddy
print(big_dog_instance.age)   # 输出: 5
print(big_dog_instance.get_size())  # 输出: Large

dog_a = BigDog ("aa",3,"medium","black")
a=dog_a.speak()
print(a)
dog_b=Dog('bb',5,"blue")
b=dog_b.get_color()
c=dog_b.get_species()
print(c)
