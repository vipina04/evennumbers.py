def count(val):
  vow=0
  cons=0
  for i in range(len(val)):
      if val[i]in["a","e","i","o","u"]:
          vow+=1
      else:
          cons = cons+1
  print("count of vowels",vow)
  print("count of consonants", cons)

count("abcdefg")




