dct = {
    "details": "interesting",
    "length": lambda x: len(str(x)),
    "is_int": lambda x: type(x) == int,
}

print(dct["length"]("ram"))
print(dct["is_int"]("ram"))
print(dct["is_int"](1))
print(dct)
