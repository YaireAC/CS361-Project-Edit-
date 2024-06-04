def get_music_data():
    # Prompt the user for music details
    artist_name = input("Enter the name of the artist: ")
    genre = input("Enter the genre of the music: ")
    num_streams = input("Enter the number of streams: ")
    country_origin = input("Enter the country of origin: ")

    return artist_name, genre, num_streams, country_origin


def save_to_file(data, filename='artists.txt'):
    with open(filename, 'a') as file:
        file.write(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}\n")


def main():
    while True:
        # Get music data from the user
        music_data = get_music_data()

        # Save the data to the file
        save_to_file(music_data)

        # Ask the user if they want to add another entry
        another = input("Do you want to add another entry? (yes/no): ").strip().lower()
        if another != 'yes':
            break


if __name__ == "__main__":
    main()
