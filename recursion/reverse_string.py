def reverse(string):
    if len(string) == 1:
        return string
    len_str = len(string)
    return string[len_str - 1] + reverse(string[: len_str - 1])


print(reverse("pranjal"))
print(reverse("nepal"))
print(reverse("pranjal is my name"))
