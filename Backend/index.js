const app = require("express")();
const server = require("http").createServer(app);
let bodyParser = require('body-parser');
const cors = require('cors');

server.listen(5008, () => {
    console.log("Server is listening at port 5005...");
  });
  
  app.use(bodyParser.json());
//Routes

let registrationRouter = require('./admin/routes/registration');

app.use(cors());
app.use('/registration',registrationRouter);

// app.post('/registration' , (req , res )=>{
//     console.log("aagya");
//     res.send(200).json({name : "Ritik"});
// });
