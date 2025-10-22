# Kata 6: Name Input

**Concept:** useState with text input

## Challenge

Create a `NameInput` component that:
1. Has a text input field
2. Has text below that says "Your name is: [entered name]"
3. Updates in real-time as the user types

## Expected Behavior

When user types "Ash":
<pre><code>[text input showing: Ash]
Your name is: Ash</code></pre>

## Starter Code

<pre><code class="language-jsx">import { useState } from &#x27;react&#x27;;

export default function NameInput() {
  // Create state for name
  
  // Create handler for input change
  
  return (
    &lt;div&gt;
      {/* Add input */}
      {/* Display name */}
    &lt;/div&gt;
  );
}</code></pre>

## Hints

- Use `value={name}` on the input to control it
- Use `onChange={handleChange}` to update state
- Access input value with `event.target.value`

## Solution

<details>
<summary>Click to reveal solution</summary>

<pre><code class="language-jsx">import { useState } from &#x27;react&#x27;;

export default function NameInput() {
  const [name, setName] = useState(&#x27;&#x27;);
  
  function handleChange(event) {
    setName(event.target.value);
  }
  
  return (
    &lt;div&gt;
      &lt;input 
        type=&quot;text&quot; 
        value={name} 
        onChange={handleChange}
        placeholder=&quot;Enter your name&quot;
      /&gt;
      &lt;p&gt;Your name is: {name}&lt;/p&gt;
    &lt;/div&gt;
  );
}</code></pre>

</details>

## Concept Review
- Controlled inputs: React controls the input value via state
- `onChange` event fires every time the input changes
- `event.target.value` gets the current input value
- State updates cause component to re-render with new value

