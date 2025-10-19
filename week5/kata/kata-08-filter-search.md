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
```
Search: [input showing: a]
Results: Alice, Charlie, David
```

When user types "e":
```
Search: [input showing: e]
Results: Alice, Charlie, Eve
```

## Starter Code

```jsx
import { useState } from 'react';

export default function SearchNames() {
  const names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve'];
  const [search, setSearch] = useState('');
  
  // Filter names using a for loop
  
  return (
    <div>
      {/* Add search input */}
      {/* Display filtered results */}
    </div>
  );
}
```

## Hints

- Use `.toLowerCase()` for case-insensitive search
- Use `.includes()` to check if name contains search text
- If search is empty, show all names

## Solution

<details>
<summary>Click to reveal solution</summary>

```jsx
import { useState } from 'react';

export default function SearchNames() {
  const names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve'];
  const [search, setSearch] = useState('');
  
  // FILTER: Find names matching search using a for loop
  const filtered = [];
  for (let i = 0; i < names.length; i++) {
    const nameLower = names[i].toLowerCase();
    const searchLower = search.toLowerCase();
    
    if (nameLower.includes(searchLower)) {
      filtered.push(names[i]);
    }
  }
  
  return (
    <div>
      <input 
        type="text"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Search names..."
      />
      <p>Results: {filtered.join(', ')}</p>
    </div>
  );
}
```

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

