import socket
 
class ClienteTCP:

    def iniciar_cliente():
        host = '127.0.0.1'
        puerto = 8809
    
        # Crear el socket del cliente
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((host, puerto))
            
            # Recibir la respuesta del servidor
            respuesta = client_socket.recv(1024).decode()
            print("Respuesta del servidor:", respuesta)
        except Exception as e:
            print(f"Error en la conexión: {e}")
        finally:
            client_socket.close()