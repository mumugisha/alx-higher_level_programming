#!/usr/bin/env node

// Write a script that computes the number
// of tasks completed by user id.

const request = require('request');
const { argv } = process;
const api = 'https://swapi-api.alx-tools.com/api';

request(`${api}/films/${argv[2]}`, (err, response, body) => {
  if (err) {
    console.error('Error fetching film:', err);
    return;
  }

  if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
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
  }
});

