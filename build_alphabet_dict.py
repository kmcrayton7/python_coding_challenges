# Create a key value pair dictionary. I followed answer #2 http://stackoverflow.com/questions/19542820/creating-dict-where-keys-are-alphabet-letters-and-values-are-1-26-using-dict-com


from string import ascii_lowercase
from collections import OrderedDict

od = OrderedDict((ch, idx) for idx, ch in enumerate(ascii_lowercase, 1))
print od