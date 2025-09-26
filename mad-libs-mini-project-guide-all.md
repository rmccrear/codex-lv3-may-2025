# 🎯 Mad Libs Mini-Project Guide

This guide provides step-by-step instructions for building a Mad Libs web application using Node.js, Express.js, and modern web development concepts.

**Structure:**
- Each level builds on the previous one
- Clear instructions and checkpoints
- Code examples and hints provided
- Progressive complexity from basic to advanced

---

<!-- LEVEL_START -->

# Level 1: Project Setup & Planning

**Goal:** Set up your development environment and understand the project requirements.

**User Story:** As a developer, I want to create a new project folder with all necessary files so that I can start building my Mad Libs application.

---

## What You'll Do
Create a new project folder and set up all the necessary files to get started.

## Instructions
- Make a new folder for your project named `mad-libs-project`
- Navigate to the project folder and run `npm init -y` to create package.json
- Inside, create these files:
  - `server.js`
  - `public/mad-libs-form.html`
  - `README.md`


## ✅ Check
Open your project folder in VS Code and verify you can see all files:
- `server.js`
- `package.json`
- `public/mad-libs-form.html`
- `README.md`

If any files are missing, create them before moving to Level 2.

---

<!-- LEVEL_START -->

# Level 2: Basic Express Server Setup

**User Story:** As a developer, I want to create a basic Express server so that I can handle web requests for my Mad Libs application.

## What You'll Do
Create a basic Express server that listens on port 3000.

## Instructions
- Install Express using `npm install express`
- Install nodemon using `npm install nodemon --save-dev`
- Create basic `server.js` file
- Set up server to listen on port 3000
- Add a simple route that responds with "Hello World"

## 💡 Code Hints
Need help with Express setup? Check out these snippets:
- **Basic Express server:** See [Week 1 Notes](../notes/week1-notes.md#day-1) for server setup examples
- **Route handling:** Use `app.get()` to create routes

Show Me: the basic Express server structure

```javascript
const express = require('express');
const app = express();
const PORT = 3000;

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
```

Show Me: a simple route example

```javascript
app.get('/', (req, res) => {
    res.send('Hello World!');
});
```

## ✅ Check
1. Run `npm install` to install dependencies
2. Run `npx nodemon server.js` to start your server
3. Open your browser to `http://localhost:3000`
4. You should see "Hello World" displayed
5. If you see errors, check your server.js file and dependencies

---

<!-- LEVEL_START -->

# Level 3: Static File Serving

**User Story:** As a developer, I want to serve HTML files from my server so that users can access my Mad Libs form in a web browser.

## What You'll Do
Set up static file serving to serve HTML files from the public directory.

## Instructions
- Create `public/mad-libs-form.html` with basic HTML structure
- Add static middleware to your server
- Test serving HTML files

## 💡 Code Hints
Need help with static files? Check out these snippets:
- **Static middleware:** Use `app.use(express.static('public'))`
- **HTML structure:** Include `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`

Show Me: how to add static middleware

```javascript
app.use(express.static('public'));
```

Show Me: basic HTML structure

```html
<!DOCTYPE html>
<html>
<head>
    <title>Mad Libs Form</title>
</head>
<body>
    <h1>Welcome to Mad Libs!</h1>
</body>
</html>
```

## ✅ Check
1. Create `public/mad-libs-form.html` with basic HTML
2. Add static middleware to your server
3. Restart your server
4. Navigate to `http://localhost:3000/mad-libs-form.html`
5. You should see your HTML page instead of "Hello World"

---

<!-- LEVEL_START -->

# Level 4: HTML Form Creation

**User Story:** As a user, I want to fill out a form with my words so that I can create a personalized Mad Libs story.

## What You'll Do
Create an HTML form with all the required fields for the Mad Libs story.

## Instructions
- Add HTML form with text inputs for:
  - Name
  - Adjective 1
  - Noun 1
  - Verb
  - Adjective 2
  - Noun 2
- Set form method to "GET"
- Set form action to "/create-mad-libs"

## 💡 Code Hints
Need help with forms? Check out these snippets:
- **Form structure:** Use `<form method="GET" action="/create-mad-libs">`
- **Input fields:** Use `<input type="text" name="fieldName">`
- **Labels:** Use `<label>` elements for better accessibility

Show Me: form structure with inputs

```html
<form method="GET" action="/create-mad-libs">
    <label for="name">Name:</label>
    <input type="text" name="name" id="name" required>
    
    <label for="adjective1">Adjective:</label>
    <input type="text" name="adjective1" id="adjective1" required>
    
    <button type="submit">Create Mad Libs!</button>
</form>
```

Show Me: input field with proper attributes

```html
<input type="text" name="noun1" placeholder="Enter a noun" required>
```

## ✅ Check
1. Open your webpage in a browser
2. You should see a form with 6 input fields
3. Each field should have a clear label
4. The form should have a submit button
5. If the form doesn't appear, check your HTML structure

---

<!-- LEVEL_START -->

# Level 5: Bootstrap Styling

**User Story:** As a user, I want the form to look attractive and easy to use so that I enjoy filling it out.

## What You'll Do
Add Bootstrap CSS to style your form and make it look professional.

## Instructions
- Link Bootstrap CSS via CDN in your HTML head
- Add Bootstrap classes to your form elements
- Style the form inputs and button

## 💡 Code Hints
Need help with Bootstrap? Check out these snippets:
- **Bootstrap CDN:** Use `https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css`
- **Form styling:** Use `form-control` class for inputs
- **Button styling:** Use `btn btn-primary` classes

Show Me: Bootstrap CDN link in HTML head

```html
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Mad Libs Form</title>
</head>
```

Show Me: Bootstrap form styling

```html
<div class="container mt-5">
    <form method="GET" action="/create-mad-libs" class="row g-3">
        <div class="col-md-6">
            <label class="form-label">Name:</label>
            <input type="text" class="form-control" name="name">
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</div>
```

## ✅ Check
1. Open your webpage in a browser
2. Your form should look styled and professional
3. Inputs should have clean borders and padding
4. Button should have Bootstrap button styling
5. If styling doesn't appear, check your Bootstrap CDN link

---

<!-- LEVEL_START -->

# Level 6: Server Route for Form Processing

**User Story:** As a developer, I want to create a server route so that I can receive and process the form data when users submit their Mad Libs.

## What You'll Do
Create a server route to handle form submission and process the form data.

## Instructions
- Create `/create-mad-libs` route using `app.get()`
- Access form data using `req.query`
- Log the form data to console for testing

## 💡 Code Hints
Need help with routes? Check out these snippets:
- **Route creation:** Use `app.get('/create-mad-libs', (req, res) => {})`
- **Query parameters:** Use `req.query.fieldName` to access form data, where `fieldName` is the "name" of the input in the form. For example for "properNoun1", you would have `req.query.properNoun1`.
- **Console logging:** Use `console.log()` to debug form data

Show Me: basic route structure

```javascript
app.get('/create-mad-libs', (req, res) => {
    // Access form data here
    console.log('Form submitted!');
    res.send('Form received!');
});
```

Show Me: accessing form data

```javascript
app.get('/create-mad-libs', (req, res) => {
    const name = req.query.name;
    const adjective = req.query.adjective1;
    
    console.log('Name:', name);
    console.log('Adjective:', adjective);
    
    res.send('Data received!');
});
```

## ✅ Check
1. Fill out your form and submit it
2. Check your server console for logged form data
3. You should see all form fields logged with their values
4. If you don't see the data, check your route and form action

---

<!-- LEVEL_START -->

# Level 7: Template Literals and Story Generation

**User Story:** As a user, I want to see my personalized Mad Libs story with my words inserted so that I can laugh at the funny result.

## What You'll Do
Generate the Mad Libs story using JavaScript template literals and form data.

## Instructions
- Create the story template using template literals
- Insert form data into the story template
- Send the complete story as HTML response

## 💡 Code Hints
Need help with template literals? Check out these snippets:
- **Template literals:** Use backticks and `${variable}` syntax
- **Story template:** Create a complete story with placeholders
- **HTML response:** Use `res.send()` to send HTML

Show Me: template literal syntax

```javascript
const name = "Alice";
const adjective = "silly";
const story = `Once upon a time, ${name} was feeling very ${adjective}.`;
```

Show Me: story template structure

```javascript
const storyTemplate = `
    <h1>Your Mad Libs Story</h1>
    <p>Once upon a time, ${name} went to the ${noun1} and found a ${adjective1} ${noun2}.</p>
`;
res.send(storyTemplate);
```

## 🚀 Pro Tip
**Practice with dummy variables first!** Before using the real form data from `req.query`, create your story template with hardcoded dummy values (like `name = "Alice"`, `adjective = "silly"`). This helps you:
- Test your template literal syntax
- Verify your story structure works
- Debug any formatting issues
- Then replace the dummy values with the real `req.query` variables

## ✅ Check
1. Fill out your form and submit it
2. You should see the completed Mad Libs story
3. The story should use your form data correctly
4. If the story doesn't appear, check your template literal syntax

---

<!-- LEVEL_START -->

# Level 8: Story Display Styling

**User Story:** As a user, I want to read my Mad Libs story in a beautiful, easy-to-read format so that I can fully enjoy the experience.

## What You'll Do
Style the story display with CSS and improve the user experience. Add CSS styling directly in your server route response.

## Instructions
- Add CSS styling to the story display HTML
- Include Bootstrap CSS link in the HTML head
- Create a styled layout for the story
- Add navigation links back to the form
- **Important:** This CSS is added inside your server route response, not in a static file

## 💡 Code Hints
Need help with styling? Check out these snippets:
- **CSS in server route:** Add complete HTML with CSS link in your `res.send()`
- **Bootstrap CDN:** Include Bootstrap CSS link in the HTML head
- **Navigation:** Add links with `href="/mad-libs-form.html"`

Show Me: complete HTML with CSS in server route

```javascript
const storyHTML = `
<!DOCTYPE html>
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Your Mad Libs Story</title>
</head>
<body>
    <div class="container mt-5">
        <div class="card">
            <div class="card-body">
                <h1 class="card-title">Your Mad Libs Story</h1>
                <p class="card-text">${storyContent}</p>
                <a href="/mad-libs-form.html" class="btn btn-primary">Create Another Story</a>
            </div>
        </div>
    </div>
</body>
</html>`;

res.send(storyHTML);
```

Show Me: basic story structure

```html
<div class="container mt-5">
    <div class="card">
        <div class="card-body">
            <h1>Your Story</h1>
            <p>Story content goes here...</p>
            <a href="/mad-libs-form.html">Create Another Story</a>
        </div>
    </div>
</div>
```

## ✅ Check
1. Submit your form and view the story
2. The story should be displayed with Bootstrap styling
3. You should see a navigation link back to the form
4. The page should look professional and responsive
5. **Important:** The CSS is loaded from the CDN link in your server response

## 🚨 Important Note
**Server Route vs Static Files:** Unlike your form HTML file (which is static), the story display HTML is generated dynamically in your server route. This means you include the CSS link directly in the HTML string that you send with `res.send()`.

---

<!-- LEVEL_START -->

# Level 9: Code Organization and Best Practices

**User Story:** As a developer, I want to organize my code with comments and good practices so that my Mad Libs application is easy to read and maintain.

## What You'll Do
Organize your code for maintainability and follow best practices.

## Instructions
- Add comments to explain code sections
- Use meaningful variable names
- Organize routes logically
- Test all functionality

## 💡 Code Hints
Need help with organization? Check out these snippets:
- **Code comments:** Use `//` for single-line comments
- **Variable naming:** Use descriptive names like `storyContent`
- **Route organization:** Group related routes together

Show Me: code comments

```javascript
// Server setup
const express = require('express');
const app = express();

// Static file serving
app.use(express.static('public'));

// Routes
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/mad-libs-form.html');
});
```

Show Me: descriptive variable names

```javascript
const storyTemplate = `Your story here...`;
const completedStory = storyTemplate.replace('${name}', userName);
const storyResponse = `<div class="card">${completedStory}</div>`;
```

## ✅ Check
1. Your code should be well-commented
2. Variable names should be descriptive
3. Routes should be organized logically
4. All functionality should work correctly
5. Code should be easy to read and understand

---

<!-- LEVEL_START -->

# Level 10: Data Storage in Memory ⚡ CHALLENGE LEVEL

> **Note:** Levels 10 and beyond are challenge levels that extend the basic Mad Libs functionality. These are optional but recommended for a more complete learning experience.

**User Story:** As a user, I want to save my completed Mad Libs stories so that I can read them again later and share them with friends.

## What You'll Do
Store completed stories in an in-memory array for later access.

## Instructions
- Create a global array to store stories
- Push completed stories to the array
- Add a link to view all stories

## 💡 Code Hints
Need help with arrays? Check out these snippets:
- **Global array:** Use `let stories = [];` outside route handlers
- **Array push:** Use `stories.push(storyContent);`
- **Array length:** Use `stories.length` to check array size

## ✅ Check
1. Create and submit multiple stories
2. Check that stories are being stored
3. Verify the array grows with each submission
4. If stories aren't stored, check your array operations

---

<!-- LEVEL_START -->

# Level 11: Random Story Access ⚡ CHALLENGE LEVEL

**User Story:** As a user, I want to discover random Mad Libs stories from my collection so that I can be surprised by stories I've forgotten about.

## What You'll Do
Create a route to display a random story from the stored stories.

## Instructions
- Create `/random` route
- Use `Math.random()` to select a random story
- Display the random story in a styled format

## 💡 Code Hints
Need help with random selection? Check out these snippets:
- **Random number:** Use `Math.floor(Math.random() * stories.length)`
- **Array access:** Use `stories[randomIndex]`
- **Empty array check:** Handle case when no stories exist

## ✅ Check
1. Create several stories first
2. Navigate to `/random` route
3. You should see a random story displayed
4. Refresh the page to see different random stories
5. If no random story appears, check your random selection logic

---

<!-- LEVEL_START -->

# Level 12: Individual Story Access ⚡ CHALLENGE LEVEL

**User Story:** As a user, I want to find and read a specific Mad Libs story by its number so that I can revisit my favorite stories.

## What You'll Do
Create a route to access individual stories by number using query parameters.

## Instructions
- Create `/story-no` route
- Parse query parameter `number`
- Display the specific story requested

## 💡 Code Hints
Need help with query parameters? Check out these snippets:
- **Parameter parsing:** Use `parseInt(req.query.number)`
- **Array indexing:** Convert to 0-based index with `number - 1`
- **Error handling:** Handle invalid numbers gracefully

## ✅ Check
1. Create several stories first
2. Navigate to `/story-no?number=1`
3. You should see the first story
4. Try different numbers to access different stories
5. If stories don't appear, check your parameter parsing

---

<!-- LEVEL_START -->

# Level 13: Navigation Between Stories ⚡ CHALLENGE LEVEL

**User Story:** As a user, I want to easily move between different Mad Libs stories so that I can browse through my collection without getting lost.

## What You'll Do
Add navigation links to move between stories and improve user experience.

## Instructions
- Add "Next Story" link when available
- Add navigation links to random story and main form
- Handle boundary conditions (no next story at end)

## 💡 Code Hints
Need help with navigation? Check out these snippets:
- **Conditional links:** Use `if (hasNextStory)` to show/hide links
- **Link generation:** Use template literals for dynamic URLs
- **Boundary checking:** Check `storyNumber < stories.length`

## ✅ Check
1. Navigate to individual stories
2. You should see appropriate navigation links
3. "Next Story" should only appear when there is a next story
4. All navigation should work correctly
5. If navigation doesn't work, check your conditional logic

---

<!-- LEVEL_START -->

# Level 14: Error Handling and Validation ⚡ CHALLENGE LEVEL

**User Story:** As a user, I want to get clear, helpful messages when something goes wrong so that I know how to fix the problem.

## What You'll Do
Add basic validation and error handling to improve the user experience.

## Instructions
- Add validation for required form fields
- Handle edge cases (empty stories, invalid numbers)
- Display user-friendly error messages

## 💡 Code Hints
Need help with validation? Check out these snippets:
- **Field validation:** Use `if (!fieldName)` to check for empty fields
- **Error messages:** Use `res.status(400).send()` for error responses
- **User feedback:** Display clear error messages

## ✅ Check
1. Submit form with empty fields
2. You should see validation error messages
3. Try accessing invalid story numbers
4. Error messages should be user-friendly
5. If validation doesn't work, check your conditional statements

---

<!-- LEVEL_START -->

# Level 15: Final Testing and Polish

**User Story:** As a developer, I want to thoroughly test my application so that I can ensure everything works perfectly before sharing it.

## What You'll Do
Perform comprehensive testing and add final polish to your application.

## Instructions
- Test all routes and functionality
- Test with different inputs and edge cases
- Add final styling improvements
- Ensure everything works smoothly

## 💡 Code Hints
Need help with testing? Check out these snippets:
- **Comprehensive testing:** Test all routes and features
- **Edge cases:** Test with empty inputs, very long inputs
- **User experience:** Ensure smooth navigation and interactions

## ✅ Check
1. Test all routes thoroughly
2. Test with different inputs and edge cases
3. Ensure smooth user experience
4. Add any final styling improvements
5. Everything should work perfectly

---

<!-- LEVEL_START -->

# Level 16: Documentation and README

**User Story:** As a developer, I want to create clear documentation so that others can understand and use my Mad Libs application.

## What You'll Do
Update your README.md with comprehensive project documentation.

## Instructions
- Add project description and features
- Include setup and installation instructions
- Add usage instructions
- Include technical details

## 💡 Code Hints
Need help with documentation? Check out these snippets:
- **Project description:** Explain what the app does
- **Setup instructions:** Include npm install and run commands
- **Usage instructions:** Explain how to use the app
- **Technical details:** List technologies and concepts used

## ✅ Check
1. README should clearly describe the project
2. Setup instructions should be complete
3. Usage instructions should be clear
4. Technical details should be accurate
5. Documentation should be professional

---

<!-- LEVEL_START -->

# Level 17: Git Setup and Version Control

**User Story:** As a developer, I want to set up version control so that I can track changes and share my Mad Libs project on GitHub.

## What You'll Do
Initialize version control and push your project to GitHub.

## Instructions
- Initialize a git repository (`git init`)
- Add all files to git (`git add .`)
- Create your first commit with a meaningful message
- Push to GitHub (if you have a remote repository set up)

## 💡 Code Hints
Need help with git? Check out these snippets:
- **Git init:** Use `git init` to initialize repository
- **Git add:** Use `git add .` to add all files
- **Git commit:** Use `git commit -m "message"` to commit changes
- **Git push:** Use `git push` to push to remote repository

## ✅ Check
1. Run `git status` - you should see "On branch main" and "nothing to commit, working tree clean"
2. Run `git log --oneline` - you should see your commit message
3. Verify your project is on GitHub
4. If you see any errors, check your git commands and repository setup

---

<!-- LEVEL_START -->

# Level 18: Challenge Extensions ⚡ ADVANCED CHALLENGE LEVEL

**User Story:** As a developer, I want to implement advanced features so that I can create an even more impressive Mad Libs application.

## What You'll Do
Implement advanced features from the challenge extensions document.

## Instructions
- Review the [Mad Libs Challenge Extensions](./mad-libs-mini-project-challenge-todo.md)
- Choose one or more challenges to implement
- Add the advanced features to your application

## 💡 Code Hints
Need help with challenges? Check out these snippets:
- **Form validation:** See Challenge 1 for validation examples
- **Data storage:** See Challenge 2 for array storage
- **Random access:** See Challenge 3 for random story selection
- **Individual access:** See Challenge 4 for query parameter handling
- **Navigation:** See Challenge 5 for next story links
- **Boundary checking:** See Challenge 6 for preventing invalid access

## ✅ Check
1. Choose and implement at least one challenge
2. Test your challenge implementation thoroughly
3. Ensure the new features work correctly
4. Update your documentation if needed
5. Commit your changes to git

---

<!-- LEVEL_START -->

# Level 19: Final Integration and Testing

**User Story:** As a developer, I want to integrate all features and test everything together so that my complete Mad Libs application works flawlessly.

## What You'll Do
Integrate all features and perform final comprehensive testing.

## Instructions
- Test all features together
- Test with different scenarios and edge cases
- Ensure smooth user experience
- Fix any remaining issues

## 💡 Code Hints
Need help with integration? Check out these snippets:
- **Comprehensive testing:** Test all features systematically
- **Edge cases:** Test with empty inputs, invalid numbers, etc.
- **User experience:** Ensure smooth navigation and interactions
- **Error handling:** Test error scenarios and recovery

## ✅ Check
1. Test all features thoroughly
2. Test with different scenarios and edge cases
3. Ensure smooth user experience
4. Fix any remaining issues
5. Everything should work perfectly

---

<!-- LEVEL_START -->

# Level 20: Project Complete

**User Story:** As a developer, I want to celebrate my completed Mad Libs project so that I can appreciate what I've accomplished and plan my next learning steps.

## What You'll Do
Celebrate your completed Mad Libs project!

## Instructions
- Take a moment to appreciate what you've accomplished
- Reflect on what you've learned
- Be proud of your work

## 🎉 Congratulations!

You've successfully completed your Mad Libs mini-project! You've built a full-stack web application that demonstrates:

- **Server-side development** with Node.js and Express
- **Form handling** and data processing
- **Template literals** for dynamic content generation
- **Array operations** and data storage
- **Random number generation** and array access
- **Query parameters** and dynamic routing
- **Conditional rendering** and navigation
- **Error handling** and validation
- **Bootstrap styling** and responsive design
- **Version control** with Git and GitHub

## What You've Learned

Through this project, you've gained experience with:
- HTML, CSS, and JavaScript fundamentals
- Node.js and Express.js server development
- Form handling and data processing
- Template literals and dynamic content
- Array operations and data storage
- Random number generation and array access
- Query parameters and dynamic routing
- Conditional rendering and navigation
- Error handling and validation
- Bootstrap framework for styling
- Version control with Git and GitHub
- Project planning and documentation

## Next Steps

- Continue building projects to reinforce your skills
- Explore more advanced Node.js and Express features
- Consider implementing additional challenge extensions
- Keep learning and growing as a developer

## 🎊 Well Done!

You've completed a significant milestone in your coding journey. Your Mad Libs project demonstrates your ability to build real-world web applications and solve complex problems with code.

---

**Project Complete!** 🎉

---

## Resources and References

### Code.org Patterns Used:
- **Random List Access Pattern**: [Code.org Documentation](https://studio.code.org/docs/concepts/patterns/random-list-access/)
- **List Scrolling Pattern**: [Code.org Documentation](https://studio.code.org/docs/concepts/patterns/list-scrolling-pattern/)

### Additional Resources:
- Express.js Documentation
- Node.js Documentation
- Bootstrap Documentation
- MDN Web Docs (JavaScript, HTML, CSS)

### Troubleshooting Tips:
- Check console for error messages
- Verify file paths and server routes
- Test each feature individually
- Use `console.log()` for debugging
- Ask for help when stuck
