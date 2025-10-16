# Kata 10: Calculate Average Rating

**Concept:** Reduce pattern to find average (using for loop)

## Challenge

Create an `AverageRating` component that:
1. Has an array of product ratings: `[4.5, 5.0, 3.5, 4.0, 4.5, 5.0]`
2. Calculates the average rating using a **for loop**
3. Displays the average rounded to 1 decimal place
4. Shows a star rating (⭐ for each full star)

## Expected Output

```
Ratings: 4.5, 5.0, 3.5, 4.0, 4.5, 5.0
Average: 4.4
⭐⭐⭐⭐
```

## Starter Code

```jsx
export default function AverageRating() {
  const ratings = [4.5, 5.0, 3.5, 4.0, 4.5, 5.0];
  
  // Calculate average using a for loop
  
  // Create star display
  
  return (
    <div>
      {/* Display ratings, average, and stars */}
    </div>
  );
}
```

## Hints

- Sum all ratings first, then divide by array length
- Use `.toFixed(1)` to round to 1 decimal place
- Use `Math.round()` to get full star count
- Use `.repeat()` to repeat star emoji

## Solution

<details>
<summary>Click to reveal solution</summary>

```jsx
export default function AverageRating() {
  const ratings = [4.5, 5.0, 3.5, 4.0, 4.5, 5.0];
  
  // REDUCE: Sum all ratings using a for loop
  let total = 0;
  for (let i = 0; i < ratings.length; i++) {
    total = total + ratings[i];
  }
  
  // Calculate average
  const average = total / ratings.length;
  
  // Create star display (rounded to nearest whole number)
  const starCount = Math.round(average);
  const stars = '⭐'.repeat(starCount);
  
  return (
    <div>
      <p>Ratings: {ratings.join(', ')}</p>
      <p>Average: {average.toFixed(1)}</p>
      <p>{stars}</p>
    </div>
  );
}
```

</details>

## Concept Review
- **Reduce pattern**: Summarize array into single value (average)
- Sum all values first, then calculate average
- `.toFixed(1)` formats number to 1 decimal place
- `Math.round()` rounds to nearest integer
- `.repeat(n)` repeats string n times

## Challenge Variation

Try:
- Show half stars for .5 ratings (⭐ vs ⚝)
- Add a rating input to add new ratings
- Calculate median instead of average
- Show "Excellent!" if average > 4.5

