#!/usr/bin/node
const dict = require('./101-data').dict;
const new_Dict = {};
for (const ke in dict) {
  if (newDict[dict[ke]] === undefined) {
    newDict[dict[ke]] = [];
  }
  newDict[dict[ke]].push(ke);
}
console.log(newDict);
