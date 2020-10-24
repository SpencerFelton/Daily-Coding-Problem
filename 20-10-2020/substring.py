def sub_string(substring, string):
    sub = ""
    for sub_letters in substring:
        if(sub_letters in string and sub_letters not in sub):
                sub += sub_letters
    print(sub)
    return sub

#test case:
string1 = "aaaaaaaaaaaaa"
string1 = list(string1)
substring = "eci"
substring = list(substring)

sub_string(substring, string1)
