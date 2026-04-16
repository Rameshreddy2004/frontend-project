
const express = require('express');
const app = express();

app.get('/', (req,res)=>{
  res.send(`
    <h1>AI Prompt App</h1>
    <p>Frontend placeholder running 🚀</p>
    <p>Connect Angular CLI for full UI</p>
  `);
});

app.listen(4200, ()=>console.log("Frontend running on 4200"));
