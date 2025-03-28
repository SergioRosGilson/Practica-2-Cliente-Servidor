from Launcher import Launcher
from Juego import Juego
from ServidorTCP import ServidorTCP
from ClienteTCP import ClienteTCP

if __name__ == '__main__':
        ClaseServidor = ServidorTCP()
        ClaseServidor.iniciar_servidor()
        ClaseCliente = ClienteTCP()
        ClaseCliente.iniciar_cliente()
        ClaseLauncher = Launcher()
        ClaseLauncher.launcher()
        ClaseJuego2 = Juego()
        ClaseJuego2.iniciar_juego()
        ClaseJuego2.play_music()
        ClaseJuego2.Game_Loop(print(ClaseJuego2.RoomBa_position))