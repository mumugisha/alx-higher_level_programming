#!/usr/bin/env node

const request = require('request');
const { argv } = process;
const api = 'https://swapi-api.alx-tools.com/api';

// Function to fetch and print character names
const fetchCharacterNames = (characterUrls) => {
  characterUrls.forEach((character) => {
    request(character, (err, response, body) => {
      if (err) {
        console.error('Error fetching character:', err);
        return;
      }
      if (response.statusCode === 200) {
        console.log(JSON.parse(body).name);
      }
    });
  });
};

request(`${api}/films/${argv[2]}`, (err, response, body) => {
  if (err) {
    console.error('Error fetching film:', err);
    return;
  }

  if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    fetchCharacterNames(characters);
  }
});
