# Kata 4: Show/Hide Toggle

**Concept:** useState with boolean and conditional rendering

## Challenge

Create a `Toggle` component that:
1. Has a button that says "Show Message"
2. When clicked, displays "Hello! 👋" below the button
3. The button text changes to "Hide Message"
4. When clicked again, hides the message and button text returns to "Show Message"

## Expected Behavior

Initial state:
```
[Show Message]
```

After clicking:
```
[Hide Message]
Hello! 👋
```

## Starter Code

```jsx
import { useState } from 'react';

export default function Toggle() {
  // Create boolean state here
  
  // Create toggle function here
  
  return (
    <div>
      {/* Add button */}
      {/* Conditionally show message */}
    </div>
  );
}
```

## Hints

- Use ternary operator: `{isVisible ? "Hide Message" : "Show Message"}`
- Use `&&` operator: `{isVisible && <p>Hello! 👋</p>}`

## Solution

<details>
<summary>Click to reveal solution</summary>

```jsx
import { useState } from 'react';

export default function Toggle() {
  const [isVisible, setIsVisible] = useState(false);
  
  function handleToggle() {
    setIsVisible(!isVisible);
  }
  
  return (
    <div>
      <button onClick={handleToggle}>
        {isVisible ? "Hide Message" : "Show Message"}
      </button>
      {isVisible && <p>Hello! 👋</p>}
    </div>
  );
}
```

</details>

## Concept Review
- State can hold any type of value (boolean, string, number, array, object)
- `!isVisible` flips the boolean value
- Ternary operator: `condition ? trueValue : falseValue`
- `&&` operator: only renders if condition is true

