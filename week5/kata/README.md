# React Katas 🥋

Simple React exercises to practice core concepts from the [React Cheatsheet](../../REACT_CHEATSHEET.md).

**📋 [View Assignment Instructions](./KATA_ASSIGNMENT.md)** - Practice and record yourself completing a kata!

## What are Katas?

Katas are small, focused coding exercises designed to build muscle memory and reinforce fundamental concepts. Complete these in order to build your React skills!

## Kata List

### Basic Concepts (1-6)
1. **[Kata 1: Simple Greeting](./kata-01-greeting.md)** - Basic component and JSX
2. **[Kata 2: Welcome with Props](./kata-02-props.md)** - Props and destructuring
3. **[Kata 3: Click Counter](./kata-03-counter.md)** - useState and event handling
4. **[Kata 4: Show/Hide Toggle](./kata-04-toggle.md)** - Boolean state and conditional rendering
5. **[Kata 5: Fruit List](./kata-05-list.md)** - Array .map() to render lists
6. **[Kata 6: Name Input](./kata-06-input.md)** - Controlled inputs with state

### Filter Pattern (7-8)
7. **[Kata 7: Filter Even Numbers](./kata-07-filter-numbers.md)** - Filter pattern with numbers
8. **[Kata 8: Search/Filter Names](./kata-08-filter-search.md)** - Filter pattern with search

### Reduce Pattern (9-11)
9. **[Kata 9: Calculate Total Score](./kata-09-reduce-sum.md)** - Reduce pattern to sum
10. **[Kata 10: Calculate Average Rating](./kata-10-reduce-average.md)** - Reduce pattern to average
11. **[Kata 11: Count by Category](./kata-11-reduce-count.md)** - Reduce pattern to count

### Intermediate: API Integration (12-16)
📡 **[Intermediate Katas: API Integration](./INTERMEDIATE_KATAS.md)** - Async/await, fetch API, and list patterns with real data

## How to Use These Katas

### Option 1: In Your Own Project

1. Create a new Vite React project:
   ```bash
   npm create vite@latest react-katas -- --template react
   cd react-katas
   npm install
   ```

2. For each kata, create the component in your project
3. Import and render it in `App.jsx` to test
4. Try solving without looking at the solution first!

### Option 2: In CodeSandbox

1. Go to [codesandbox.io](https://codesandbox.io/)
2. Create a new React sandbox
3. Complete each kata in the sandbox

### Option 3: Review Only

- Read through each kata
- Study the solutions
- Type them out to build muscle memory

## Tips for Success

- ✅ **Try first, then check** - Attempt the solution before looking
- ✅ **Type it out** - Don't copy/paste; typing builds memory
- ✅ **Understand, don't memorize** - Focus on why the code works
- ✅ **Experiment** - Try variations and see what happens
- ✅ **Use the cheatsheet** - Reference the [React Cheatsheet](../../REACT_CHEATSHEET.md) when stuck

## Concepts Covered

These katas reinforce:
- ✅ Component structure and JSX
- ✅ Props with destructuring
- ✅ useState hook
- ✅ Event handlers (onClick, onChange)
- ✅ Conditional rendering
- ✅ Array mapping
- ✅ Controlled inputs
- ✅ **Filter pattern** - Select items matching criteria (using for loops)
- ✅ **Reduce pattern** - Summarize/calculate from arrays (using for loops)
- ✅ **Async/await** - Handling asynchronous operations with fetch API
- ✅ **useEffect hook** - Fetching data when components load
- ✅ **Combining patterns** - Filter then map, fetch then process

**Note on Array Methods:** While these katas use for loops to practice the underlying patterns, you'll often see the built-in array methods in real code:
- `.map()` - Transforms each item in an array (List Scrolling Pattern)
- `.filter()` - Selects items matching criteria (List Filter Pattern)
- `.reduce()` - Combines all items into a single value (List Patterns)

Learn more: [MDN: Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

## Next Steps

After completing these katas:
- Build a small project combining multiple concepts
- Review your Week 2, 3, or 4 projects
- Prepare for your code interview!

---

**Good luck practicing!** 🚀

---

**Attribution:** These React katas were created with assistance from Claude AI (Anthropic) to provide focused practice exercises for core React concepts.

---

## Glossary

### Key Terms from [Vocabulary List](../../VOCABULARY_LIST.md)

**[Kata](../../VOCABULARY_LIST.md#kata):** A coding exercise where you practice implementing a specific feature or pattern repeatedly to build muscle memory and fluency.

**[Components](../../VOCABULARY_LIST.md#components):** In React, the building blocks of applications. Everything in React is made from components. They help organize code and keep programs from becoming too complicated.

**[React](../../VOCABULARY_LIST.md#react):** A framework created by Facebook in 2013. It's built on the idea of components and is one of the most popular tools for making modern websites.

**[JSX](../../VOCABULARY_LIST.md#jsx):** A special syntax used in React. It looks like HTML but isn't exactly the same. JSX must be used inside React components.

**[Props (Properties)](../../VOCABULARY_LIST.md#props-properties):** Attributes you can give to components to make them more powerful. Props are like HTML attributes but for your own custom components.

**[State](../../VOCABULARY_LIST.md#state):** In React, component-local data that React preserves between renders so a component can remember information and update the UI (e.g., a click counter).

**[useState](../../VOCABULARY_LIST.md#usestate):** Hook that returns a state value and a setter. Initializes component state and triggers re-render when the setter is called.

**[Hook](../../VOCABULARY_LIST.md#hook):** Special React function whose name starts with `use` (e.g., `useState`, `useEffect`). Must follow the Rules of Hooks.

**[handleClick](../../VOCABULARY_LIST.md#handleclick):** Conventional camelCase name for a click event handler function.

**[Function](../../VOCABULARY_LIST.md#function):** In programming, reusable blocks of code that perform a specific task. They help organize code, avoid repetition, and make programs easier to understand.

**[Return](../../VOCABULARY_LIST.md#return):** In a React component function, the return statement sends back the JSX that should be shown on the screen.

**[Conditional Rendering](../../VOCABULARY_LIST.md#conditional-rendering):** Showing different UI based on a condition using JS expressions in JSX (e.g., `{isOn ? 'On' : 'Off'}`).

**[Ternary Operator](../../VOCABULARY_LIST.md#ternary-operator):** `condition ? exprIfTrue : exprIfFalse`; commonly used inside JSX for conditional rendering.

**[Event Listener](../../VOCABULARY_LIST.md#event-listener):** In web development, code that waits for something to happen (like a button click or a request) and then runs a function in response.

**[useEffect](../../VOCABULARY_LIST.md#useeffect):** Hook that runs code after a component renders. Commonly used to fetch data when a component first loads.

**[Async](../../VOCABULARY_LIST.md#async):** Keyword that creates asynchronous functions, allowing the use of `await` inside.

**[Await](../../VOCABULARY_LIST.md#await):** Keyword used inside async functions to wait for a promise to resolve before continuing.

**[Fetch](../../VOCABULARY_LIST.md#fetch):** JavaScript function that makes HTTP requests to APIs and returns a promise.

