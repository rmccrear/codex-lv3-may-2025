# Kata 7: Filter Even Numbers

**Concept:** Filter pattern with arrays (using for loop)

## Challenge

Create a `FilterEvens` component that:
1. Has an array of numbers: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
2. Filters out only the even numbers using a **for loop**
3. Displays the even numbers as a comma-separated list

## Expected Output

```
Even numbers: 2, 4, 6, 8, 10
```

## Starter Code

```jsx
export default function FilterEvens() {
  const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  
  // Filter even numbers using a for loop
  
  return (
    <div>
      {/* Display filtered numbers */}
    </div>
  );
}
```

## Hints

- Use a for loop to check each number
- Use `if (numbers[i] % 2 === 0)` to check if even
- Push even numbers into a new array
- Use `.join(', ')` to display as comma-separated string

## Solution

<details>
<summary>Click to reveal solution</summary>

```jsx
export default function FilterEvens() {
  const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  
  // FILTER: Select only even numbers using a for loop
  const evenNumbers = [];
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0) {
      evenNumbers.push(numbers[i]);
    }
  }
  
  return (
    <div>
      <p>Even numbers: {evenNumbers.join(', ')}</p>
    </div>
  );
}
```

</details>

## Concept Review
- **Filter pattern**: Loop through array and select items matching a condition
- Create empty array, check condition, push matching items
- `% 2 === 0` checks if number is divisible by 2 (even)
- This is the **List Filter Pattern** from Code.org - see [Code.org List Filter Pattern](https://studio.code.org/docs/concepts/patterns/list-filter-pattern/)
- The built-in `.filter()` method does this automatically

**Note:** Learn more about the built-in `.filter()` method at [MDN: Array.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)

## Challenge Variation

Try filtering for:
- Odd numbers (`% 2 !== 0`)
- Numbers greater than 5 (`numbers[i] > 5`)
- Numbers divisible by 3 (`numbers[i] % 3 === 0`)

