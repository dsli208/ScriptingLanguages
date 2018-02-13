from mycollection import *

print '-------------- stack ------------'
a = Stack()
a.push(1)
a.push(2)
a.push(3)

print 'Top element of stack is: ', a.top()
print 'Is stack empty? ', a.isEmpty()


print '-------------- queue ------------'
b = Queue()
b.add('M')
b.add('N')
b.add('O')
print 'Front element of queue is: ', b.front()

b.removeFront()
print 'New front element is: ', b.front()
print 'Is queue empty? ', b.isEmpty()


print '-------------- set ------------'
c = Set()
c.add('first')
c.add('second')
c.add('third')
c.add('second')

print 'c contains third?', c.contains('third')
print 'c contains second?', c.contains('second')

c.remove('second')
print 'After removal, c contains second? ', c.contains('second')
