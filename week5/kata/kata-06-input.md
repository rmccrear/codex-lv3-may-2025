# Kata 6: Name Input

**Concept:** useState with text input

## Challenge

Create a `NameInput` component that:
1. Has a text input field
2. Has text below that says "Your name is: [entered name]"
3. Updates in real-time as the user types

## Expected Behavior

When user types "Ash":
```
[text input showing: Ash]
Your name is: Ash
```

## Starter Code

```jsx
import { useState } from 'react';

export default function NameInput() {
  // Create state for name
  
  // Create handler for input change
  
  return (
    <div>
      {/* Add input */}
      {/* Display name */}
    </div>
  );
}
```

## Hints

- Use `value={name}` on the input to control it
- Use `onChange={handleChange}` to update state
- Access input value with `event.target.value`

## Solution

<details>
<summary>Click to reveal solution</summary>

```jsx
import { useState } from 'react';

export default function NameInput() {
  const [name, setName] = useState('');
  
  function handleChange(event) {
    setName(event.target.value);
  }
  
  return (
    <div>
      <input 
        type="text" 
        value={name} 
        onChange={handleChange}
        placeholder="Enter your name"
      />
      <p>Your name is: {name}</p>
    </div>
  );
}
```

</details>

## Concept Review
- Controlled inputs: React controls the input value via state
- `onChange` event fires every time the input changes
- `event.target.value` gets the current input value
- State updates cause component to re-render with new value

