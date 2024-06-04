# microserviceB.py

def read_documentation(file_path):
    artists = []
    try:
        with open(file_path, 'r') as file:
            in_artists_section = False
            for line in file:
                if line.strip() == "All Artists:":
                    in_artists_section = True
                    continue
                if in_artists_section:
                    if line.strip() == "":
                        break
                    artist = eval(line.strip())
                    artists.append(artist)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return artists

def analyze_aesthetic(artists):
    genre_count = {}
    for artist in artists:
        genre = artist[1]
        if genre not in genre_count:
            genre_count[genre] = 0
        genre_count[genre] += 1

    if not genre_count:
        return "Unknown"

    max_genre = max(genre_count, key=genre_count.get)

    aesthetic_mapping = {
        "Pop": "Hyperpop",
        "Rap": "Streetwear",
        "Rock": "Rockstar",
        "R&B": "Y2K",
        "Country": "Cowboy aesthetic",
        "Disco": "Glitz and glamour"
    }

    return aesthetic_mapping.get(max_genre, "Unknown")

def write_aesthetic(aesthetic, output_file):
    try:
        with open(output_file, 'w') as file:
            file.write(f"{aesthetic}\n")
        print(f"Aesthetic has been written to {output_file}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    documentation_file = "documentation.txt"
    output_file = "aesthetic.txt"

    artists = read_documentation(documentation_file)

    if not artists:
        print("No artists found in the documentation file. Please check the file and try again.")
        return

    aesthetic = analyze_aesthetic(artists)
    write_aesthetic(aesthetic, output_file)

if __name__ == "__main__":
    main()
