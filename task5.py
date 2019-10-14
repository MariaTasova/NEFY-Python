def is_valid(braces_string):
    some_list = []
    for i in braces_string:
        if i == '(':
            some_list.append(i)
        elif i == ')':
            if len(some_list) == 0:
                return False
            else:
                some_list.pop()
    if len(some_list) == 0:
        return True


braces_string = 'T)()()()('
print(is_valid(braces_string))


