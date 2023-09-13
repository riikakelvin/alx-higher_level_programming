#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const kE in dict) {
  if (newDict[dict[kE]] === undefined) {
    newDict[dict[kE]] = [];
  }
  newDict[dict[kE]].push(kE);
}
console.log(newDict);
