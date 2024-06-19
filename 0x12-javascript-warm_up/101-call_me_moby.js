#!/usr/bin/node

exports.callMeMoby = function(x, theFunction) {
  for (let b = 0; b < x; b++) {
    theFunction();
  }
};

