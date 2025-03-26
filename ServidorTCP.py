import socket
import logging
import Main

# Configuración del logging para registrar la actividad
logging.basicConfig(filename='servidor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def iniciar_servidor():
    # Configurar el socket del servidor
    host = '127.0.0.1'
    puerto = 8809
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, puerto))
    server_socket.listen(5)
    print(f"Servidor escuchando en {host}:{puerto}...")
 
    while True:
        conexion, direccion = server_socket.accept()
        print(f"Conexión establecida con {direccion}")
        try:
            datos = conexion.recv(1024)
            if not datos:
                continue
 
            # Intentar convertir los datos recibidos a entero
            try:
                numero = int(datos.decode().strip())
            except ValueError:
                respuesta = "Error: Entrada no es un número entero."
                conexion.send(respuesta.encode())
                logging.error(f"Datos inválidos recibidos: {datos.decode().strip()}")
                conexion.close()
                continue
 
        except Exception as e:
            logging.error(f"Error en la conexión: {e}")
        finally:
            conexion.close()

if __name__ == '__main__':
    iniciar_servidor()
    ClaseMain = Main()
    ClaseMain.main()
    ClaseJuego2 = Juego()
    ClaseJuego2.iniciar_juego()
    ClaseJuego2.play_music()
    ClaseJuego2.Game_Loop(print(ClaseJuego2.RoomBa_position))