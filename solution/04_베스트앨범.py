from collections import defaultdict

def solution(genres, plays):
    answer = []
    num_of_play = defaultdict(int)
    for genre, play in zip(genres, plays):
        num_of_play[genre] += play
        
    sorted_genres = sorted(list(num_of_play.items()), key=lambda x:x[1], reverse=True)
        
    song_list = defaultdict(list)
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        song_list[genre].append((play, idx))
    for songs in song_list.values():
        songs.sort(key=lambda x:(-x[0], x[1]))

    for genre, _ in sorted_genres:
        two_songs = song_list[genre][:2]
        for _, idx in two_songs:
            answer.append(idx)

    return answer