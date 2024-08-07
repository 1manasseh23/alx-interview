#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments are passed
if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Function to get character details
const getCharacterDetails = (url, callback) => {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Failed to fetch character data. Status code: ${response.statusCode}`);
      return;
    }

    const character = JSON.parse(body);
    callback(character.name);
  });
};

// Main function to fetch movie details and characters
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Check if the response status is not OK (200)
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  // Iterate over each character URL in order
  characters.forEach((characterUrl) => {
    getCharacterDetails(characterUrl, (name) => {
      console.log(name);
    });
  });
});
