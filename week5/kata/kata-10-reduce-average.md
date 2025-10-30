# Kata 10: Calculate Average Rating

**Concept:** Reduce pattern to find average (using for loop)

## Challenge

Create an `AverageRating` component that:
1. Has an array of product ratings: `[4.5, 5.0, 3.5, 4.0, 4.5, 5.0]`
2. Calculates the average rating using a **for loop**
3. Displays the average rounded to 1 decimal place
4. Shows a star rating (⭐ for each full star)

**🔗 [Practice on CodeSandbox](https://codesandbox.io/)**

## Expected Output

<pre><code>Ratings: 4.5, 5.0, 3.5, 4.0, 4.5, 5.0
Average: 4.4
⭐⭐⭐⭐</code></pre>

## Starter Code

<pre><code class="language-jsx">export default function AverageRating() {
  const ratings = [4.5, 5.0, 3.5, 4.0, 4.5, 5.0];
  
  // Calculate average using a for loop
  
  // Create star display
  
  return (
    &lt;div&gt;
      {/* Display ratings, average, and stars */}
    &lt;/div&gt;
  );
}</code></pre>

## Hints

- Sum all ratings first, then divide by array length
- Use `.toFixed(1)` to round to 1 decimal place
- Use `Math.round()` to get full star count
- Use `.repeat()` to repeat star emoji

## Solution

<details>
<summary>Click to reveal solution</summary>

<pre><code class="language-jsx">export default function AverageRating() {
  const ratings = [4.5, 5.0, 3.5, 4.0, 4.5, 5.0];
  
  // REDUCE: Sum all ratings using a for loop
  let total = 0;
  for (let i = 0; i &lt; ratings.length; i++) {
    total = total + ratings[i];
  }
  
  // Calculate average
  const average = total / ratings.length;
  
  // Create star display (rounded to nearest whole number)
  const starCount = Math.round(average);
  const stars = &#x27;⭐&#x27;.repeat(starCount);
  
  return (
    &lt;div&gt;
      &lt;p&gt;Ratings: {ratings.join(&#x27;, &#x27;)}&lt;/p&gt;
      &lt;p&gt;Average: {average.toFixed(1)}&lt;/p&gt;
      &lt;p&gt;{stars}&lt;/p&gt;
    &lt;/div&gt;
  );
}</code></pre>

</details>

## Concept Review
- **Reduce pattern**: Summarize array into single value (average)
- Sum all values first, then calculate average
- `.toFixed(1)` formats number to 1 decimal place
- `Math.round()` rounds to nearest integer
- `.repeat(n)` repeats string n times

**Note:** Learn more about the built-in `.reduce()` method at [MDN: Array.reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)

## Challenge Variation

Try:
- Show half stars for .5 ratings (⭐ vs ⚝)
- Add a rating input to add new ratings
- Calculate median instead of average
- Show "Excellent!" if average > 4.5

---

**← [Back to Kata Index](./README.md)**
