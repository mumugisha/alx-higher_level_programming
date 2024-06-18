#!/usr/bin/node
/**
 * The script that concats 2 files.
 * The first argument is the file path of the first source file
 * The second argument is the file path of the second source file
 * The third argument is the file path of the destination
 */
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

if (!fileA || !fileB || !fileC) {
    console.error('Please provide valid paths for both source files and the destination file.');
    process.exit(1);
}

if (
    !fs.existsSync(fileA) || !fs.statSync(fileA).isFile() ||
    !fs.existsSync(fileB) || !fs.statSync(fileB).isFile()
) {
    console.error('One or both of the source files do not exist or are not valid files.');
    process.exit(1);
}

try {
    const fileAdata = fs.readFileSync(fileA, 'utf8');
    const fileBdata = fs.readFileSync(fileB, 'utf8');
    fs.writeFileSync(fileC, fileAdata + fileBdata, 'utf8');
    console.log(`Successfully concatenated ${fileA} and ${fileB} into ${fileC}`);
} catch (error) {
    console.error(`Error reading or writing files: ${error.message}`);
    process.exit(1);
}
