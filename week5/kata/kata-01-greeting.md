# Kata 1: Simple Greeting Component

**Concept:** Basic component and JSX

## Challenge

Create a React component called `Greeting` that displays "Hello, World!" in an `<h1>` tag.

## Expected Output

When rendered, it should display:
```
Hello, World!
```

## Starter Code

```jsx
export default function Greeting() {
  // Your code here
}
```

## Solution

<details>
<summary>Click to reveal solution</summary>

```jsx
export default function Greeting() {
  return <h1>Hello, World!</h1>;
}
```

</details>

## Concept Review
- Components are functions that return JSX
- Component names must start with a capital letter
- JSX looks like HTML but is actually JavaScript

