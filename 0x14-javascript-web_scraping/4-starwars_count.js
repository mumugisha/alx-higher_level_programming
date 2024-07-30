#!/usr/bin/node

// Write a script that prints the number of movies
// where the character “Wedge Antilles” is present.

const request = require('request');
const args = process.argv;

request.get(args[2], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  if (response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    let count = 0;
    for (const movie of movies) {
      movie.characters.forEach(url => {
        if (url.includes('18')) {
          count++;
        }
      });
    }
    console.log(count);
  }
});
