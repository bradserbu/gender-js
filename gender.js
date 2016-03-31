#!/usr/bin/env node

// ** Libraries
const gender = require('./build/Release/gender');

function getGender(name) {
    const result = gender.getGender(name);
    return String.fromCharCode(result);
}

module.exports = getGender;