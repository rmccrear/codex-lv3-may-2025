Level Navigation: [1](./react-clicker-game-lv-1.md) | [2](./react-clicker-game-lv-2.md) | [3](./react-clicker-game-lv-3.md) | [4](./react-clicker-game-lv-4.md) | [5](./react-clicker-game-lv-5.md) | [6](./react-clicker-game-lv-6.md) | [7](./react-clicker-game-lv-7.md) | [8](./react-clicker-game-lv-8.md) | [9](./react-clicker-game-lv-9.md) | [10](./react-clicker-game-lv-10.md) | [11](./react-clicker-game-lv-11.md) | [12](./react-clicker-game-lv-12.md) | [13](./react-clicker-game-lv-13.md) | [14](./react-clicker-game-lv-14.md) | **15** | [16](./react-clicker-game-lv-16.md) | [17](./react-clicker-game-lv-17.md) | [18⚡](./react-clicker-game-lv-18.md) | [19](./react-clicker-game-lv-19.md)

# Level 15: Code Review and Understanding

**User Story:** As a developer, I want to understand every part of my code so that I can explain it and build on it.

## What You'll Do

Review your complete code and make sure you understand each concept.

## Key Concepts to Understand

### React Hooks - useState
```jsx
const [value, setValue] = useState(initialValue)
```
- **What it does:** Creates a state variable that persists between renders
- **Why we need it:** Regular variables reset on every render
- **How to update:** Always use the setter function (setValue)

### Event Handling
```jsx
<div onClick={handleClick}>Click me</div>
```
- **onClick:** Attaches event listener for clicks
- **event parameter:** Contains information about the click event
- **event.stopPropagation():** Prevents click from bubbling to parent

### Dynamic Styling
```jsx
const style = { width: "100px", backgroundColor: "red" }
<div style={style}>Styled</div>
```
- **Inline styles:** JavaScript objects with CSS properties
- **camelCase:** CSS properties use camelCase (backgroundColor not background-color)
- **Units:** Values need units as strings ("100px")

### Conditional Rendering
```jsx
{condition && <Component />}           // Render OR nothing
{condition ? <CompA /> : <CompB />}    // Render A OR B
```

### Random Numbers
```jsx
Math.floor(Math.random() * (max - min) + min)
```
- **Math.random():** Returns decimal 0-1
- **Multiply by range:** Scale to desired range
- **Add minimum:** Shift to starting point
- **Math.floor():** Round down to integer

## ✅ Check

Can you answer these questions?

1. **Why do we use `useState` instead of regular variables?**
   <details>
<summary>Answer</summary>

<p>Regular variables reset on every render. State persists and triggers re-renders.</p>

</details>

2. **Why do we need `event.stopPropagation()` in clickTarget?**
   <details>
<summary>Answer</summary>

<p>To prevent the click from bubbling up to the parent and triggering missTarget.</p>

</details>

3. **How does the ternary operator work in JSX?**
   <details>
<summary>Answer</summary>

<p>It evaluates a condition and renders one component if true, another if false.</p>

</details>

4. **Why are styles in camelCase instead of kebab-case?**
   <details>
<summary>Answer</summary>

<p>Because they're JavaScript object properties, not CSS. JavaScript uses camelCase.</p>

</details>

5. **How does `randomNumber(0, 400)` work?**
   <details>
<summary>Answer</summary>

<p>It generates a random integer from 0 to 399 (inclusive).</p>

</details>

---