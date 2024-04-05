class MyClass:
    class_attribute = "class attribute"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    @classmethod
    def class_method(cls):
        print("This is a class method")
        print("Accessing class attribute:", cls.class_attribute)

    @classmethod
    def create_instance(cls, instance_attribute):
        print("Creating instance via class method")
        return cls(instance_attribute)

# Accessing a class method without instantiating the class
MyClass.class_method()

# Using a class method as an alternative constructor
instance = MyClass.create_instance("instance attribute")
print("Instance attribute:", instance.instance_attribute)