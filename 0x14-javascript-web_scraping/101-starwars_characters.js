#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});
function printCharacters (characters, index) {
  if (index < characters.length) {
    request(characters[index], (error, response, body) => {
      if (!error) {
        console.log(JSON.parse(body).name);
        printCharacters(characters, index + 1);
      }
    });
  }
}
