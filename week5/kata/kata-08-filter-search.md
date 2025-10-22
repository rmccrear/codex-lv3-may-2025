# Kata 8: Search/Filter Names

**Concept:** Filter pattern with strings (using for loop)

## Challenge

Create a `SearchNames` component that:
1. Has an array of names: `['Alice', 'Bob', 'Charlie', 'David', 'Eve']`
2. Has a text input for search
3. Filters and displays only names that include the search text (case-insensitive)
4. Uses a **for loop** for filtering

## Expected Behavior

When user types "a":
<pre><code>Search: [input showing: a]
Results: Alice, Charlie, David</code></pre>

When user types "e":
<pre><code>Search: [input showing: e]
Results: Alice, Charlie, Eve</code></pre>

## Starter Code

<pre><code class="language-jsx">import { useState } from &#x27;react&#x27;;

export default function SearchNames() {
  const names = [&#x27;Alice&#x27;, &#x27;Bob&#x27;, &#x27;Charlie&#x27;, &#x27;David&#x27;, &#x27;Eve&#x27;];
  const [search, setSearch] = useState(&#x27;&#x27;);
  
  // Filter names using a for loop
  
  return (
    &lt;div&gt;
      {/* Add search input */}
      {/* Display filtered results */}
    &lt;/div&gt;
  );
}</code></pre>

## Hints

- Use `.toLowerCase()` for case-insensitive search
- Use `.includes()` to check if name contains search text
- If search is empty, show all names

## Solution

<details>
<summary>Click to reveal solution</summary>

<pre><code class="language-jsx">import { useState } from &#x27;react&#x27;;

export default function SearchNames() {
  const names = [&#x27;Alice&#x27;, &#x27;Bob&#x27;, &#x27;Charlie&#x27;, &#x27;David&#x27;, &#x27;Eve&#x27;];
  const [search, setSearch] = useState(&#x27;&#x27;);
  
  // FILTER: Find names matching search using a for loop
  const filtered = [];
  for (let i = 0; i &lt; names.length; i++) {
    const nameLower = names[i].toLowerCase();
    const searchLower = search.toLowerCase();
    
    if (nameLower.includes(searchLower)) {
      filtered.push(names[i]);
    }
  }
  
  return (
    &lt;div&gt;
      &lt;input 
        type=&quot;text&quot;
        value={search}
        onChange={(e) =&gt; setSearch(e.target.value)}
        placeholder=&quot;Search names...&quot;
      /&gt;
      &lt;p&gt;Results: {filtered.join(&#x27;, &#x27;)}&lt;/p&gt;
    &lt;/div&gt;
  );
}</code></pre>

</details>

## Concept Review
- **Filter pattern**: Select items that match a condition
- `.toLowerCase()` makes search case-insensitive
- `.includes()` checks if string contains substring
- Empty search matches all items (all names include "")
- This follows the **List Filter Pattern** from Code.org - see [Code.org List Filter Pattern](https://studio.code.org/docs/concepts/patterns/list-filter-pattern/)

**Note:** Learn more about the built-in `.filter()` method at [MDN: Array.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)

## Challenge Variation

Try:
- Show "No results found" when filtered array is empty
- Add a count: "Found 3 results"
- Filter products, movies, or other data types

