f='23|8|1|20|4|15|25|15|21|11|14|15|23|1|2|15|21|20|1|2|3'
while '26' in f:
    f=f.replace('26', 'z',1)
while '25' in f:
    f=f.replace('25', 'y',1)
while '24' in f:
    f=f.replace('24', 'x',1)
while '23' in f:
    f=f.replace('23', 'w',1)
while '22' in f:
    f=f.replace('22', 'v',1)
while '21' in f:
    f=f.replace('21', 'u',1)
while '20' in f:
    f=f.replace('20', 't',1)
while '18' in f:
    f=f.replace('19', 's',1)
while '18' in f:
    f=f.replace('18', 'r',1)
while '17' in f:
    f=f.replace('17', 'q',1)
while '16' in f:
    f=f.replace('16', 'p',1)
while '15' in f:
    f=f.replace('15', 'o',1)
while '14' in f:
    f=f.replace('14', 'n',1)
while '13' in f:
    f=f.replace('13', 'm',1) 
while '12' in f:
    f=f.replace('12', 'l',1)
while '11' in f:
    f=f.replace('11', 'k',1)
while '10' in f:
    f=f.replace('10', 'j',1)
while '9' in f:
    f=f.replace('9', 'i',1)
while '8' in f:
    f=f.replace('8', 'h',1)
while '7' in f:
    f=f.replace('7', 'g',1)
while '6' in f:
    f=f.replace('6', 'f',1)
while '5' in f:
    f=f.replace('5', 'e',1)
while '4' in f:
    f=f.replace('4', 'd',1)
while '3' in f:
    f=f.replace('3', 'c',1)
while '2' in f:
    f=f.replace('2', 'b',1)
while '1' in f:
    f=f.replace('1', 'a',1)
print(f)
while '|' in f:
    f=f.replace('|',' ',1)
print(f)
