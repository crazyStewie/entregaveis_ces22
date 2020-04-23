num_count = 12

#header line
line = ''
line += 3 * ' ' #space for line headers
line += 2 * ' ' #space before first element
for i in range(1, num_count + 1):
    line += '{:>4}'.format(i)
print(line)

#division line
line = ''
line += 2*' ' + ':'
line += '-'*(num_count*4 + 2)
print(line)

#table lines
for i in range (1, num_count + 1):
    line = '{:>2}:'.format(i)
    line += 2*' '
    for j in range (1, num_count + 1):
        line += '{:>4}'.format(i*j)
    print(line)
