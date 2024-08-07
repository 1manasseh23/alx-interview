#!/usr/bin/node
import requests
import sys

def get_characters(movie_id):
    url = f"https://swapi.dev/api/films/{movie_id}/"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: unable to fetch data for movie ID {movie_id}")
        return
    
    data = response.json()
    character_urls = data['characters']
    
    for character_url in character_urls:
        char_response = requests.get(character_url)
        if char_response.status_code != 200:
            print(f"Error: unable to fetch data for character URL {character_url}")
            continue
        char_data = char_response.json()
        print(char_data['name'])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-starwars_characters.py <movie_id>")
        sys.exit(1)

    movie_id = sys.argv[1]
    get_characters(movie_id)


// // Import the request module to handle HTTP requests
// const request = require('request');

// // Check if the correct number of arguments are passed
// if (process.argv.length !== 3) {
//   console.error('Usage: ./0-starwars_characters.js <Movie ID>');
//   process.exit(1);
// }

// // Store the movie ID from the command line argument
// const movieId = process.argv[2];
// // Construct the API URL using the movie ID
// const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// // Make a request to the API to get the movie details
// request(apiUrl, (error, response, body) => {
//   // Handle any errors that occur during the request
//   if (error) {
//     console.error(error);
//     return;
//   }

//   // Check if the response status is not OK (200)
//   if (response.statusCode !== 200) {
//     console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
//     return;
//   }

//   // Parse the response body to get the film details
//   const film = JSON.parse(body);
//   // Get the list of character URLs from the film details
//   const characters = film.characters;

//   // Iterate over each character URL
//   characters.forEach((characterUrl) => {
//     // Make a request to get the character details
//     request(characterUrl, (error, response, body) => {
//       // Handle any errors that occur during the request
//       if (error) {
//         console.error(error);
//         return;
//       }

//       // Check if the response status is not OK (200)
//       if (response.statusCode !== 200) {
//         console.error(`Failed to fetch character data. Status code: ${response.statusCode}`);
//         return;
//       }

//       // Parse the response body to get the character details
//       const character = JSON.parse(body);
//       // Print the character's name to the console
//       console.log(character.name);
//     });
//   });
// });
