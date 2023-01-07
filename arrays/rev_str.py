def reverse_string(string):
    len_str = len(string)
    if len_str <= 1:
        return string
    reversed = ""
    for i in range(len_str):
        reversed += string[len_str - i - 1]
    print(reversed)


reverse_string("Pranjal is a Good Boy!")
