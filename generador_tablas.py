import sys
import os


# Ojo: nombre de script es primer argumento
if len(sys.argv) == 2:
    filename = str(sys.argv[1])
else:
    print "El argumente debe ser el nombre del archivo"
    sys.exit()


if os.path.isfile('./' + filename):
    extension = filename[-4:len(filename)]
    name = filename[0:len(filename)-4]

    csv = open(filename, 'r')
else:
    print "Nombre de archivo no existe"
    sys.exit()


if  extension ==  '.tsv':
    cols = csv.readline().split('\t')
elif  extension == '.csv':
    cols = csv.readline().split(',')

out = open(name + '.txt', 'w+')

print >>out, 'CREATE TABLE ' + name + ' ('

for c in cols[0:len(cols)-2]:
    # Si hay espacios ponemos corchetes alrededor
    if c.find(' ') != -1:
        c = '[' + c + ']'

    print >>out, c + " STRING,"

## La ultima columna
lastcol = cols[len(cols)-2]
if lastcol.find(' ') != -1:
    lastcol = '[' + lastcol + ']'

print >>out,  lastcol + " STRING) ;"

csv.close()
out.close()
