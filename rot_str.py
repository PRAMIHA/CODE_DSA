def rot_str(s,goal):
  if len(s)!=len(goal):
    return False
  return goal in s+s
  s='abcde'
  goal='cdeab'
  print(rot_str(s,goal))
