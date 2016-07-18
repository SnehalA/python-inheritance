class A: # super class
  def f(self):
    print "in f"

  def h(self):
    print "in h"

class B(A): # sub class
  def f(self):
    print "in B:f"

def test(x):
  x.f()
  x.h()

test(A())
test(B())