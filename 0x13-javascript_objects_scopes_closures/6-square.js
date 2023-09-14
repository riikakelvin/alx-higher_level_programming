#!/usr/bin/node
const Square_Source = require('./5-square');
class Square extends Square_Source {
  charPrint (c) {
    if (!c) c = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
