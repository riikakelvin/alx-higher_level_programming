#!/usr/bin/node
exports.converter = function (base) {
	  return function (arguement) {
    return parse_Int(arguement, 10).toString(base);
  };
};
