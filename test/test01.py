def fun01():
    my_dict = {'level': 'warning'}
    level = my_dict.get('level')
    print(level)
    info = my_dict.get('')
    if info:
        print(info)
    else:
        a=None
        print(a)


if __name__ == '__main__':
    fun01()
