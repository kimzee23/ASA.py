import datetime  
def display_menu():
    print("1. Add a Movie")
    print("2. Rate a Movie")
    print("3. View Average Ratings")
    print("4. Exit....! \U0001F44B\U0001F6AA")

def get_add_movie():
    while True:
        name = input("Enter movie Name: ").strip()
        if name:
            return name
        print("Invalid input. Please enter a valid movie name.")
def get_date():
   dating = datetime.datetime.now()
   print(dating.strftime("%Y, %B, %d, %I:%p"))

def get_rating_movie():
    while True:
        try:
            get_date()
            rating = float(input("Rate the movie between (1-5): "))
            if 1 <= rating <= 5:
                return rating
            else:
                print("Invalid input. Enter a rating between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    movies = {}  
    while True:
        display_menu()
        choice = input("Choose between (1-4): ")
        match choice:
            case "1":
                name = get_add_movie()
                if name not in movies:
                    movies[name] = []  
                    print(f"Movie '{name}' added successfully.")
                else:
                    print("Movie already exists.")
            case "2":
                print("="*40)
                name = input("Enter the movie name you want to rate: ").strip()
                if name in movies:
                    rating = get_rating_movie()
                    movies[name].append(rating)
                    print(f"You Rated {name} {rating} it has been added.")
                else:
                    print("Movie not found. Please add the movie first.")
                    
            case "3":
                if movies:
                    for movie, ratings in movies.items():
                        average_rating = sum(ratings) / len(ratings) if ratings else 0
                        print(f" {movie}: Average Rating: {average_rating:.2f} found")
                else:
                    print("No movies available.")
            case "4":
                    print("Bye: \U0001F44B your ratings are valid...")
                    break
            case _:
                print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
  

