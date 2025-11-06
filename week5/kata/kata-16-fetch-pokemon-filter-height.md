# Kata 16: Fetch All Pokemon and Filter by Height

**Concept:** Filter pattern with fetched data (using for loop), then map to display

## Challenge

Create a `FilterPokemonByHeight` component that:
1. Fetches 20 pokemon from: `https://pokeapi.co/api/v2/pokemon?limit=20`
2. Fetches each pokemon's details (like Kata 15)
3. Uses a **for loop** to filter pokemon where height is greater than 10
4. Stores the filtered pokemon in state
5. Uses `.map()` in JSX to display the filtered pokemon names

**🔗 [Practice on CodeSandbox](https://codesandbox.io/)**

## Expected Output

Displays only pokemon with height > 10:
<pre><code>Pokemon with height > 10:
- venusaur
- charizard
- blastoise
... (only tall pokemon)</code></pre>

## Starter Code

<pre><code class="language-jsx">import { useState, useEffect } from 'react';

export default function FilterPokemonByHeight() {
  const [filteredPokemon, setFilteredPokemon] = useState([]);
  
  useEffect(() => {
    async function fetchAndFilterPokemon() {
      // Step 1: Fetch list of pokemon
      const response = await fetch('https://pokeapi.co/api/v2/pokemon?limit=20');
      const data = await response.json();
      
      // Step 2: Fetch all pokemon details (same as Kata 15)
      const allPokemon = [];
      for (let i = 0; i &lt; data.results.length; i++) {
        const pokemonResponse = await fetch(data.results[i].url);
        const pokemon = await pokemonResponse.json();
        allPokemon.push(pokemon);
      }
      
      // Step 3: FILTER: Select only pokemon with height > 10 using for loop
      const tallPokemon = [];
      // Your filter for loop here
      
      setFilteredPokemon(tallPokemon);
    }
    
    fetchAndFilterPokemon();
  }, []);
  
  if (filteredPokemon.length === 0) {
    return &lt;div&gt;Loading...&lt;/div&gt;;
  }
  
  return (
    &lt;div&gt;
      &lt;h3&gt;Pokemon with height &gt; 10:&lt;/h3&gt;
      &lt;ul&gt;
        {filteredPokemon.map((pokemon, index) => (
          &lt;li key={index}&gt;{pokemon.name}&lt;/li&gt;
        ))}
      &lt;/ul&gt;
    &lt;/div&gt;
  );
}</code></pre>

## Hints

- First, fetch 20 pokemon (like Kata 14)
- FILTER loop: `for (let i = 0; i < allPokemon.length; i++)`
- Check condition: `if (allPokemon[i].height > 10)`
- Push matching pokemon: `tallPokemon.push(allPokemon[i])`
- Store filtered pokemon objects in state
- Use `.map()` in JSX to render: `filteredPokemon.map((pokemon, index) => ...)`

## Solution

<details>
<summary>Click to reveal solution</summary>

<pre><code class="language-jsx">import { useState, useEffect } from 'react';

export default function FilterPokemonByHeight() {
  const [filteredPokemon, setFilteredPokemon] = useState([]);
  
  useEffect(() => {
    async function fetchAndFilterPokemon() {
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
      
      // Step 3: FILTER: Select only pokemon with height > 10 using for loop
      const tallPokemon = [];
      for (let i = 0; i &lt; allPokemon.length; i++) {
        if (allPokemon[i].height &gt; 10) {
          tallPokemon.push(allPokemon[i]);
        }
      }
      
      setFilteredPokemon(tallPokemon);
    }
    
    fetchAndFilterPokemon();
  }, []);
  
  if (filteredPokemon.length === 0) {
    return &lt;div&gt;Loading...&lt;/div&gt;;
  }
  
  return (
    &lt;div&gt;
      &lt;h3&gt;Pokemon with height &gt; 10:&lt;/h3&gt;
      &lt;ul&gt;
        {filteredPokemon.map((pokemon, index) => (
          &lt;li key={index}&gt;{pokemon.name}&lt;/li&gt;
        ))}
      &lt;/ul&gt;
    &lt;/div&gt;
  );
}</code></pre>

</details>

## Concept Review

### Using For Loop for Filtering

- **Filter pattern with for loop**: Select items matching a condition (`height > 10`)
- Loop through `allPokemon` array using a for loop
- Check condition: `if (allPokemon[i].height > 10)`
- Push matching pokemon into new array: `tallPokemon.push(allPokemon[i])`
- Store the filtered pokemon objects in state
- This is the **List Filter Pattern** from Code.org - see [Code.org List Filter Pattern](https://studio.code.org/docs/concepts/patterns/list-filter-pattern/)
- **Using for loop**: Good for practice and keeping sharp with list patterns. This helps you understand what's happening under the hood and reinforces the fundamental pattern.

### Using .map() Method for Rendering

- **Built-in `.map()` method**: Transform array items into JSX elements for display
- Used in the JSX return: `filteredPokemon.map((pokemon, index) => <li>...</li>)`
- A popular shorthand alternative in React that can be used directly in JSX
- Cleaner and more concise than a for loop for rendering
- Automatically handles creating an array of JSX elements
- Access pokemon name: `pokemon.name`

### Why Use Both?

- **For loop in useEffect**: Good for algorithmically filtering data. Also great for practice and understanding the underlying pattern.
- **.map() in JSX**: Ideal for rendering because it's clean, readable, and React-optimized. This is the popular shorthand you'll see in most React code.
- Storing filtered pokemon objects (not just names) in state allows you to access other properties if needed

**Note:** Learn more about:
- Built-in `.filter()` method: [MDN: Array.filter()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
- Built-in `.map()` method: [MDN: Array.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

## Challenge Variation

Try filtering by:
- Weight instead of height
- Multiple conditions: `height > 10 && weight > 100`
- Display both name and height after filtering
- Filter pokemon with specific types

---

**← [Back to Kata Index](./README.md)**

