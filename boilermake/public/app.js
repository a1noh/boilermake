const express = require("express");
const app = express();
app.get("/", function(req, res){
    res.sendFile(__dirname + "/index.html");
})

app.listen(3000, function () {
    console.log('listening at port 3000');
})

app.post("/first", function(req,res){
  res.send("hello")

})


