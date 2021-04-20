def shrink_string(st):
    new_string = ""
    lastChar = ''
    reps = 0
    for c in st:
        if lastChar != c:
            if lastChar != '':
                new_string += lastChar + str(reps)
            lastChar = c
            reps = 1
        else:
            reps += 1
    new_string += lastChar + str(reps)
    return new_string  
            
string = 'aabbbbcdddeaaaaa'
print(string)
print(shrink_string(string))
