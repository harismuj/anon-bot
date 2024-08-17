import vlc
import time

def play_m3u(m3u_file):
    # Inisialisasi VLC instance
    instance = vlc.Instance('--no-xlib')

    # Buat media player
    player = instance.media_player_new()

    # Buka file M3U
    media_list = instance.media_list_new([m3u_file])
    player.set_media_list(media_list)

    # Putar daftar putar
    player.play()

    # Tunggu sampai putaran selesai
    while player.is_playing():
        time.sleep(1)

    # Hentikan pemutaran
    player.stop()

if __name__ == "__main__":
    m3u_file = 'Tvku.m3u'
    play_m3u(m3u_file)
