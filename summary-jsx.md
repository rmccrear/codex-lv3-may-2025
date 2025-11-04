# Testing Details/Summary with JSX Permutations

This file tests all permutations of `&lt;details&gt;` and `&lt;summary&gt;` elements with JSX (React) examples.

**Note:** Examples with unescaped JSX and `&lt;pre&gt;&lt;code&gt;` tags will likely not work correctly - the unescaped JSX gets parsed as actual HTML elements instead of displaying as code.

## Example 1: &lt;pre&gt;&lt;code class="..."&gt; escaped JSX

<details>
<summary>Show Me: React Counter Component (pre+code with class, escaped)</summary>

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

**Configuration:** `&lt;pre&gt;&lt;code class="language-javascript"&gt;` with escaped JSX

</details>

## Example 2: &lt;pre&gt;&lt;code class="..." markdown="1"&gt; unescaped JSX

<details>
<summary>Show Me: React Counter Component (pre+code with class and markdown="1", unescaped)</summary>

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

**Configuration:** `&lt;pre&gt;&lt;code class="language-javascript" markdown="1"&gt;` with unescaped JSX

</details>

## Example 3: &lt;pre&gt;&lt;code&gt; escaped JSX (no class)

<details>
<summary>Show Me: React Counter Component (pre+code, no class, escaped)</summary>

<pre><code>
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

**Configuration:** `&lt;pre&gt;&lt;code&gt;` (no class) with escaped JSX

</details>

## Example 4: &lt;pre class="..."&gt; no code tag, with unescaped JSX

<details>
<summary>Show Me: React Counter Component (pre with class, no code tag, unescaped)</summary>

<pre class="language-javascript">
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
</pre>

**Configuration:** `&lt;pre class="language-javascript"&gt;` (no code element) with unescaped JSX

</details>

## Example 5: &lt;pre class="..."&gt; no code tag, with escaped JSX

<details>
<summary>Show Me: React Counter Component (pre with class, no code tag, escaped)</summary>

<pre class="language-javascript">
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
</pre>

**Configuration:** `&lt;pre class="language-javascript"&gt;` (no code element) with escaped JSX

</details>

## Example 6: &lt;pre&gt; no code tag, with unescaped JSX

<details>
<summary>Show Me: React Counter Component (pre only, no class, no code tag, unescaped)</summary>

<pre>
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
</pre>

**Configuration:** `&lt;pre&gt;` (no class, no code) with unescaped JSX

</details>

## Example 7: &lt;pre&gt; no code tag, with escaped JSX

<details>
<summary>Show Me: React Counter Component (pre only, no class, no code tag, escaped)</summary>

<pre>
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
</pre>

**Configuration:** `&lt;pre&gt;` (no class, no code) with escaped JSX

</details>

## Example 8: Triple backticks with language, unescaped JSX

<details>
<summary>Show Me: React Counter Component (triple backticks with language, unescaped)</summary>

```javascript
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
```

**Configuration:** Triple backticks with language tag, unescaped JSX

</details>

## Example 9: Triple backticks with language, escaped JSX

<details>
<summary>Show Me: React Counter Component (triple backticks with language, escaped)</summary>

```javascript
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
```

**Configuration:** Triple backticks with language tag, escaped JSX

</details>

## Example 10: Triple backticks without language, unescaped JSX

<details>
<summary>Show Me: React Counter Component (triple backticks, no language, unescaped)</summary>

```
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
```

**Configuration:** Triple backticks without language tag, unescaped JSX

</details>

## Example 11: Triple backticks without language, escaped JSX

<details>
<summary>Show Me: React Counter Component (triple backticks, no language, escaped)</summary>

```
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
```

**Configuration:** Triple backticks without language tag, escaped JSX

</details>

## Testing Notes

All examples use **JSX (React)** with the same counter functionality. Compare how each renders:

**Permutations tested:**

**HTML `&lt;pre&gt;` tags:**
1. `&lt;pre&gt;&lt;code class="..."&gt;` escaped JSX
2. `&lt;pre&gt;&lt;code class="..." markdown="1"&gt;` unescaped JSX
3. `&lt;pre&gt;&lt;code&gt;` escaped JSX (no class)
4. `&lt;pre class="..."&gt;` no code tag, with unescaped JSX
5. `&lt;pre class="..."&gt;` no code tag, with escaped JSX
6. `&lt;pre&gt;` no code tag, with unescaped JSX
7. `&lt;pre&gt;` no code tag, with escaped JSX

**Markdown triple backticks:**
8. Triple backticks with language tag, unescaped JSX
9. Triple backticks with language tag, escaped JSX
10. Triple backticks without language tag, unescaped JSX
11. Triple backticks without language tag, escaped JSX

**Key variables:**
- **HTML vs Markdown syntax** (`&lt;pre&gt;` tags vs triple backticks)
- **With/without `&lt;code&gt;` element**
- **With/without `class` attribute (or language tag)**
- **With/without `markdown="1"` attribute**
- **Escaped vs unescaped JSX**

The `markdown="1"` attribute tells some markdown processors to process the content inside as markdown. Escaped JSX characters (`&lt;`, `&gt;`, `=&gt;`) ensure the code displays correctly without being interpreted as HTML tags or JSX syntax.


