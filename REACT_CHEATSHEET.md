# 🧠 React Basic Commands and Concepts Cheat Sheet

This cheat sheet focuses on **core React concepts** and the **modern JavaScript (ES6+)** syntax essential for effective React development — especially the tricky ideas of **Props** and **State**.

---

## I. React Application Fundamentals

**Definition:** React is a framework that combines **JavaScript and HTML** to address issues like repetitive code and indentation problems. It’s often described as **“all JavaScript.”**

**Project Setup (Using Vite):**

1. `npm create vite@latest`
2. `cd [project name]`
3. `npm install` — installs dependencies and creates the `node_modules` folder
4. `npm run dev` — starts the local development server

**The Component Function:**

* React code is made of **components**, which are just **functions** that return **JSX**.
* Must start with a **capital letter** (React assumes lowercase is regular HTML).
* Example:

  ```jsx
  export default function Greeting() {
    return <h1>Hello!</h1>;
  }
  ```

**Importing Components:**

When you organize components into separate files (typically in a `components/` folder), you import them using relative paths:

```jsx
// In App.jsx
import Greeting from './components/Greeting';
import Avatar from './components/Avatar';

export default function App() {
  return (
    <>
      <Greeting />
      <Avatar name="Ash" />
    </>
  );
}
```

* Use `./` for current directory or `./components/` for subdirectory
* File extension `.jsx` is optional in the import statement
* Component file must `export default` the component

---

## II. JSX (JavaScript XML) Syntax

**Definition:** JSX lets you write HTML-like code directly inside JavaScript.

**Key Rules:**

* Use **curly braces `{}`** to embed JavaScript inside JSX.
* Use **`className`** instead of `class` for CSS.
* Wrap multiple elements in a parent (e.g., `<div>` or `<>...</>`).

Example:

```jsx
return (
  <>
    <h1>{title}</h1>
    <p>{message}</p>
  </>
);
```

---

## III. Data Handling: Props (Component Configuration)

**Definition:** Props are data passed from a **parent** to a **child** component.

**Usage Example:**

```jsx
<Avatar name="Ash" />
```

**Receiving Props:**

```jsx
export default function Avatar({ name }) {
  return <h2>{name}</h2>;
}
```

**Note:** Using `{ name }` is called **destructuring** - it extracts the `name` property directly from props, making your code cleaner and easier to read.

**Children Prop:**

```jsx
<Card>
  <p>This content is passed as children.</p>
</Card>
```

**Best Practice:**
Start without props → then add props to make components reusable.

---

## IV. Tricky Data Handling: State (`useState`)

**Purpose:**
State allows a component to **remember** information and **update the screen automatically** when that information changes — such as a counter, score, or text input. It replaces manual DOM updates like `document.getElementById()` or `innerText`.

**Import and Declare:**

```jsx
import { useState } from "react";

const [count, setCount] = useState(0);
```

* `count` → current value
* `setCount()` → updates the value
* `0` → initial value

**Rule:**
Never update state directly (`count = count + 1 ❌`).
Use the setter function instead (`setCount(count + 1) ✅`).

---

### 🧩 Example 1: Numeric Counter

```jsx
import { useState } from "react";

export default function Counter() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <button onClick={handleClick}>
      You clicked {count} times
    </button>
  );
}
```

---

### 🧩 Example 2: String State (Using a Word or Name)

```jsx
import { useState } from "react";

export default function Greeting() {
  const [name, setName] = useState("Ash");

  function handleChange() {
    setName("Misty");
  }

  return (
    <>
      <h2>Hello, {name}!</h2>
      <button onClick={handleChange}>Change Name</button>
    </>
  );
}
```

👉 Here, React **remembers** the `name` string and automatically **updates the text** when `setName()` is called.

---

## V. Event Handling

**Events in React:**

* Use **camelCase** event props like `onClick`, `onChange`.
* Pass the function name in **curly braces**.

Example:

```jsx
function handleClick() {
  setCount(count + 1);
}

<button onClick={handleClick}>Add One</button>
```

---

## VI. Useful JavaScript Features for React

| Concept              | Description                   | Example                             |
| -------------------- | ----------------------------- | ----------------------------------- |
| **Arrow Functions**  | Shorter function syntax       | `const greet = () => "Hi";`         |
| **const / let**      | Modern variable declarations  | `const name = "Ash";`               |
| **Ternary Operator** | Inline `if` inside JSX        | `{isOn ? "Yes" : "No"}`             |
| **Array `.map()`**   | Loop through items and render | `{cats.map(cat => <li>{cat}</li>)}` |

---

## VII. Styling and CSS

**Import CSS File:**

```jsx
import './App.css';
```

**Inline Styles:**

```jsx
<div style={{ backgroundColor: 'skyblue', padding: '10px' }}>
  Hello
</div>
```

Note: Use **camelCase** (`backgroundColor` not `background-color`).

**Bootstrap Integration:**
Add to your `index.html`:

```html
<link
  href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
  rel="stylesheet"
/>
```

or use **React Bootstrap** for ready-made components.

---

✅ **Tip:**
React doesn’t update the DOM directly — instead, it **re-renders** the component whenever `state` or `props` change. Think of it like an automatic `updateScreen()` each time your data updates.
