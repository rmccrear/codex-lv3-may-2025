# Week 1: Building a Mad Libs Web Application with Express and Node.js

## Overview
Today you'll learn how to build a full-stack web application using Node.js and Express. You'll create an interactive Mad Libs game where users fill out a form and see a funny story generated from their inputs.

## Learning Objectives
By the end of this activity, you'll be able to:
- Set up a Node.js project with Express
- Create HTML forms to collect user input
- Process form data on a server
- Use template literals to generate dynamic content
- Serve static files with Express
- Style web pages using Bootstrap CSS framework

## Today's Topics

### 1. What is Node.js?
Node.js is a JavaScript runtime that lets you run JavaScript outside the browser:
- Build servers and web applications
- Process data and files
- Connect to databases
- Create command-line tools

### 2. What is Express?
Express is a web framework for Node.js that makes it easy to:
- Create web servers
- Define routes (URL paths)
- Handle HTTP requests and responses
- Serve HTML files and static content

### 3. How Forms Work
HTML forms collect user input and send it to a server:
- Forms use `<input>` elements for different data types
- The `name` attribute identifies each input
- Form data is sent via GET or POST requests
- Servers process the data and send back a response

---

## Part 1: Demo - Basic Express Server

### Creating Your First Express Server

Here's the basic structure of an Express server:

```javascript
// server.js
const express = require('express');
const app = express();
const PORT = 3000;

// Serve static files from the 'public' folder
app.use(express.static('public'));

// Route to handle the home page
app.get('/', (req, res) => {
  // TODO: Send a response to the client
});

// Start the server
app.listen(PORT, () => {
  // TODO: Log a message when server starts
});
```

### Key Concepts:
- **require()**: Import packages in Node.js
- **app.get()**: Define a route that responds to GET requests
- **req**: The request object (contains user input)
- **res**: The response object (sends data back to user)
- **app.listen()**: Start the server on a specific port

---

## Part 2: Demo - Processing Form Data

### Basic Form Structure

```html
<!-- public/mad-libs-form.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Mad Libs Game</title>
</head>
<body>
  <h1>Mad Libs Story Generator</h1>
  <form action="/story" method="GET">
    <!-- TODO: Add input fields for noun, verb, adjective -->
    <!-- Remember to add name attributes! -->
    
    <button type="submit">Create Story!</button>
  </form>
</body>
</html>
```

### Processing the Form Data

```javascript
// server.js
app.get('/story', (req, res) => {
  // TODO: Get form data from req.query
  // Example: const noun = req.query.noun;
  
  // TODO: Create story with template literals
  // Use backticks ` and ${variable} syntax
  
  // TODO: Send HTML response back to user
});
```

### Key Concepts:
- **req.query**: Access form data sent via GET request
- **Template literals**: Use backticks (\`) and `${variable}` for string interpolation
- **required attribute**: Makes form fields mandatory

---

## Part 3: Hands-On Activities

### Activity 1: Project Setup (20 minutes)

**Goals:**
- Create a new Node.js project
- Install Express
- Set up basic file structure
- Start your first server

**Steps:**

1. **Create your project folder:**
   ```bash
   mkdir mad-libs-project
   cd mad-libs-project
   ```

2. **Initialize npm:**
   ```bash
   npm init -y
   ```

3. **Install Express:**
   ```bash
   npm install express
   ```

4. **Install nodemon (development tool):**
   ```bash
   npm install --save-dev nodemon
   ```

5. **Update `package.json` scripts:**
   Open `package.json` and modify the scripts section:
   ```json
   "scripts": {
     "start": "node server.js",
     "dev": "npx nodemon server.js"
   }
   ```

6. **Create files:**
   ```bash
   touch server.js
   mkdir public
   touch public/mad-libs-form.html
   ```

7. **Create a basic server in `server.js`:**
   - Import express
   - Set up static file serving
   - Create a route for `/`
   - Start the server listening on port 3000
   - See Part 1 demo above for structure

8. **Start your server:**
   ```bash
   npm run dev
   ```

9. **Test it:** Open `http://localhost:3000` in your browser

✅ **Checkpoint**: You should see "Mad Libs Server is Running!" in your browser

---

### Activity 2: Create Your First Form (30 minutes)

**Goals:**
- Build an HTML form
- Collect at least 5 different word types
- Style the form with basic CSS
- Test form submission

**Steps:**

1. **Create your form in `public/mad-libs-form.html`:**
   - Add HTML boilerplate (DOCTYPE, html, head, body tags)
   - Add a heading and instructions
   - Create a `<form>` with `action="/story"` and `method="GET"`
   - Add at least 5 input fields:
     - noun (text input with `name="noun"`)
     - verb (text input with `name="verb"`)
     - adjective (text input with `name="adjective"`)
     - place (text input with `name="place"`)
     - number (number input with `name="number"`)
   - Add labels for each input
   - Add a submit button
   - Add basic CSS styling in a `<style>` tag:
     - Center the form
     - Style the inputs (padding, margin)
     - Style the button (colors, padding)

2. **Update `server.js` to serve the form:**
   - Change the `/` route to redirect to `/mad-libs-form.html`
   - Use `res.redirect('/mad-libs-form.html')`

3. **Test your form:**
   - Go to `http://localhost:3000`
   - You should see your form
   - Try filling it out and clicking submit
   - You'll get an error (we haven't created the `/story` route yet!)

✅ **Checkpoint**: Form displays with all fields and styling

---

### Activity 3: Process Form Data (30 minutes)

**Goals:**
- Create a `/story` route
- Access form data from `req.query`
- Generate a Mad Libs story
- Send HTML response

**Steps:**

1. **Add the `/story` route to `server.js`:**
   - Create a new `app.get('/story', ...)` route
   - Extract form data from `req.query` (noun, verb, adjective, place, number)
   - Create a story using template literals with `${variable}` syntax
   - Build an HTML response string that includes:
     - HTML boilerplate
     - A heading for "Your Story"
     - The story in a paragraph
     - A button to create another story (`onclick="window.location.href='/'")
     - Some basic CSS styling
   - Send the HTML with `res.send(html)`

2. **Test the complete flow:**
   - Go to `http://localhost:3000`
   - Fill out all form fields
   - Click "Create My Story!"
   - You should see your generated story!

3. **Debug with console.log:**
   - Add `console.log('Form data:', req.query)` at the start of your route
   - Check the terminal to see what data you're receiving

✅ **Checkpoint**: Form submits successfully and displays a complete story

---

### Activity 4: Add Bootstrap Styling (25 minutes)

**Goals:**
- Add Bootstrap CSS framework
- Improve the visual design
- Make the form responsive
- Add professional styling

**Steps:**

1. **Update `mad-libs-form.html` with Bootstrap:**
   - Add Bootstrap CDN link in the `<head>`:
     ```html
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
     ```
   - Replace your custom CSS with Bootstrap classes:
     - Use `class="container mt-5"` for the main wrapper
     - Use `class="card shadow"` for the card container
     - Use `class="form-control"` for all inputs
     - Use `class="form-label"` for all labels
     - Use `class="btn btn-primary btn-lg"` for the button
     - Wrap each input in `<div class="mb-3">` for spacing
   - Refer to [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/forms/overview/) for examples

2. **Update the story page with Bootstrap:**
   - Add the same Bootstrap CDN link in your HTML response
   - Use Bootstrap classes:
     - `class="container mt-5"` for main container
     - `class="card shadow"` for the story card
     - `class="alert alert-info"` for the story text area
     - `class="btn btn-primary"` for the button
   - Keep your story template literal inside the HTML

✅ **Checkpoint**: Both pages should look professional with Bootstrap styling

---

### Activity 5: Create Your Own Story Template (20 minutes)

**Goals:**
- Write a unique Mad Libs story
- Add more word types
- Personalize your application
- Test with creative inputs

**Steps:**

1. **Plan your story:**
   - Choose a theme (adventure, school, cooking, etc.)
   - Decide what word types you need (8-10 different inputs)
   - Write the story template on paper first

2. **Update your form** with the new word types:
   - Add 3-5 more input fields (aim for 8-10 total)
   - Possible word types: pluralNoun, color, emotion, adverb, celebrity, food, animal
   - Each input needs a unique `name` attribute
   - Use Bootstrap classes for styling consistency

3. **Update your `/story` route** with your custom template:
   - Get all the new form data from `req.query`
   - Write a creative story template using your theme
   - Use template literals to insert all the variables
   - Make it funny! The more unexpected word combinations, the better

4. **Test with silly inputs** - The funnier, the better!

✅ **Checkpoint**: Your custom story generates correctly with all inputs

---

## Key Express Concepts Reference

### Setting Up Express
```javascript
const express = require('express');
const app = express();
const PORT = 3000;
```

### Serving Static Files
```javascript
app.use(express.static('public'));
// Now files in 'public/' folder are accessible
```

### Creating Routes
```javascript
// GET route
app.get('/path', (req, res) => {
  res.send('Response');
});

// Access query parameters
app.get('/story', (req, res) => {
  const data = req.query.paramName;
});
```

### Starting the Server
```javascript
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
```

### Template Literals
```javascript
const name = "Alice";
const age = 25;
const message = `Hello, my name is ${name} and I am ${age} years old.`;
```

---

## Troubleshooting

### Issue: Cannot GET /
**Solution**: Make sure `app.use(express.static('public'))` is in your server.js
```javascript
app.use(express.static('public'));
```

### Issue: Port 3000 already in use
**Solution**: Either stop the other server or change the port
```javascript
const PORT = 3001; // Use a different port
```

### Issue: `req.query` is undefined or empty
**Solution**: 
- Check form `method="GET"` attribute
- Verify input `name` attributes match
- Check form `action="/story"` points to correct route

### Issue: Template literal not working
**Solution**: 
- Use backticks (\`) not quotes (' or ")
- Use `${variable}` not `{variable}` or `$(variable)`

### Issue: Changes not showing
**Solution**: 
- Hard refresh browser (Cmd+Shift+R or Ctrl+Shift+R)
- Check if nodemon is running (should auto-restart)
- Make sure you saved all files

### Issue: Form doesn't submit
**Solution**: 
- Check all inputs have `name` attributes
- Verify form has `action` and `method` attributes
- Look for JavaScript errors in browser console (F12)

---

## npm Commands Reference

```bash
# Initialize a new project
npm init -y

# Install a package
npm install package-name

# Install dev dependency
npm install --save-dev package-name

# Run a script from package.json
npm run script-name

# Start server (using your custom script)
npm run dev
```

---

## Success Criteria

By the end of today, you should have:
- ✅ A working Node.js + Express server
- ✅ An HTML form that collects user input
- ✅ A `/story` route that processes form data
- ✅ Template literals generating dynamic stories
- ✅ Bootstrap styling on both pages
- ✅ Your own custom story template
- ✅ Understanding of GET requests and query parameters

---

## Homework / Before Next Class

1. **Complete Levels 1-5** of the Mad Libs project guide
2. **Create at least 2 different story templates** (see [Activity Guide](./mad-libs-mini-project-activity-guide.md) for examples)
3. **Add more form inputs** - aim for 8-10 different word types
4. **Experiment with Bootstrap components**:
   - Try different button styles
   - Add alert boxes or cards
   - Explore color themes
5. **Start thinking about** how you could save stories (we'll cover this in challenge levels)

**Optional Challenges:**
- Add form validation (check for empty inputs)
- Create a "print" button for stories
- Add images or emojis to your stories
- Make multiple story templates users can choose from

---

## Next Steps Preview

In the next session, you'll:
- Learn about multiple story templates
- Implement story selection
- Work on challenge features (if ready)
- Complete your Mad Libs project
- Deploy your app (if time permits)

---

## Resources

**Documentation:**
- [Express.js Official Docs](https://expressjs.com/)
- [Node.js Official Docs](https://nodejs.org/)
- [Bootstrap 5 Docs](https://getbootstrap.com/)
- [MDN HTML Forms](https://developer.mozilla.org/en-US/docs/Learn/Forms)

**Helpful Tools:**
- [Nodemon](https://www.npmjs.com/package/nodemon) - Auto-restart server
- [Postman](https://www.postman.com/) - Test API endpoints
- Chrome DevTools - Debug in browser

**Mad Libs Resources:**
- [Activity Guide](./mad-libs-mini-project-activity-guide.md) - Full project guide
- [Mad Libs Levels](../mad-libs-levels/) - Step-by-step instructions

---

**Great work today!** You've learned the fundamentals of server-side JavaScript and built your first full-stack web application. Keep building! 🚀

---

#### ✍️ Attribution

This guide was developed with assistance from **Anthropic's Claude (Claude 3.5 Sonnet)** to ensure clarity, accuracy, and consistency in the explanations and examples.

