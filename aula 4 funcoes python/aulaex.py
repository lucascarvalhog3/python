def saudacao(hora):
  if hora >= 5 and hora <= 12:
    return "bom dia"
  elif hora > 12 and hora <= 18:
    return "boa tarde"
  else:
    return "boa noite"

hr = int(input("Digite que horas são: "))
print(saudacao(hr))
xy = int(input("Digite outra hora: "))
print(saudacao(xy))

daqui_2_horas = int(input("Digite a hora: "))
print(saudacao(daqui_2_horas + 2))