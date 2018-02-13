#!/usr/local/bin/python
# Filename: mycollection.py

#
# Module for simple collection classes
#

class Stack(object):
  def __init__(self):
    self.storage = []

  def push(self, newValue):
    self.storage.append(newValue)

  def top(self):
    return self.storage[len(self.storage)-1]
 
  def pop(self):
    result = self.top()
    self.storage.pop()
    return result

  def isEmpty(self):
    return len(self.storage) == 0


class Queue(object):
  def __init__(self):
    self.storage = []
   
  def add(self, newValue):
    self.push = self.storage.append(newValue)

  def front(self):
    return self.storage[0]

  def removeFront(self):
    result = self.front()
    del self.storage[0]
    return result

  def isEmpty(self):
    return len(self.storage) == 0


class Set(object):
  def __init__(self):
    self.storage = []
  
  def add(self, newValue):
    if not newValue in self.storage:
      self.storage.append(newValue) 

  def contains(self, testValue):
    return testValue in self.storage

  def remove(self, testValue):
    i = self.storage.index(testValue)
    if i:
      del(self.storage[i])

# End of mycollection.py
