import tensorflow as tf

create_placeholders = __import__("./0-create_placeholders.py").create_placeholders

x, y = create_placeholders(784, 10)
print(x)
print(y)
