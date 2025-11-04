## 📦 Mini Lesson: Importing Functions with Node.js

### 🎯 Goal

Learn how to **separate your code into different files** and **import functions** from one file into another using Node.js **modules**. This helps you organize your code and reuse functions across multiple files.

---

### 📚 Two Module Systems

JavaScript has two main ways to import and export code:

**1. CommonJS (older style):**
```js
// Export
module.exports = add;

// Import
const add = require('./add');
```

**2. ES6 Modules (modern style):**
```js
// Export
export default add;

// Import
import add from './add.js';
```

**In this lesson, we'll use ES6 modules** (the modern style). This requires adding `"type": "module"` to your `package.json` file, or using `.mjs` file extensions.

---

### 🧩 Step 1: Why Separate Code into Files?

When your code gets bigger, it's better to organize it into **separate files**:

* **Reusability** — Write a function once, use it in many places
* **Organization** — Keep related code together
* **Maintainability** — Easier to find and fix bugs
* **Teamwork** — Multiple people can work on different files

---

### 🧠 Step 2: Exporting a Function

Before you can **import** a function, you need to **export** it from the file where it's defined.

#### Example: `add.js`

```js
// Your function code here...

// Export the function so other files can use it
export default add;
```

The `export default` line makes the function available to other files.

**Note:** The `add` function is just a **simple example** to demonstrate the import/export pattern. In real projects, you'd use more useful functions like:
* `toSnakeCase()` — Converting strings to snake_case (from the previous lesson)
* `formatDate()` — Formatting dates
* `validateEmail()` — Validating email addresses
* `calculateTotal()` — Business logic calculations
* And many other reusable utility functions

The import/export pattern works the same way regardless of what your function does!

---

### 💬 Step 3: Importing from the Same Directory

When your files are in the **same directory** (next door to each other), you use a **relative path** starting with `./`.

#### Example: Same Directory Structure

```
my-project/
  ├── add.js
  └── app.js
```

#### `add.js` (the function file):

```js
// Your function code here...

export default add;
```

#### `app.js` (the file that uses the function):

```js
// Import the function from the same directory
import add from './add.js';

// Now you can use it!
let result = add(2, 3);
console.log(result); // 5
```

**Key points:**
* `./` means "current directory"
* `import add from './add.js'` looks for `add.js` in the same folder
* You need to include the `.js` extension in ES6 modules

---

### 🎁 Step 4: Importing from a Subdirectory

When your function is in a **subdirectory** (a folder inside your project), you need to specify the path with `./` followed by the folder name.

#### Example: Subdirectory Structure

```
my-project/
  ├── app.js
  └── helpers/
      └── math.js
```

#### `helpers/math.js` (the function file):

```js
// Your function code here...

export default add;
```

#### `app.js` (the file that uses the function):

```js
// Import from the helpers subdirectory
import add from './helpers/math.js';

// Now you can use it!
let result = add(5, 7);
console.log(result); // 12
```

**Key points:**
* `./helpers/math.js` means "look in the `helpers` folder for `math.js`"
* The path always starts with `./` when it's a relative path
* You can nest folders deeper: `./utils/helpers/math.js`

---

### 🧰 Step 5: Understanding Module Paths

There are different ways to specify where to find a module:

| Path Type | Example | Meaning |
| --------- | ------- | ------- |
| **Relative** | `./add` | Same directory |
| **Relative** | `./helpers/math` | Subdirectory |
| **Relative** | `../utils/helper` | Parent directory (go up one level) |
| **Absolute** | `/Users/name/project/helper` | Full path from root |
| **Node Module** | `fs` or `path` | Built-in Node.js module |

For now, focus on **relative paths** starting with `./` for files in your project.

---

### 🧩 Step 6: Complete Example

Let's see a complete example with multiple files:

#### File Structure:

```
my-project/
  ├── app.js
  └── helpers/
      └── math.js
```

#### `helpers/math.js`:

```js
// Your function code here...

// Export both functions
export { add, subtract };
```

#### `app.js`:

```js
// Import both functions from the helpers folder
import { add, subtract } from './helpers/math.js';

// Use them
console.log(add(5, 3)); // 8
console.log(subtract(10, 4));  // 6
```

**Note:** When exporting multiple functions, you use `export { add, subtract }` and can import specific ones using **destructuring** `{ add, subtract }`.

---

### ⚡ Challenges

1. **Import Your Snake Case Function:**
   * Create a `helpers/` folder
   * Create `helpers/string-convert.js` with your `toSnakeCase` function from the previous lesson
   * Export the `toSnakeCase` function
   * Import and use it in `app.js` to convert "Hello World" to snake case

2. **Multiple Functions:**
   * Add `toKebabCase` and `toCamelCase` to your `helpers/string-convert.js` file
   * Export all three functions
   * Import and use them in `app.js`

3. **Nested Folders:**
   * Create `utils/helpers/` structure
   * Move your `string-convert.js` file there
   * Import `toSnakeCase` using `./utils/helpers/string-convert`

---

### 📝 Summary

| Concept | Description | Example |
| ------- | ----------- | ------- |
| **Export** | Making a function available to other files | `export default add;` |
| **Import (Same Dir)** | Getting a function from the same folder | `import add from './add.js';` |
| **Import (Subdirectory)** | Getting a function from a subfolder | `import add from './helpers/math.js';` |
| **Multiple Exports** | Exporting multiple functions | `export { add, subtract };` |
| **Relative Path** | Path starting with `./` that's relative to current file | `./helpers/math.js` |
| **Module** | A file that exports functions/variables for reuse | `math.js` |

---

### 🙏 Acknowledgement

This lesson was created with assistance from GPT-5.

