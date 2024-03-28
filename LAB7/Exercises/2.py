import pygame

def load_and_play_song(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

def pause_or_unpause(paused):
    if paused:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
    return not paused

def adjust_volume(direction):
    current_volume = pygame.mixer.music.get_volume()
    new_volume = min(1.0, max(0.0, current_volume + direction))
    pygame.mixer.music.set_volume(new_volume)

def main():
    pygame.init()
    screen = pygame.display.set_mode((960, 600))
    songs = ['C:/Users/user/Desktop/pp2/LAB7/Songs/ayau-shiza-mdee-basqany_(muzzonas.ru).mp3',
             'C:/Users/user/Desktop/pp2/LAB7/Songs/Chase Atlantic - Swim.mp3',
             'C:/Users/user/Desktop/pp2/LAB7/Songs/maniac.mp3',
             'C:/Users/user/Desktop/pp2/LAB7/Songs/The_Weeknd_-_Is_There_Someone_Else.mp3']
    current_song_index = 0
    paused = False

    font = pygame.font.Font(None, 36)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    current_song_index = (current_song_index + 1) % len(songs)
                    load_and_play_song(songs[current_song_index])
                    paused = False
                elif event.key == pygame.K_LEFT:
                    current_song_index = (current_song_index - 1) % len(songs)
                    load_and_play_song(songs[current_song_index])
                    paused = False
                elif event.key == pygame.K_SPACE:
                    paused = pause_or_unpause(paused)
                elif event.key == pygame.K_UP:
                    adjust_volume(0.02)
                elif event.key == pygame.K_DOWN:
                    adjust_volume(-0.02)

        screen.fill((0, 0, 0))
        text = font.render("Now playing: " + songs[current_song_index], True, (255, 255, 255))
        screen.blit(text, (10, 10))
        volume_text = font.render("Volume: {:.0%}".format(pygame.mixer.music.get_volume()), True, (255, 255, 255))
        screen.blit(volume_text, (10, 50))
        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()
