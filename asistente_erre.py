import webbrowser
# Mis colores

RED= '\033[31m'
GREEN = '\033[32m'
RESET = '\033[39m'
# Mis colores hasta aca.

# Mis variables

cantidad = 1
urlg ="http://google.com"
urlgs = "https://www.google.com/search?q="
urlf =    "https://facebook.com"
urlfs = "https://m.facebook.com/search/top/?q="
urli = "https://www.instagram.com"
urlis = "https://www.instagram.com/explore/search/="
urly = "https://www.youtube.com"
urlys = "https://m.youtube.com/results?sp=mAEA&search_query="

#    Mis variables hasta aqui
print("Bienvenido/a seas usuario/a yo soy ERRE tu asistente de texto.")
print(RED +"==============================================================" + RESET)
print()
print(GREEN + "Ingresa [1] para ingresar a Google, [1b] para buscar algo en Google")
print()
print("Ingresa [2] para ingresar a Facebook [2b] para buscar algo en Facebook")
print()
print("Ingresa [3] para ingresar a Instagram")
print()
print("Ingresa [4] para ingresar a Youtube, [4b] para buscar algo en Youtube")
print()
opcion = input(RESET + "Que opcion deseas: ")
if opcion == "1":
     webbrowser.open(urlg,new=cantidad)
if opcion == "1b":
     busqueda =   input("\nQue quieres buscar: ")
     urlgs = urlgs + busqueda
     webbrowser.open(urlgs,new=cantidad)
if opcion == "2":
     webbrowser.open(urlf,new=cantidad)
if opcion == "2b":
     busqueda =   input("\nQue quieres buscar: ")
     urlfs = urlfs + busqueda
     webbrowser.open(urlfs,new=cantidad)
if opcion == "3":
     webbrowser.open(urli,new=cantidad)
if opcion == "4":
     webbrowser.open(urly,new=cantidad)
if opcion == "4b":
     busqueda =   input("\nQue quieres buscar: ")
     urlys = urlys + busqueda
     webbrowser.open(urlys,new=cantidad)
