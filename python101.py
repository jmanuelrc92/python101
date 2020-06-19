def sayHelloWParams(name, title):
    return "Hi " + name + " you are " + title

def sayHello():
    print("Hi man, how are you?")

"""You can pass parameters with name in any order
"""
print(sayHelloWParams(title="the king", name="johndoe"))

''' Hola... '''
try:
    print("Algo")
except Exception as x:
    print("algo ocurrio: " + type(x).__name__)

try:
    print("Algo")
except TypeError:
    print("algo ocurrio: ")
except ValueError:
    print("algo ocurrio: ")


raise ValueError("Mensaje")