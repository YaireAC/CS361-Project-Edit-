def read_artists(file_path):
    artists = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Assuming each line in artists.txt follows the format: "Artist, genre, number of streams, country of origin"
                parts = line.strip().split(', ')
                if len(parts) == 4:
                    artist, genre, streams, country = parts
                    streams = int(streams)
                    artists.append([artist, genre, streams, country])
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return artists


def organize_by_genre(artists):
    genres = {}
    for artist in artists:
        genre = artist[1]
        if genre not in genres:
            genres[genre] = []
        genres[genre].append(artist)
    return genres


def organize_by_country(artists):
    countries = {}
    for artist in artists:
        country = artist[3]
        if country not in countries:
            countries[country] = []
        countries[country].append(artist)
    return countries


def write_documentation(artists, genres, countries, output_file):
    with open(output_file, 'w') as file:
        file.write("All Artists:\n")
        for artist in artists:
            file.write(f"{artist}\n")

        file.write("\nArtists by Genre:\n")
        for genre, artists in genres.items():
            file.write(f"\n{genre}:\n")
            for artist in artists:
                file.write(f"  {artist}\n")

        file.write("\nArtists by Country:\n")
        for country, artists in countries.items():
            file.write(f"\n{country}:\n")
            for artist in artists:
                file.write(f"  {artist}\n")


def main():
    while True:
        artists_file = input("Please enter the path to the text file with artist information: ")

        # Verify if the file exists
        try:
            artists = read_artists(artists_file)
            if artists:
                print("Data has been successfully retrieved.")
                break
            else:
                print("The file is empty or data format is incorrect. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

    output_file = "documentation.txt"

    # Organize artists by genre
    genres = organize_by_genre(artists)

    # Organize artists by country
    countries = organize_by_country(artists)

    # Write the organized data to the output file
    write_documentation(artists, genres, countries, output_file)

    print(f"Documentation has been written to {output_file}")


if __name__ == "__main__":
    main()
