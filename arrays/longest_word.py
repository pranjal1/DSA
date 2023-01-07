import re


def LongestWord(sen):

    # code goes here
    m = re.sub(r"[^a-z\s]+", "", sen)
    print(m)
    texts = m.split(" ")
    max_str = ""
    for t in texts:
        if len(t) > len(max_str):
            max_str = t
    return max_str


# keep this function call here
print(LongestWord("pranjal1234 askjashf#@$asdf"))
print(LongestWord("fun&!! time"))
