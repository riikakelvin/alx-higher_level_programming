#!/usr/bin/node
exports.converter = function (base) {
	  return function (arguement) {
    return parseInt(arguement, 10).toString(base);
  };
};
