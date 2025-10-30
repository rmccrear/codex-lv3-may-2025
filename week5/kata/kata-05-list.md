# Kata 5: Fruit List

**Concept:** List pattern - displaying arrays in JSX

## Challenge

Create a `FruitList` component that:
1. Has an array of fruits: `['Apple', 'Banana', 'Orange', 'Grape']`
2. Displays them as an unordered list (`<ul>`) with list items (`<li>`)
3. Uses a **for loop** to build an array of JSX elements

**🔗 [Practice on CodeSandbox](https://codesandbox.io/)**

## Expected Output

<pre><code>• Apple
• Banana
• Orange
• Grape</code></pre>

## Starter Code

<pre><code class="language-jsx">export default function FruitList() {
  const fruits = [&#x27;Apple&#x27;, &#x27;Banana&#x27;, &#x27;Orange&#x27;, &#x27;Grape&#x27;];
  
  // Build array of list items using a for loop
  
  return (
    &lt;ul&gt;
      {/* Display the array of list items here */}
    &lt;/ul&gt;
  );
}</code></pre>

## Hints

- Create an empty array to store JSX elements: `const listItems = [];`
- Use a for loop to go through each fruit
- Push `<li>` elements into the array
- Remember to add a `key` prop to each `<li>`: `<li key={i}>{fruits[i]}</li>`
- Display the array in JSX using curly braces: `{listItems}`

## Solution

<details>
<summary>Click to reveal solution</summary>

<pre><code class="language-jsx">export default function FruitList() {
  const fruits = [&#x27;Apple&#x27;, &#x27;Banana&#x27;, &#x27;Orange&#x27;, &#x27;Grape&#x27;];
  
  // Build list items using a for loop
  const listItems = [];
  for (let i = 0; i &lt; fruits.length; i++) {
    listItems.push(&lt;li key={i}&gt;{fruits[i]}&lt;/li&gt;);
  }
  
  return (
    &lt;ul&gt;
      {listItems}
    &lt;/ul&gt;
  );
}</code></pre>

**Note:** You can also use `.map()` as a shortcut:
<pre><code class="language-jsx">{fruits.map((fruit, index) =&gt; &lt;li key={index}&gt;{fruit}&lt;/li&gt;)}</code></pre>

</details>

## Concept Review
- Use a for loop to build an array of JSX elements
- Each rendered item needs a unique `key` prop for React to track changes
- Push JSX elements into an array, then display the array in curly braces
- This is the foundation of the **List Pattern** - see [Code.org List Patterns](https://studio.code.org/docs/concepts/patterns/list-filter-pattern/)
- `.map()` is a built-in method that does this automatically

**Note:** Learn more about the built-in `.map()` method at [MDN: Array.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

---

**← [Back to Kata Index](./README.md)**
