const express = require("express");
const router = express.Router();
const conn = require('../../Database/connection');
const registrationControllers = require("../controllers/registration");


router.post('/register' , (req , res)=>{
    
    console.log(req.body);
    let { userid , name , email , pass } = req.body;
    // console.log(req.body);
    registrationControllers.putInformation(userid , name , email , pass );

});


module.exports = router;