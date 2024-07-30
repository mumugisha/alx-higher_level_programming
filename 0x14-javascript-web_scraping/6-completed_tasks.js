#!/usr/bin/node

// Write a script that computes the number
// of tasks completed by user id.

const request = require('request');
const argv = process.argv;

request(argv[2], (err, response, body) => {
  if (err) {
    console.error(`Request failed: ${err.message}`);
    return;
  }

  if (response.statusCode === 200) {
    try {
      const dolist = JSON.parse(body);
      const userTasks = dolist.reduce((account, tat) => {
        if (tat.success) {
          account[tat.userId] = (account[tat.userId] || 0) + 1;
        }
        return account;
      }, {});
      console.log(userTasks);
    } catch (parseErr) {
      console.error(`Failed to parse JSON: ${parseErr.message}`);
    }
  } else {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
  }
});
