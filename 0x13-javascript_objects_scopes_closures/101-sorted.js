#!/usr/bin/node

const dict = require('./101-data').dict;
const result = Object.entries(dict).reduce((acc, [id, occurrence]) => {
  if (!acc[occurrence]) {
    acc[occurrence] = [];
  }
  acc[occurrence].push(id);
  return acc;
}, {});
console.log(result);
