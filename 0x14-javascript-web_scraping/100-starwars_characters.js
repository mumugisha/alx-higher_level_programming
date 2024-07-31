#!/usr/bin/node

// Script that prints all characters of a Star Wars movie

const request = require('request');
const argv = process.argv;
const api = 'https://swapi-api.alx-tools.com/api';

// Check if a movie ID is provided
if (argv.length < 3) {
  console.error('Usage: ./script.js <movie_id>');
  process.exit(1);
}

const movieId = argv[2];

request(api + '/films/' + movieId, function (_error, response, body) {
  if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.forEach(function (characterUrl) {
      request(characterUrl, function (_error, _response, body) {
        console.log(JSON.parse(body).name);
      });
    });
  } else {
    console.error('Failed to retrieve movie data.');
  }
});
