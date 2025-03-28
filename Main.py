from Launcher import Launcher
from Juego import Juego

if __name__ == '__main__':
        ClaseLauncher = Launcher()
        ClaseLauncher.launcher()
        ClaseJuego2 = Juego()
        ClaseJuego2.iniciar_juego()
        ClaseJuego2.play_music()
        ClaseJuego2.Game_Loop(print(ClaseJuego2.RoomBa_position))