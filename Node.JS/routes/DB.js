

var mysql = require('mysql');

var con = mysql.createConnection({
  host: "db-6r1d0.pub-cdb.ntruss.com",
  user: "playdata",
  password: "playdata1!",
  database: "frezo"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});


module.exports = con;  // 다른곳 에서 con 을 땡겨 오겠다.

