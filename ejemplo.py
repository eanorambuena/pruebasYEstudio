import webview 

busqueda = "tortuga" # Busqueda a realizar

URL = 'https://www.google.com/search?q=' + "+".join(busqueda.split(" ")) 

PAGE = URL.split("://") # Separar la URL en protocolo y direccion
PROTOCOL = PAGE[0] # Protocolo
ADRESS = PAGE[1].split("/") # Direccion
TITLE = ADRESS[0] # Titulo

webview.create_window(TITLE, URL, width=480, height=720) # Crear la ventana

webview.start() # Iniciar la ventana
