const mongoose = require("mongoose");
const dbUrl = process.env.DB_URL;

// Set up default mongoose connection
const mongoDBURL = dbUrl; // Replace with your MongoDB URL
mongoose.connect(mongoDBURL, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Check if the connection is successful
const db = mongoose.connection;
db.on("error", console.error.bind(console, "MongoDB connection error:"));
db.once("open", () => {
  console.log("Connected to MongoDB successfully");
});
