# Testing Details/Summary with markdown="1"

This file tests the `<details>` and `<summary>` elements with and without the `markdown="1"` attribute.

## Example 1: Without markdown="1"

<details>
<summary>Show Me: Counter Component (no markdown attribute)</summary>

<pre><code class="language-javascript">
import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    <>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </>
  );
}
</code></pre>

**Key points:**
- Uses `useState` hook
- Button updates state on click
- State persists across renders

</details>

## Example 2: With markdown="1"

<details>
<summary>Show Me: Counter Component (with markdown="1")</summary>

<pre><code class="language-javascript" markdown="1">
import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    <>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </>
  );
}
</code></pre>

**Key points:**
- Uses `useState` hook
- Button updates state on click
- State persists across renders

</details>

## Example 3: Without markdown="1" but with escaped HTML characters

<details>
<summary>Show Me: Counter Component (escaped HTML chars, no markdown)</summary>

<pre><code class="language-javascript">
import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    &lt;&gt;
      &lt;p&gt;Count: {count}&lt;/p&gt;
      &lt;button onClick={() =&gt; setCount(count + 1)}&gt;
        Increment
      &lt;/button&gt;
    &lt;/&gt;
  );
}
</code></pre>

**Key points:**
- Uses `useState` hook
- Button updates state on click
- State persists across renders

</details>

## Testing Notes

Compare how the code blocks and markdown formatting render in all three examples above:

1. **Example 1**: No markdown attribute, unescaped HTML (may be parsed as HTML)
2. **Example 2**: With `markdown="1"` attribute (processes content as markdown)
3. **Example 3**: No markdown attribute, escaped HTML characters (`&lt;`, `&gt;`, `=&gt;`) - safe for display

The `markdown="1"` attribute tells some markdown processors to process the content inside as markdown. Escaped HTML characters ensure the code displays correctly without being interpreted as HTML tags.