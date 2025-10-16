# Kata 11: Count Items by Category

**Concept:** Reduce pattern to count (using for loop)

## Challenge

Create a `CategoryCount` component that:
1. Has an array of items with categories:
   ```javascript
   const items = [
     { name: 'Apple', category: 'Fruit' },
     { name: 'Carrot', category: 'Vegetable' },
     { name: 'Banana', category: 'Fruit' },
     { name: 'Broccoli', category: 'Vegetable' },
     { name: 'Orange', category: 'Fruit' }
   ];
   ```
2. Counts how many items are in each category using a **for loop**
3. Displays the counts

## Expected Output

```
Fruit: 3
Vegetable: 2
```

## Starter Code

```jsx
export default function CategoryCount() {
  const items = [
    { name: 'Apple', category: 'Fruit' },
    { name: 'Carrot', category: 'Vegetable' },
    { name: 'Banana', category: 'Fruit' },
    { name: 'Broccoli', category: 'Vegetable' },
    { name: 'Orange', category: 'Fruit' }
  ];
  
  // Count items by category using a for loop
  
  return (
    <div>
      {/* Display counts */}
    </div>
  );
}
```

## Hints

- Create variables to count each category: `let fruitCount = 0;`
- Loop through items and increment the appropriate counter
- Use if statements to check category

## Solution

<details>
<summary>Click to reveal solution</summary>

```jsx
export default function CategoryCount() {
  const items = [
    { name: 'Apple', category: 'Fruit' },
    { name: 'Carrot', category: 'Vegetable' },
    { name: 'Banana', category: 'Fruit' },
    { name: 'Broccoli', category: 'Vegetable' },
    { name: 'Orange', category: 'Fruit' }
  ];
  
  // REDUCE: Count items by category using a for loop
  let fruitCount = 0;
  let vegetableCount = 0;
  
  for (let i = 0; i < items.length; i++) {
    if (items[i].category === 'Fruit') {
      fruitCount = fruitCount + 1;
    } else if (items[i].category === 'Vegetable') {
      vegetableCount = vegetableCount + 1;
    }
  }
  
  return (
    <div>
      <p>Fruit: {fruitCount}</p>
      <p>Vegetable: {vegetableCount}</p>
    </div>
  );
}
```

</details>

## Concept Review
- **Reduce pattern**: Count items that meet criteria
- Start counters at 0
- Check condition and increment appropriate counter
- Can count multiple categories in one loop

## Challenge Variation

Try:
- Add a third category (e.g., 'Grain')
- Show the actual items in each category (combine with filter!)
- Calculate percentage of each category
- Find which category has the most items

