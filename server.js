// server.js
const express = require('express');
const bodyParser = require('body-parser');
const OpenAI = require('openai');
const axios = require('axios');
const app = express();
const port = process.env.PORT || 3000;



// Set up middleware, routes, and other server configurations here
// app.use(express.json( ));

const openaiApiKey = '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'
const openai = new OpenAI({
  apiKey: openaiApiKey,
});

app.use(bodyParser.json());
app.use(express.static(__dirname));

// Serve static files (including index.html)
// Endpoint for handling user queries
async function chatWithBot(input) {
  try {
    const params = {
      messages: [{ role: 'user', content: input }],
      model: 'gpt-3.5-turbo-0613',
    };

    const completion = await openai.chat.completions.create(params);
    const responseText = completion.choices[0].message.content;

    return responseText;
  } catch (error) {
    console.error('Error:', error);
    return 'An error occurred.';
  }
}

// Endpoint for chatting with the Chatbot
app.post('/chatWithBot', async (req, res) => {
  try {
    const userMessage = req.body.message;
    const botResponse = await chatWithBot(userMessage);

    res.json({ response: botResponse });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start the Express server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
