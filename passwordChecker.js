
const fs = require('fs');
const crypto = require('crypto');
const readline = require('readline');

function encodePass(password) {
const passHash = crypto.createHash('sha256').update(password).digest('hex');
return passHash;
}

let accounts = JSON.parse(fs.readFileSync('accounts.json', 'utf8'));

async function signInProcess() {

  let invalid = true;
  while (invalid) {
      let username = document.getElementById('username');
      let password = document.getElementById('password');
      let encryptedPass = encodePass(password);
      if (accounts[username] === encryptedPass) {
          invalid = false;
          location.replace("/other.html")
      } else {
          console.log("Please try again");
      }
  }
}
async function createAccount(){
  let username = document.getElementById(username);
  let password = document.getElementById(password);
  let encryptedPass = encodePass(password);

  //add account data to dictionary from json file
  accounts[username] = encryptedPass;
  console.log(accounts);

  //store account data in json file
  fs.writeFileSync('accounts.json', JSON.stringify(accounts, null, 4));
}
async function test(){
location.replace("./other.html")
}
