#!/usr/bin/node
const request = require('request');
let FilmIs = 0;

request(process.argv[2], function (err, response, body) {
  if (err == null) {
	  const res = JSON.parse(body);
	  const results = res.results;
	  for (let i = 0; i < results.length; i++) {
		  if (characters[j].search('18') > 0) {
			  FilmIs++;
		  }
	  }
  }
  console.log(FilmIs);
});