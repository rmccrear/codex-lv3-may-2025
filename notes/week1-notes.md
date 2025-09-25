# Week 1 Notes

## Table of Contents

- [Day 1](#day-1)
- [Day 2: JavaScript Fundamentals for React Development](#day-2-javascript-fundamentals-for-react-development)
- [Day 3: Loops and Patterns](#day-3-loops-and-patterns)

---

## Day 1

[slides](https://docs.google.com/presentation/d/1oeOAD7S_alHmSAVD7FGZWn4FgGcUw-RhwbrxEEZ9gO4/edit?usp=sharing)

Today we are building a server.

Steps:

* create a github repo
* create a `server.js` file
* create a .gitignore file with `/node_modules`
* Create a npm package with these commands:
    * `npm init -y`
    * `npm install express`
* Make a server in `server.js`
    * See the slides for today
* Use this command to run it:
    * `node server.js`
    * use `^C` to restart the server when you make changes.

### Learning Objectives
By the end of today, you'll be able to:
- Understand the fundamentals of web development and client-server architecture
- Set up a Node.js development environment
- Create and run a basic HTTP server
- Handle different HTTP routes
- Understand the request-response cycle
- Debug server applications effectively

### Web Development Fundamentals

#### Client-Server Architecture
- **How the web works**: Request → Server → Response
- **Frontend vs Backend**: What runs where and why
- **HTTP Protocol**: The language of the web
- **URLs and Routes**: How we navigate web applications

#### Introduction to Node.js
- **What is Node.js?**: JavaScript runtime for servers
- **Why Node.js?**: Benefits for web development
- **npm**: Package management and ecosystem
- **Development workflow**: From code to running server

### Hands-On Practice: Building Your First Server

#### Server Setup Checklist
Create a Node.js server that demonstrates core web development concepts:

1. **✅ Project Initialization**
   ```bash
   mkdir my-first-server
   cd my-first-server
   npm init -y
   npm install express
   ```

2. **✅ Basic Server Structure**
   ```javascript
   const express = require('express');
   const app = express();
   const PORT = 3000;
   
   app.get('/', (req, res) => {
     res.send('Hello, World!');
   });
   
   app.listen(PORT, () => {
     console.log(`Server running on http://localhost:${PORT}`);
   });
   ```

3. **✅ Multiple Routes**
   - Create endpoints for different purposes
   - Understand route parameters
   - Handle different HTTP methods (GET, POST)

4. **✅ Error Handling**
   - Implement basic error handling
   - Understand HTTP status codes
   - Create meaningful error responses

5. **🎯 Bonus Challenge: Dynamic Content**
   - Use query parameters
   - Create interactive responses
   - Implement basic data handling

#### Key Concepts to Master
- **Express.js**: Web framework for Node.js
- **Routing**: How to handle different URL paths
- **Request Object**: Accessing client data
- **Response Object**: Sending data back to client
- **Ports**: How servers communicate

### Learning Resources
- **[Node.js Official Documentation](https://nodejs.org/en/docs/)** - Comprehensive Node.js reference
- **[Express.js Guide](https://expressjs.com/en/guide/routing.html)** - Express routing fundamentals
- **[HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)** - Understanding response codes
- **[npm Documentation](https://docs.npmjs.com/)** - Package management guide

### Pro Tips
- Always test your server after making changes
- Use `console.log()` to debug and understand what's happening
- Start simple and add complexity gradually
- Remember to restart your server when you make changes
- Use meaningful route names that describe what they do
- Keep your code organized and commented for clarity

## Day 2: JavaScript Fundamentals for React Development

### Learning Objectives
By the end of today, you'll be able to:
- Write modern JavaScript using ES6+ features
- Understand variable declarations and their appropriate usage
- Create and use arrow functions effectively
- Implement template literals for dynamic strings
- Apply ternary operators for conditional logic
- Navigate object properties using different notation styles

### Core JavaScript Concepts

#### Variable Declarations
- **`var` vs `let` vs `const`**
  - Scope differences (function vs block scope)
  - Hoisting behavior
  - When to use each declaration type
  - Best practices for React development

#### Functions & Arrow Functions
- **Traditional Functions**: `function myFunction() {}`
- **Arrow Functions**: `() => {}`

#### Template Literals
- **String Interpolation**: `` `Hello ${name}!` ``
- **Multi-line strings**
- **Expression evaluation**
- **Dynamic content generation**

#### Conditional Logic
- **Ternary Operator**: `condition ? trueValue : falseValue`

#### Object Notation
- **Dot notation**: `obj.property`
- **Bracket notation**: `obj['property']`

### Learning Resources
- **[Interactive Course](https://www.educative.io/courses/javascript-fundamentals-before-learning-react)** - Comprehensive JavaScript fundamentals
- **[Robin Wieruch's Guide](https://www.robinwieruch.de/javascript-fundamentals-react-requirements/)** - React-specific JavaScript requirements
  - [Arrow Functions in React](https://www.robinwieruch.de/javascript-fundamentals-react-requirements/#arrow-functions-in-react)
  - [Template Literals in React](https://www.robinwieruch.de/javascript-fundamentals-react-requirements/#template-literals-in-react)
  - [var, let and const in React](https://www.robinwieruch.de/javascript-fundamentals-react-requirements/#var-let-and-const-in-react)
  - [Ternary Operator in React](https://www.robinwieruch.de/javascript-fundamentals-react-requirements/#ternary-operator-in-react)

### Hands-On Practice: Enhanced Server Project

#### Development Environment Setup
First, let's improve your development workflow with nodemon:

```bash
# Install nodemon globally for automatic server restarts
npm install -g nodemon

# Or install as a dev dependency in your project
npm install --save-dev nodemon
```

**Using nodemon:**
```bash
# Instead of: node server.js
# Use: nodemon server.js
nodemon server.js
# or
npx nodemon server.js
```

#### Server Enhancement Checklist
Update your Node.js server to demonstrate modern JavaScript concepts:

1. **✅ Template Literals**
   - Replace string concatenation with backticks and `${}`
   - Create dynamic responses using variables

2. **✅ Multiple Endpoints**
   ```javascript
   app.get("/my-cat", (req, res) => {
     // Your cat endpoint
   });
   
   app.get("/my-dog", (req, res) => {
     // Your dog endpoint
   });
   ```

3. **✅ Object Manipulation**
   - Create a POJO (Plain Old JavaScript Object)
   - Use bracket notation for dynamic property access
   - Demonstrate both dot and bracket notation

4. **✅ Modern Variable Declarations**
   - Replace `var` with `let` and `const` appropriately
   - Show understanding of when to use each

5. **🎯 Bonus Challenge: Ternary Operators**
   - Implement conditional logic using ternary operators
   - Create dynamic responses based on request parameters

#### Reference Materials
- **[Sample Code Repository](https://github.com/rmccrear/node-server-demo)** - Working examples
- **[Presentation Slides](https://docs.google.com/presentation/d/19uCcQR8DVvdMSm5BKJEjxW62xr4-bbDhsnj9mbrb854/edit?usp=sharing)** - Visual learning aids

### Pro Tips
- Practice writing arrow functions until they feel natural
- You may always use `let` but prefer `const` unless you need to reassign the variable.
- Use template literals for any string that includes variables
- Bracket notation is useful in some cases.
- Ternary operators make code more concise for simple conditionals

## Day 3: Lists and Patterns

### Learning Objectives

### Core Concepts
- **Code.org patterns**: Random List Access Pattern, List Scrolling Pattern, Update Screen Pattern

### Learning Resources
- **[Code.org Lists Lesson](https://studio.code.org/courses/csp-2025/units/6/lessons/1/levels/1)** - Interactive loop fundamentals
- **[Arrays and Loops Tutorial](https://github.com/microsoft/Web-Dev-For-Beginners/tree/main/2-js-basics/4-arrays-loops)** - Basic Tutorial from Microsoft

![Video on adding data to an array](https://youtu.be/ZARmjyg7Lik?feature=shared)

### Hands-On Practice
- Complete Code.org list exercises
- Practice list patterns with JavaScript