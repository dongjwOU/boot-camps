def divide_it(x, y):
    try:
        out = x / y
    except ZeroDivisionError:
        print '   Divide by zero!'
        out = None
    except:
        print ' It's not division by zero but something is wrong!'
        out = None
    return out


print divide_it(4,2)
print divide_it(4,0)
print divide_it('a',2)

