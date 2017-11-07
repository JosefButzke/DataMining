
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
vet = []
x = sorted(x)

vet.append(min(x))
vet.append(x[len(x)/8])
vet.append(x[2*len(x)/8])
vet.append(x[3*len(x)/8])
vet.append(x[4*len(x)/8])
vet.append(x[5*len(x)/8])
vet.append(x[6*len(x)/8])
vet.append(max(x))

print vet
