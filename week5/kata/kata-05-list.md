# Kata 5: Fruit List

**Concept:** Array .map() to render lists

## Challenge

Create a `FruitList` component that:
1. Has an array of fruits: `['Apple', 'Banana', 'Orange', 'Grape']`
2. Displays them as an unordered list (`<ul>`) with list items (`<li>`)
3. Uses `.map()` to render the list items

## Expected Output

```
• Apple
• Banana
• Orange
• Grape
```

## Starter Code

```jsx
export default function FruitList() {
  const fruits = ['Apple', 'Banana', 'Orange', 'Grape'];
  
  return (
    <ul>
      {/* Use .map() here */}
    </ul>
  );
}
```

## Hints

- Use `.map()` to transform each fruit into an `<li>` element
- Remember to add a `key` prop to each `<li>`
- Syntax: `{fruits.map((fruit, index) => <li key={index}>{fruit}</li>)}`

## Solution

<details>
<summary>Click to reveal solution</summary>

```jsx
export default function FruitList() {
  const fruits = ['Apple', 'Banana', 'Orange', 'Grape'];
  
  return (
    <ul>
      {fruits.map((fruit, index) => (
        <li key={index}>{fruit}</li>
      ))}
    </ul>
  );
}
```

</details>

## Concept Review
- `.map()` transforms each item in an array
- Each rendered item needs a unique `key` prop
- Use `index` as key when items don't have unique IDs
- Wrap the map in curly braces `{}` to embed in JSX

