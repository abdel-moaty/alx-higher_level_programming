#!/usr/bin/node
require('request')(process.argv[2]).pipe(require('fs').createWriteStream(process.argv[3]));
