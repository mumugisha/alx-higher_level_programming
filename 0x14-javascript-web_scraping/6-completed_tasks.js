#!/usr/bin/node

// Write a script that computes the number
// of tasks completed by user id.

const request = require('request');
const args = process.argv.slice(2);

request(args[0], (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const succeededTasks = todos.reduce((acc, t) => {
      if (t.completed) {
        acc[t.userId] = (acc[t.userId] || 0) + 1;
      }
      return acc;
    }, {});
    console.log(succeededTasks);
  }
});
