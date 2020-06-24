# Software Libre
# autor: Esteban Aulestia
# 16/06/2020

v=input("ingrese una cadena: ")
consonantes = ['B','C','D','F','G','H','J','K','L','M','Ñ','P','Q','R','S','T','V','W','X','Y','Z',
          'b','c','d','f','g','h','j','k','l','m','ñ','p','q','r','s','t','v','w','x','y','z']
res = ' '
for letra in v:
    if letra not in consonantes:
        res += letra
print(res)