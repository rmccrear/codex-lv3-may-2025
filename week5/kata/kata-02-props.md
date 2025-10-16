# Kata 2: Welcome Component with Props

**Concept:** Props and destructuring

## Challenge

Create a `Welcome` component that accepts a `name` prop and displays "Welcome, [name]!" in an `<h2>` tag.

Use **destructuring** to extract the `name` prop.

## Expected Usage

```jsx
<Welcome name="Ash" />
// Should display: Welcome, Ash!

<Welcome name="Misty" />
// Should display: Welcome, Misty!
```

## Starter Code

```jsx
export default function Welcome(/* add props here */) {
  // Your code here
}
```

## Solution

<details>
<summary>Click to reveal solution</summary>

```jsx
export default function Welcome({ name }) {
  return <h2>Welcome, {name}!</h2>;
}
```

</details>

## Concept Review
- Props are data passed from parent to child component
- Use `{ name }` to destructure props (modern React pattern)
- Use curly braces `{}` to embed JavaScript in JSX

