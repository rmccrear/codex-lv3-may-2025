# Kata 9: Calculate Total Score

**Concept:** Reduce pattern to sum numbers (using for loop)

## Challenge

Create a `TotalScore` component that:
1. Has an array of scores: `[85, 92, 78, 90, 88]`
2. Calculates the total sum of all scores using a **for loop**
3. Displays the individual scores and the total

**🔗 [Practice on CodeSandbox](https://codesandbox.io/)**

## Expected Output

<pre><code>Scores: 85, 92, 78, 90, 88
Total: 433</code></pre>

## Starter Code

<pre><code class="language-jsx">export default function TotalScore() {
  const scores = [85, 92, 78, 90, 88];
  
  // Calculate total using a for loop
  
  return (
    &lt;div&gt;
      {/* Display scores and total */}
    &lt;/div&gt;
  );
}</code></pre>

## Hints

- Start with `let total = 0`
- Loop through array and add each score to total
- `total = total + scores[i]` (or `total += scores[i]`)

## Solution

<details>
<summary>Click to reveal solution</summary>

<pre><code class="language-jsx">export default function TotalScore() {
  const scores = [85, 92, 78, 90, 88];
  
  // REDUCE: Sum all scores using a for loop
  let total = 0;
  for (let i = 0; i &lt; scores.length; i++) {
    total = total + scores[i];
  }
  
  return (
    &lt;div&gt;
      &lt;p&gt;Scores: {scores.join(&#x27;, &#x27;)}&lt;/p&gt;
      &lt;p&gt;Total: {total}&lt;/p&gt;
    &lt;/div&gt;
  );
}</code></pre>

</details>

## Concept Review
- **Reduce pattern**: Combine all items into a single value
- Start with initial value (0 for sum)
- Loop through array and accumulate result
- This is what `.reduce()` does under the hood!

**Note:** Learn more about the built-in `.reduce()` method at [MDN: Array.reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)

## Challenge Variation

Try calculating:
- Average score: `total / scores.length`
- Highest score: keep track of max value
- Lowest score: keep track of min value
- Count of passing scores (>= 80)

---

**← [Back to Kata Index](./README.md)**
