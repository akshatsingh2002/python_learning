def is_even(s):
    if s%2 == 0:
            return s
        
a = filter(is_even,[1,323,2432,321,234,445])
a = list(a)
print(a)
