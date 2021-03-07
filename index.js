const express = require("express");
const app = express();
const port = 3000;
const path = require("path");
const router = express.Router();
const body = require("body-parser");
const fs = require("fs");

app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  //res.render('index')
  es.sendFile(path.join(__dirname + "/public/index.html"));
});

app.get("/waitingList", (req, res) => {
  //res.render('waitingList')
  res.sendFile(path.join(__dirname + "/public/waitingList.html"));
});

app.use("/", router);
app.use(
  express.urlencoded({
    extended: true,
  })
);

app.post("/waitingList", (req, res) => {
  let name = req.body.name;
  let email = req.body.email;

  const user = {
    name: name,
    email: email,
  };

  const data = user.name + ", " + user.email + ";\n";

  fs.writeFile("users.txt", data, { flag: "a+" }, (err) => {
    if (err) {
      throw err;
    }
    console.log("Data is saved.");
  });
  res.sendFile(path.join(__dirname + "/public/page.html"));
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
