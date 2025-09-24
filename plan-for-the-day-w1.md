
# Week 1

## Day 1

* Intro to the class
* Servers + Node.js
* [notes](./notes/week1-notes.md#day-1)

## Day 2: JavaScript Fundamentals for React Development

### 🎯 Learning Objectives
By the end of today, you'll be able to:
- Write modern JavaScript using ES6+ features
- Understand variable declarations and their appropriate usage
- Create and use arrow functions effectively
- Implement template literals for dynamic strings
- Apply ternary operators for conditional logic
- Navigate object properties using different notation styles

### 📚 Core JavaScript Concepts

#### Variable Declarations
- **`var` vs `let` vs `const`**
  - Scope differences (function vs block scope)
  - Hoisting behavior
  - When to use each declaration type
  - Best practices for React development

#### Functions & Arrow Functions
- **Traditional Functions**: `function myFunction() {}`
- **Arrow Functions**: `() => {}`
  - Syntax variations and when to use parentheses
  - `this` binding differences
  - Implicit vs explicit returns
  - Common React patterns

#### Template Literals
- **String Interpolation**: `` `Hello ${name}!` ``
- **Multi-line strings**
- **Expression evaluation**
- **Dynamic content generation**

#### Conditional Logic
- **Ternary Operator**: `condition ? trueValue : falseValue`
- **Logical operators**: `&&`, `||`
- **Conditional rendering patterns**

#### Object Notation
- **Dot notation**: `obj.property`
- **Bracket notation**: `obj['property']`
- **Dynamic property access**
- **When to use each approach**

### 📖 Learning Resources
- **[Interactive Course](https://www.educative.io/courses/javascript-fundamentals-before-learning-react)** - Comprehensive JavaScript fundamentals
- **[Robin Wieruch's Guide](https://www.robinwieruch.de/javascript-fundamentals-react-requirements/)** - React-specific JavaScript requirements
  - [Arrow Functions in React](https://www.robinwieruch.de/javascript-fundamentals-react-requirements/#arrow-functions-in-react)
  - [Template Literals in React](https://www.robinwieruch.de/javascript-fundamentals-react-requirements/#template-literals-in-react)
  - [var, let and const in React](https://www.robinwieruch.de/javascript-fundamentals-react-requirements/#var-let-and-const-in-react)
  - [Ternary Operator in React](https://www.robinwieruch.de/javascript-fundamentals-react-requirements/#ternary-operator-in-react)

### 🛠️ Hands-On Practice: Enhanced Server Project

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

### 💡 Pro Tips
- Practice writing arrow functions until they feel natural
- Always prefer `const` unless you need to reassign the variable
- Use template literals for any string that includes variables
- Bracket notation is essential for dynamic property access
- Ternary operators make code more concise for simple conditionals

## Day 3

* Code.org lesson - loops
* patterns
