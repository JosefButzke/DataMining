import pylab

names = ['anne','barbara','cathy']
counts = [3230,2002,5456]

pylab.figure(1)
x = range(3)
pylab.xticks(x, names)
pylab.plot(x,counts,"g")

pylab.show()