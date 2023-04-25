#!/usr/bin/node 

//script to write to a file

const fs = require('fs');
const filepath = process.argv[2];
const content = process.argv[3] + '\n'
fs.writeFile(filePath, content, err => {
  if (err) {
    console.error(err);
  }
});
