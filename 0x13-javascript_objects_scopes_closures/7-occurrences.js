#!/usr/bin/node
/**
 * The function that returns the number of occurrences in a list
 */
exports.nbOccurences = function (list, searchElement) {
    return list.filter(component => searchElement === component).length;
};
