def movie_organizer(*args):
    movie_dict = {}
    for movie in args:
        movie_name, genre = movie[0], movie[1]
        if genre not in movie_dict.keys():
            movie_dict[genre] = []
        movie_dict[genre] += [movie_name]

    sorted_dict = dict(sorted(movie_dict.items(), key=lambda item: (-len(item[1]), item[0])))

    result = ""
    for genre, movies in sorted_dict.items():
        result += f"{genre} - {len(movies)}\n"
        result += '\n'.join(f"* {movie}" for movie in sorted(movies))
        result += "\n"

    return result

print(movie_organizer(
("The Godfather", "Drama"),
("The Hangover", "Comedy"),
("The Shawshank Redemption", "Drama"),
("The Pursuit of Happiness", "Drama"),
("The Hangover Part II", "Comedy")))