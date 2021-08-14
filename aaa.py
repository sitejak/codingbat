import numpy

speed = [15,25,14,13,24,15,25]
var = [15,25,14,13,24,15,25]
print(numpy.std(var))
print(numpy.std(speed))
x = numpy.percentile(speed,20)
print(x)

y = numpy.random.uniform(0.0,5.0,250)
print(y)