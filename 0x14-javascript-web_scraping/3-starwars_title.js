#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  const data = JSON.parse(body);
  const title = data.title;
  console.log(title);
});
