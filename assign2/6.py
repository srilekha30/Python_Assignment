thevariable=raw_input()
try:
  thevariable
  a=float(thevariable)
  print "this is a number "
except ValueError:
  print "this is not a num"
