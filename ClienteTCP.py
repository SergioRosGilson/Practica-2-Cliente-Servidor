import socket
 
class ClienteTCP:

    def _init_(self, host = "127.0.0.1", puerto = 8809):
        self.host = host
        self.puerto = puerto
        self.client_socket = None
        self.acceso = False
    
    def iniciar_cliente(self):
        # Crear el socket del cliente
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((self.host, self.puerto))
            # Solicitar al usuario la password
            password = input("Introduce la password: ").strip()
            self.client_socket.send(password.encode())
            
            # Recibir la respuesta del servidor
            respuesta = self.client_socket.recv(1024).decode()
            print("Respuesta del servidor:", respuesta)
            self.acceso = True
        except Exception as e:
            print(f"Error en la conexión: {e}")
        finally:
            self.client_socket.close()
            self.acceso = False