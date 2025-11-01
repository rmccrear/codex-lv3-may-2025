# Kata 16: Fetch All Pokemon and Calculate Total Weight

**Concept:** Reduce pattern with fetched data (using for loop)

## Challenge

Create a `PokemonTotalWeight` component that:
1. Fetches all pokemon from: `https://pokeapi.co/api/v2/pokemon?limit=20`
2. Fetches each pokemon's details (like Kata 14)
3. Uses a **for loop** to calculate the total weight of all pokemon (reduce pattern)
4. Displays the total weight and the count of pokemon

**🔗 [Practice on CodeSandbox](https://codesandbox.io/)**

## Expected Output

Displays:
<pre><code>Total Weight: 8500
Pokemon Count: 20</code></pre>

## Starter Code

<pre><code class="language-jsx">import { useState, useEffect } from 'react';

export default function PokemonTotalWeight() {
  const [totalWeight, setTotalWeight] = useState(0);
  const [count, setCount] = useState(0);
  
  useEffect(() => {
    async function fetchAndCalculateWeight() {
      // Step 1: Fetch list of pokemon
      const response = await fetch('https://pokeapi.co/api/v2/pokemon?limit=20');
      const data = await response.json();
      
      // Step 2: Fetch all pokemon details
      const allPokemon = [];
      for (let i = 0; i &lt; data.results.length; i++) {
        const pokemonResponse = await fetch(data.results[i].url);
        const pokemon = await pokemonResponse.json();
        allPokemon.push(pokemon);
      }
      
      // Step 3: REDUCE: Calculate total weight using for loop
      let total = 0;
      // Your reduce for loop here
      
      setTotalWeight(total);
      setCount(allPokemon.length);
    }
    
    fetchAndCalculateWeight();
  }, []);
  
  if (totalWeight === 0) {
    return &lt;div&gt;Loading...&lt;/div&gt;;
  }
  
  return (
    &lt;div&gt;
      {/* Display total weight and count */}
    &lt;/div&gt;
  );
}</code></pre>

## Hints

- Start with `let total = 0`
- Loop through `allPokemon` array
- Add each pokemon's weight: `total = total + allPokemon[i].weight`
- Or use shorthand: `total += allPokemon[i].weight`
- Set the total in state when done

## Solution

<details>
<summary>Click to reveal solution</summary>

<pre><code class="language-jsx">import { useState, useEffect } from 'react';

export default function PokemonTotalWeight() {
  const [totalWeight, setTotalWeight] = useState(0);
  const [count, setCount] = useState(0);
  
  useEffect(() => {
    async function fetchAndCalculateWeight() {
      // Step 1: Fetch list of pokemon
      const response = await fetch('https://pokeapi.co/api/v2/pokemon?limit=20');
      const data = await response.json();
      
      // Step 2: Fetch all pokemon details
      const allPokemon = [];
      for (let i = 0; i &lt; data.results.length; i++) {
        const pokemonResponse = await fetch(data.results[i].url);
        const pokemon = await pokemonResponse.json();
        allPokemon.push(pokemon);
      }
      
      // Step 3: REDUCE: Calculate total weight using for loop
      let total = 0;
      for (let i = 0; i &lt; allPokemon.length; i++) {
        total = total + allPokemon[i].weight;
      }
      
      setTotalWeight(total);
      setCount(allPokemon.length);
    }
    
    fetchAndCalculateWeight();
  }, []);
  
  if (totalWeight === 0) {
    return &lt;div&gt;Loading...&lt;/div&gt;;
  }
  
  return (
    &lt;div&gt;
      &lt;p&gt;Total Weight: {totalWeight}&lt;/p&gt;
      &lt;p&gt;Pokemon Count: {count}&lt;/p&gt;
    &lt;/div&gt;
  );
}</code></pre>

</details>

## Concept Review

### Using For Loop for Reduce Pattern

- **Reduce pattern**: Combine all items into a single value
- Start with initial value: `let total = 0`
- Loop through array and accumulate: `total += allPokemon[i].weight`
- This is the **List Patterns** from Code.org - see [Code.org List Patterns](https://studio.code.org/docs/concepts/patterns/list-patterns/)
- The built-in `.reduce()` method does this automatically

**Note:** Learn more about the built-in `.reduce()` method at [MDN: Array.reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)

### Understanding Pagination

- **Pagination**: Breaking large datasets into smaller, manageable chunks (pages)
- In this kata, we use `?limit=20` to fetch only 20 pokemon at a time
- The Pokemon API has over 1000 pokemon - fetching all at once would be slow and waste resources
- **Benefits of pagination**:
  - Faster initial load times
  - Reduces memory usage
  - Better user experience
  - More efficient for APIs and databases
- **Common pagination parameters**:
  - `limit`: Number of items per page (we use 20)
  - `offset`: Starting position for the next page (e.g., `?limit=20&offset=20` for page 2)
- **Real-world applications**: Most APIs use pagination - social media feeds, search results, product listings, etc.
- In a real app, you might add "Load More" buttons or infinite scroll to fetch additional pages

**Note:** To fetch more pokemon, you could modify the limit or implement pagination to fetch multiple pages sequentially

## Challenge Variation

Try calculating:
- Average weight: `total / allPokemon.length`
- Heaviest pokemon: track max weight in loop
- Lightest pokemon: track min weight in loop
- Total height instead of weight
- Weight of only heavy pokemon (filter + reduce)

---

**← [Back to Kata Index](./README.md)**

