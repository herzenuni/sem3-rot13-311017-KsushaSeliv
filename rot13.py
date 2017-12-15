def rot_13(text):
 def rot(englishlang):
  i='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.find(englishlang)
  if i!=-1:
   return 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'[i]
  else:
   return englishlang
 return "".join(map(rot, text))
print(rot_13('noenpnqnoen'))  #результат: abracadabra
