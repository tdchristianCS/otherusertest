n = input('Enter a float: ')

try:
    float(n)
    print('Good')
except:
    print('Could not interpret that as a float')
