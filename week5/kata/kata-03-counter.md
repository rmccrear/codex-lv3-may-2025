# Kata 3: Click Counter

**Concept:** useState and event handling

## Challenge

Create a `Counter` component that:
1. Displays a count starting at 0
2. Has a button that says "Click me!"
3. Increases the count by 1 each time the button is clicked

## Expected Behavior

- Initial display: "Count: 0"
- After 1 click: "Count: 1"
- After 3 clicks: "Count: 3"

## Starter Code

```jsx
import { useState } from 'react';

export default function Counter() {
  // Create state here
  
  // Create handler function here
  
  return (
    <div>
      {/* Display count */}
      {/* Add button */}
    </div>
  );
}
```

## Solution

<details>
<summary>Click to reveal solution</summary>

```jsx
import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  
  function handleClick() {
    setCount(count + 1);
  }
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={handleClick}>Click me!</button>
    </div>
  );
}
```

</details>

## Concept Review
- `useState(0)` creates state with initial value 0
- `const [count, setCount]` - count is current value, setCount updates it
- Never update state directly - always use the setter function
- `onClick={handleClick}` passes the function (no parentheses!)

