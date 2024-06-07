import socket

def client():
    # Obtener el hostname (ya que tanto cliente como server correrán en tu máquina)
    host = socket.gethostname()

    # Definir el número de puerto para comunicarse con el servidor
    port = 1257
    # TO DO
    
    # Crear un objeto socket
    client_socket = socket.socket()

    # Conectar al servidor especificando el hostname y el puerto
    client_socket.connect((host, port))

    # Pedir al usuario un input
    message = input("Ingresá un mensaje (Poner 'chau' para salir): ")
    
    while message.lower().strip() != "bye":
        
        # Enviar el mensaje al server (usar message.encode())
        # TO DO
        client_socket.send (message.encode())
        # Recibir una respuesta del servidor
    data = client_socket.recv(1024).decode()

        # Mostrar el mensaje recibido del servidor
    print("Received from server: " + data)
        
        # Pedir un nuevo mensaje
        # TO DO
    message = input ("Ingresa un nuevo mensaje (Poner 'chau'para salir):")
    # Cerrar la conexión
    # TO DO
    client_socket.close()

if __name__ == "__main__":
    client()