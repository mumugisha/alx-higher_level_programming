#!/usr/bin/node

// Script that prints all characters of a Star Wars movie

const request = require('request')
const { argv } = process
const api = 'https://swapi-api.alx-tools.com/api'

request(`${api}/films/${argv[2]}`, function (_error, response, body) {
  const characters = []
  if (response.statusCode === 200) {
    characters.push(...JSON.parse(body).characters)
    for (const character of characters) {
      request(character, function (_error, _response, body) {
        console.log(JSON.parse(body).name)
      })
    }
  }
})
