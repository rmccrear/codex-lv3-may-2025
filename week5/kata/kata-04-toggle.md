# Kata 4: Show/Hide Toggle

**Concept:** useState with boolean and conditional rendering

## Challenge

Create a `Toggle` component that:
1. Has a button that says "Show Message"
2. When clicked, displays "Hello! 👋" below the button
3. The button text changes to "Hide Message"
4. When clicked again, hides the message and button text returns to "Show Message"

**🔗 [Practice on CodeSandbox](https://codesandbox.io/)**

## Expected Behavior

Initial state:
<pre><code>[Show Message]</code></pre>

After clicking:
<pre><code>[Hide Message]
Hello! 👋</code></pre>

## Starter Code

<pre><code class="language-jsx">import { useState } from &#x27;react&#x27;;

export default function Toggle() {
  // Create boolean state here
  
  // Create toggle function here
  
  return (
    &lt;div&gt;
      {/* Add button */}
      {/* Conditionally show message */}
    &lt;/div&gt;
  );
}</code></pre>

## Hints

- Use ternary operator: `{isVisible ? "Hide Message" : "Show Message"}`
- Use `&&` operator: `{isVisible && <p>Hello! 👋</p>}`

## Solution

<details>
<summary>Click to reveal solution</summary>

<pre><code class="language-jsx">import { useState } from &#x27;react&#x27;;

export default function Toggle() {
  const [isVisible, setIsVisible] = useState(false);
  
  function handleToggle() {
    setIsVisible(!isVisible);
  }
  
  return (
    &lt;div&gt;
      &lt;button onClick={handleToggle}&gt;
        {isVisible ? &quot;Hide Message&quot; : &quot;Show Message&quot;}
      &lt;/button&gt;
      {isVisible &amp;&amp; &lt;p&gt;Hello! 👋&lt;/p&gt;}
    &lt;/div&gt;
  );
}</code></pre>

</details>

## Concept Review
- State can hold any type of value (boolean, string, number, array, object)
- `!isVisible` flips the boolean value
- Ternary operator: `condition ? trueValue : falseValue`
- `&&` operator: only renders if condition is true

---

**← [Back to Kata Index](./README.md)**
