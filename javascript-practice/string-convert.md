## 🐍 Mini Lesson: Changing a String to Snake Case in JavaScript

### 🎯 Goal

Learn how to write a **function** that changes any string into **snake_case** format, and understand how **arguments** and **return values** work inside that function.

---

### 🧩 Step 1: What Is Snake Case?

**Snake case** means writing all words in **lowercase** and separating them with **underscores**.
It’s often used for file names and variable names, like:

```
"Hello World" → "hello_world"
```

---

### 🧠 Step 2: Function Purpose and Structure

A **function** is a small, reusable piece of code that performs a specific job.
We give it **input** to work with, and it gives us **output** back.

#### Example structure:

```js
function name(argument) {
  // do something
  return result;
}
```

In our case, the function will:

* Take in a **string** (the argument)
* Return a **new string** in snake_case form (the return value)

---

### 💬 Step 3: Understanding Arguments

An **argument** is the **value you pass into a function** so it has something to work on.

For example:

```js
toSnakeCase("Hello World")
```

Here, `"Hello World"` is the **argument**.
Inside the function, you might refer to it as a **parameter** like `text`.
That’s just the **name** of the value while the function is running.

Arguments let functions handle many different inputs without rewriting code each time.

---

### 🎁 Step 4: Understanding Return Values

A **return value** is what the function **gives back** when it finishes.

If a function doesn’t `return` anything, it won’t produce a usable result.
For example, after we process `"Hello World"`, the function should **return** `"hello_world"`.

Returning a value makes the function **reusable**:

```js
let newText = toSnakeCase("JavaScript Is Fun");
// now newText holds "javascript_is_fun"
```

---

### 🧰 Step 5: String Methods We’ll Need

To make this conversion, we’ll use two built-in **string methods**:

* **`.toLowerCase()`** — turns all letters into lowercase.
* **`.replace()`** — swaps one set of characters for another (like spaces → underscores).

These methods help us transform the input step by step.

---

### 🧩 Step 6: The Process

1. Start with a string that might have capital letters and spaces.
2. Use `.toLowerCase()` to make everything lowercase.
3. Use `.replace()` or `.replaceAll(" ", "_")` to swap spaces for underscores.
4. Return the final, transformed string.

This is how your function takes an **argument**, processes it, and provides a **return value**.

---

### 🧰 Step 7: Expanding Your Skills

Once you’re comfortable with snake case, you can explore other formats using new methods:

* **`.split(" ")`** — breaks a string into an array of words.
* **`.join("_")`** — joins words together with a chosen symbol.

These will be useful for more complex conversions later.

---

### ⚡ Challenges

1. **Kebab Case:**
   Replace underscores with dashes → `"Hello World"` → `"hello-world"`

2. **Camel Case:**
   Join words without symbols and capitalize each word except the first → `"Hello World"` → `"helloWorld"`

---

### 📝 Summary

| Concept                 | Description                                                                             | Example         |
| ----------------------- | --------------------------------------------------------------------------------------- | --------------- |
| **Argument**            | The input we give to the function                                                       | `"Hello World"` |
| **Return Value**        | The new value the function gives back                                                   | `"hello_world"` |
| **String Methods Used** | `.toLowerCase()`, `.replace()`                                                          |                 |
| **Next Step**           | Practice writing your own `toSnakeCase` function, then adapt it for kebab or camel case |                 |

---

### 📚 Next Steps

Ready to organize your code? Learn how to **import and use** your `toSnakeCase` function in other files:

👉 [Importing Functions with Node.js](./string-convert-imports.md)

---

### 🙏 Acknowledgement

This lesson was created with assistance from GPT-5.
