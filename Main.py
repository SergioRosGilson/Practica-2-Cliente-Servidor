from Launcher import Launcher
from Juego import Juego
from ServidorTCP import ServidorTCP

if __name__ == '__main__':
        ClaseServidor = ServidorTCP()
        ClaseServidor.iniciar_servidor()
        ClaseLauncher = Launcher()
        ClaseLauncher.launcher()
        ClaseJuego2 = Juego()
        ClaseJuego2.iniciar_juego()
        ClaseJuego2.play_music()
        ClaseJuego2.Game_Loop(print(ClaseJuego2.RoomBa_position))