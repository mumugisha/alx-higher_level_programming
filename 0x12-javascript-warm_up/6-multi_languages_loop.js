#!/usr/bin/node

const myMsg = 'C is fun\nPython is cool\nJavaScript is amazing';

const myMsgLines = myMsg.split('\n');

myMsgLines.forEach((component) => console.log(component));
