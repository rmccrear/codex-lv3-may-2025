# Level 3 Vocabulary

## Table of Contents

- [Week 1](#week-1) - Servers and Node.js
- [Week 2](#week-2) - React Components
- [Week 3](#week-3) - React Events
- Week 4 - Hackathon
- [Week 5](#week-5) - Databases and Forms

---

## Week 1

### Server

A computer program that delivers things (like files or data) to your browser when you ask for them—like a waiter bringing food at a restaurant.

### Node.js (Node)

A way to run JavaScript on your computer (not just in the browser). It lets you build the "backend" or server side of websites.

**📺 Learn More:** [Node.js Ultimate Beginner's Guide in 7 Easy Steps](https://www.youtube.com/watch?v=ENrzD9HAZK4)

### Request (REQ)

The "ask." When your browser talks to a server, it sends a request (like asking for a webpage or some data).

### Response (RES)

The "answer." After the server gets the request, it sends back a response (like the HTML, CSS, or data you asked for).

### Event-driven Architecture

A style of programming where the server waits for events (like a request) and then reacts to them, just like addEventListener in the browser.

**📺 Learn More:** [JavaScript Visualized - Event Loop, Web APIs, (Micro)task Queue](https://www.youtube.com/watch?v=eiC58R16hb8)

### NPM

Short for Node Package Manager. A tool that helps you add extra code "packages" (like apps or helpers) into your project.

**📺 Learn More:** [What is NPM, and why do we need it? | Tutorial for beginners](https://www.youtube.com/watch?v=P3aKRdUyr0s)

### Module

A chunk of code you can bring into your project. Example: Express is a module that helps you make a server.

**📺 Learn More:** [JavaScript Modules in 100 Seconds](https://www.youtube.com/watch?v=qgRUr-YUk1Q)

### Mad Libs

A word game where players fill in blanks in a story with random words (like nouns, verbs, adjectives) without knowing the context. The result is usually a funny and nonsensical story! In our course, you'll build a web application that creates Mad Libs stories using forms.

**📖 Learn More:** [Mad Libs Format - Wikipedia](https://en.wikipedia.org/wiki/Mad_Libs#Format)  
**📺 Learn More:** [Mad Libs Gameplay Video](https://www.youtube.com/watch?v=48pP0WFjuOE)

### Express

A popular module for Node.js that makes building servers and handling requests/responses much easier.

### Port

A "door number" on your computer where your server listens for requests. Example: [http://localhost:3000](http://localhost:3000/).

### ES6 Function / Arrow Function

A shorter way to write functions in JavaScript. Example:

```javascript
(req, res) => {
  res.send("Hello!");
}
```

**📺 Learn More:** [Arrow Functions - Beau teaches JavaScript](https://www.youtube.com/watch?v=22fyYvxz-do)

### Path (Route)

The address you type after the main website, like `/about` or `/login`. It tells the server what part you want.

### Counter Pattern

A coding pattern where you use a variable to keep track of counts (like adding 1 in a loop). It's often the first loop pattern students learn.

### Template Literal

A way to put variables into strings using backticks (`). Example:

```javascript
`Hello, ${name}!`
```

### Loopback URL / IP

Special addresses (`localhost` or `127.0.0.1`) that let you test a server running on your own computer.

### Event Listener

Code that waits for something to happen (like a button click or a request) and then runs a function in response.

### Scoping

Rules that decide where variables can be used. Example: `let` and `const` fix problems that older `var` variables had.

### Ternary Operator

A shorthand if/else written in one line. Example:

```javascript
let result = score > 10 ? "Win" : "Lose";
```

**📺 Learn More:** [? in NaN Seconds](https://www.youtube.com/watch?v=O0gmXbN7lVE)

### Bracket Notation

A way to access object properties using square brackets. Example:

```javascript
myDog["age"];
```

### String

A piece of text inside quotes. Example: `"Hello world"`.

### Backend

The hidden "server side" of a website or app where data and logic live. Users don't see this part.

### Endpoint

A specific path on the server you can ask for. Example:

```javascript
app.get("/cats", (req, res) => { ... });
```

### V8 Engine

The part of Chrome (and Node.js) that runs JavaScript by turning code into actions on the screen or server.

### Array Literal

The syntax to create an array, using square brackets. Example:

```javascript
let colors = ["red", "green", "blue"];
```

### Index

The number that tells you an item's position in a list. Indexes start at 0. Example: in `["a", "b", "c"]`, `"a"` is index 0.

### List Scrolling Pattern

A coding pattern that uses the counter to move up or down a list, like scrolling through items in an app.

### Insert Item / Append Item

Ways to add new things to a list. Insert puts it at a chosen index, append puts it at the end. Example:

```javascript
myList.push("new item"); // append
myList.splice(0, 0, "first"); // insert at top
```

---

## Week 2

**🎵 Song:** [React Components Song](https://suno.com/s/HMFrtLoL75BpCxdI)

### Components

The building blocks of React. Everything in React is made from components. They help organize code and keep programs from becoming too complicated.

### React

A framework created by Facebook in 2013. It's built on the idea of components and is one of the most popular tools for making modern websites.

### JSX

A special syntax used in React. It looks like HTML but isn't exactly the same. JSX must be used inside React components.

### Vite (VEET)

A tool to quickly start a React project. By default, it runs on port 5173 (which matches the letters V-I-T-E as a memory trick – "V" is "5" in Roman Numerals).

### Controlling Complexity

Called the "essence of programming." In React, using components is a way to control complexity by breaking big problems into smaller, reusable pieces.

### Props (Properties)

Attributes you can give to components to make them more powerful. Props are like HTML attributes but for your own custom components.

### Return

In a React component function, the return statement sends back the JSX that should be shown on the screen. It's similar to `res.send` in a server.

### Nesting

Putting one component inside another. Example: placing `<Skills />` inside your main `<App />`.

### Fragments

Empty angle brackets (`<>...</>`) used in React components. They allow you to return multiple JSX elements without needing an extra wrapper element.

### ESLint

A tool that comes installed when you set up a React project with Vite. It checks your code and warns about errors or bad practices.

### Node modules

The folder that appears after installing dependencies. It contains all the extra code React needs to run.

---

## Week 3

### State

Component-local data React preserves between renders so a component can remember information and update the UI (e.g., a click counter).

**🔗 Learn More:** [State: A Component's Memory](https://react.dev/learn/state-a-components-memory)

### Hook

Special React function whose name starts with `use` (e.g., `useState`, `useEffect`). Must follow the Rules of Hooks.

**🔗 Learn More:** [Using Hooks](https://react.dev/learn#using-hooks)

### useState

Hook that returns a state value and a setter:

```javascript
const [count, setCount] = useState(0);
```

Initializes component state and triggers re-render when the setter is called.

**🔗 Learn More:** [Adding Interactivity: useState](https://react.dev/learn/state-a-components-memory#adding-interactivity)

### Setter Function (`setCount`)

The function from `useState` used to update state (e.g., `setCount(prev + 1)`). Schedules an update; React re-renders with the new state.

**🔗 Learn More:** [State Setter Functions](https://react.dev/learn/state-a-components-memory#updating-state)

### handleClick

Conventional camelCase name for a click event handler:

```javascript
function handleClick() {
  setScore(s + 1);
}
```

**🔗 Learn More:** [Responding to Events](https://react.dev/learn/responding-to-events)

### Conditional Rendering

Showing different UI based on a condition using JS expressions in JSX (e.g., `{isOn ? 'On' : 'Off'}`).

**🔗 Learn More:** [Conditional Rendering](https://react.dev/learn/conditional-rendering)

### Ternary Operator

`condition ? exprIfTrue : exprIfFalse`; commonly used inside JSX for conditional rendering.

**🔗 Learn More:** [Conditional Rendering (ternary)](https://react.dev/learn/conditional-rendering#choosing-between-two-jsx-tags)

### List / Array

Core JS structure often paired with loops or array methods (`map`, `filter`) to render repeated UI.

### List Patterns

Common approaches for working with lists, such as **Random List Access** and **List Scrolling Pattern**.

**📺 Learn More:** [Code.org Unit 5 Lesson 11.6 - Reduce and Filter | Traversals Practice](https://www.youtube.com/watch?v=erFdoVvkTLc)  
**🔗 Learn More:** [List Filter Pattern](https://studio.code.org/docs/concepts/patterns/list-filter-pattern/)  
**🔗 Learn More:** [List Reduce Pattern](https://studio.code.org/docs/concepts/patterns/list-reduce-pattern/)  
**🔗 Learn More:** [List Scrolling Pattern](https://studio.code.org/docs/concepts/patterns/list-scrolling-pattern/)  
**🔗 Learn More:** [Code.org Unit 6 Lesson 11.6](https://studio.code.org/courses/csp-2025/units/6/lessons/11/levels/6)

### List Scrolling Pattern

Iterating from index `0` to `list.length - 1` (e.g., `for` loop or `array.map`) to process or render each item.

### Random List Access

Selecting an item by index (often random):

```javascript
let randomIndex = Math.floor(Math.random() * list.length);
let item = list[randomIndex];
```

**🔗 Learn More:** [Rendering Lists](https://react.dev/learn/rendering-lists)

### List Destructuring

Array destructuring syntax, especially used with hooks:

```javascript
const [value, setValue] = useState(0);
const [first, second] = arr;
```

**🔗 Learn More:** [Destructuring Arrays](https://react.dev/learn/state-a-components-memory#adding-a-state-variable)

### Fragment

Wrapper for multiple JSX nodes without adding a DOM element:

```javascript
<>...</>
```

or

```javascript
<React.Fragment>...</React.Fragment>
```

### children prop

Special prop containing nested JSX between a component's opening and closing tags:

```xml
<MyCard>
  <p>Hello!</p>
</MyCard>
```

**🔗 Learn More:** [Passing JSX as Children](https://react.dev/learn/passing-props-to-a-component#passing-jsx-as-children)

### Prop

Read-only inputs to a component, similar to HTML attributes. Can model variants (e.g., `<Button variant="primary" />`) or pass classes via `className`.

**🔗 Learn More:** [Passing Props to a Component](https://react.dev/learn/passing-props-to-a-component)

### Declarative vs Imperative

Two different programming styles:

**Declarative (HTML / React):** You describe *what* you want the UI to look like, and React updates it. Example:

```jsx
<button disabled={isLoading}>Submit</button>
```

You declare the desired outcome, React handles the details.

**Imperative (Vanilla JS):** You write instructions for *how* to change the DOM step by step. Example:

```javascript
const btn = document.querySelector("button");
if (isLoading) {
  btn.setAttribute("disabled", true);
} else {
  btn.removeAttribute("disabled");
}
```

React emphasizes **declarative** code because it's easier to read, maintain, and reason about.

**🔗 Learn More:** [Declarative Programming](https://react.dev/learn/reacting-to-input-with-state)

---

## Week 5

### Database (DB)

A structured place to store and organize data so applications can save, read, update, and delete information.

**🔗 Learn More:** [Introduction to SQL & Databases](https://sqlbolt.com/lesson/introduction)

### Persistence / Persist

When data stays saved even after refreshing the page or restarting the app/server — unlike variables in JavaScript which disappear on reload.

**📺 Learn More:** [Understanding Data Persistence](https://www.youtube.com/watch?v=yJAsyKjhKIY)  
**📺 Learn More:** [Data Persistence Explained](https://www.youtube.com/watch?v=fkf28stMSr8)

### Supabase

A backend-as-a-service that gives you a PostgreSQL database, authentication, storage, and APIs. Works like an open-source Firebase.

**📺 Learn More:** [Supabase in 100 Seconds](https://www.youtube.com/watch?v=zBZgdTb-dns)  
**🔗 Learn More:** [https://supabase.com](https://supabase.com/)

### Firebase

Google's backend service for real-time databases, authentication, hosting, and storage. Uses NoSQL (document-style) data.

**📺 Learn More:** [Firebase in 100 Seconds](https://www.youtube.com/watch?v=vAoB4VbhRzM)  
**🔗 Learn More:** [https://firebase.google.com](https://firebase.google.com/)

### SQL

Structured Query Language — used to communicate with relational databases like PostgreSQL and MySQL.

**📺 Learn More:** [SQL Explained in 100 Seconds](https://www.youtube.com/watch?v=zsjvFFKOm3c)  
**🔗 Learn More:** [Intro to SQL](https://sqlbolt.com/lesson/introduction)

### Table

A collection of related data in the database, organized into rows and columns — similar to a spreadsheet.

**📺 Learn More:** [MySQL - The Basics // Learn SQL in 23 Easy Steps](https://www.youtube.com/watch?v=Cz3WcZLRaWc)  
**🔗 Learn More:** [Intro to SELECT Queries](https://sqlbolt.com/lesson/select_queries_introduction)

### Column

A labeled field in a table (e.g., `email`, `price`, `user_id`) that defines one type of data.

**🔗 Learn More:** [Columns & Rows](https://sqlbolt.com/lesson/select_queries_introduction)

### Row / Record

One entry in a table — like one user, one product, or one message.

**🔗 Learn More:** [Rows in Tables](https://sqlbolt.com/lesson/select_queries_introduction)

### SELECT

SQL command that reads data from a database.

```sql
SELECT * FROM users;
```

**📺 Learn More:** [MySQL - The Basics // Learn SQL in 23 Easy Steps](https://youtu.be/Cz3WcZLRaWc?si=BioNlI44I8nz3cDL&t=626)  
**🔗 Learn More:** [SELECT Basics](https://sqlbolt.com/lesson/select_queries_introduction)

### INSERT

SQL command that adds a new row into a table.

```sql
INSERT INTO users (name, age) VALUES ('Alex', 23);
```

**📺 Learn More:** [MySQL - The Basics // Learn SQL in 23 Easy Steps](https://youtu.be/Cz3WcZLRaWc?si=I_NGyaUbGMugW3MF&t=570)  
**🔗 Learn More:** [Inserting Rows](https://sqlbolt.com/lesson/inserting_rows)

### RLS Policy (Row-Level Security)

Rules in Supabase/PostgreSQL that control which users are allowed to read or write specific rows in a table (helps protect user data).

**📺 Learn More:** [RLS Policy Short](https://www.youtube.com/shorts/YAor6JTaqXI)  
**🔗 Learn More:** [Supabase RLS](https://supabase.com/docs/guides/auth/row-level-security)

### Environment Variables (`.env`)

Hidden configuration values like API keys, database URLs, or secrets that you don't want hardcoded in your JavaScript. Stored in a `.env` file.

**📺 Learn More:** 
- [Builds with Vite #16 - Environment variables](https://www.youtube.com/watch?v=jqCjflIGH1o)
- [What are Environment variables? [10 of 20] | Bash for Beginners](https://www.youtube.com/watch?v=aKghi0hI1OA)

**🔗 Learn More:** [Environment Variables – Supabase Docs](https://supabase.com/docs/guides/cli/local-development#environment-variables)

### Snake Case

Naming style using lowercase letters and underscores:  
`first_name`, `user_id`, `total_price`

---

## Advanced JavaScript Syntax

**🎵 Song "Function Flow":** [https://suno.com/s/eY8iez0gM4n1f3ZB](https://suno.com/s/eY8iez0gM4n1f3ZB)

### Async

A keyword that makes a function return a Promise and allows use of `await` inside it.

**📺 Learn More:** [The Async Await Episode I Promised](https://www.youtube.com/watch?v=vn3tm0quoqE)  
**🔗 Learn More:** [MDN – async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)

### await

Pauses inside an `async` function until a Promise is done.

```javascript
const data = await fetch('/api/items');
```

**🔗 Learn More:** [MDN – await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)

### fetch

Built-in browser function that makes HTTP requests to APIs. Returns a Promise.

**🔗 Learn More:** [MDN – fetch](https://developer.mozilla.org/en-US/docs/Web/API/fetch)

**🎵 Song:** [https://suno.com/s/fbOIwkbe1StSb6hY](https://suno.com/s/fbOIwkbe1StSb6hY)

**📺 Learn More:** [Learn JavaScript LOGICAL OPERATORS in 5 minutes ❗](https://www.youtube.com/watch?v=ovWYhDVQiR8)

### AND (`&&`)

Returns the first falsy value or the last value if all are truthy. Often used in conditions.

**🔗 Learn More:** [MDN – Logical AND](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND)

### OR (`||`)

Returns the first truthy value or the last value if none are truthy.

**🔗 Learn More:** [MDN – Logical OR](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR)

### NOT (`!`) / Bang

Flips a boolean value.  
Example: `!true // false`

**🔗 Learn More:** [MDN – Logical NOT](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT)

### Triple Equals (`===`)

Strict comparison — checks both value and type.

```javascript
5 === '5'; // false
```

**📺 Learn More:** [Learn JavaScript STRICT EQUALITY in 3 minutes! 🟰](https://www.youtube.com/watch?v=O7aUm0AuUy4)  
**🔗 Learn More:** [MDN – Strict Equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality)

### Truthy & Falsy

Values that count as `true` or `false` in an `if` statement.  
Falsy values: `0`, `""`, `null`, `undefined`, `NaN`, `false`

**🔗 Learn More:** [MDN – Truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)

### Scoping

Where a variable exists in your code (block, function, or global).

**🔗 Learn More:** [MDN – Scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope)

### Destructuring

A shortcut to pull values from objects or arrays.

```javascript
const { name } = user;
const [first, second] = items;
```

**🔗 Learn More:** [MDN – Destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)

### Function / Anonymous Function

Reusable block of code. Anonymous functions have no name:

```javascript
() => console.log('Hi');
```

**🔗 Learn More:** [MDN – Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)

### Argument

The actual value passed to a function when calling it.

### Return

Ends a function and sends a value back to wherever it was called.

### push

Adds a value to the *end* of an array.

**🎵 Song:** [https://suno.com/s/7xLQemRspSLltEYS](https://suno.com/s/7xLQemRspSLltEYS)  
**🔗 Learn More:** [MDN – push](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push)

### pop

Removes the *last* value from an array and returns it.

**🔗 Learn More:** [MDN – pop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop)

### Kata

A coding exercise where you practice implementing a specific feature or pattern repeatedly to build muscle memory and fluency. In our course, you'll work through React Katas to master component creation, state management, and event handling.

**📺 Learn More:** [What is a Coding Kata?](https://www.youtube.com/watch?v=ZW4AEKbHE28)  
**🔗 Learn More:** [React Katas](../week5/kata/README.md)

### import/export Module Cheatsheet

**📺 Learn More:** [JavaScript Modules in 100 Seconds](https://www.youtube.com/watch?v=qgRUr-YUk1Q)  
**🔗 Learn More:** [Module Cheatsheet](https://www.samanthaming.com/tidbits/79-module-cheatsheet/)