def checarNota(nota):
  if nota >=0 and nota <= 10:
    return "válido"
  else:
    return "inválido"
  
print(checarNota(5))
print(checarNota(-5))
print(checarNota(50))
print(checarNota(9))