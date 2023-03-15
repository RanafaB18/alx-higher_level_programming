#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const count = list.filter((element) => element === searchElement).length;
  return count;
};
