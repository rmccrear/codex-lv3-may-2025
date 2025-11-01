# Kata 14: Fetch All Pokemon and Display Names and Height

**Concept:** Map pattern with fetched array data (using for loop)

## Challenge

Create a `PokemonList` component that:
1. Fetches all pokemon from: `https://pokeapi.co/api/v2/pokemon?limit=20`
2. The response has a `results` array with pokemon data
3. Each pokemon in `results` needs to be fetched individually (use `results[i].url`)
4. Use a **for loop** to map over all pokemon and collect their names and heights
5. Display a list showing each pokemon's name and height

**🔗 [Practice on CodeSandbox](https://codesandbox.io/)**

## Expected Output

Displays a list like:
<pre><code>Pokemon List:
- bulbasaur: height 7
- ivysaur: height 10
- venusaur: height 20
... (and more)</code></pre>

## Starter Code

<pre><code class="language-jsx">import { useState, useEffect } from 'react';

export default function PokemonList() {
  const [pokemonList, setPokemonList] = useState([]);
  
  useEffect(() => {
    async function fetchAllPokemon() {
      // Step 1: Fetch list of pokemon
      const response = await fetch('https://pokeapi.co/api/v2/pokemon?limit=20');
      const data = await response.json();
      
      // Step 2: MAP: Fetch each pokemon and extract name/height using for loop
      const pokemonData = [];
      // Your for loop here
      
      setPokemonList(pokemonData);
    }
    
    fetchAllPokemon();
  }, []);
  
  if (pokemonList.length === 0) {
    return &lt;div&gt;Loading...&lt;/div&gt;;
  }
  
  return (
    &lt;div&gt;
      &lt;h3&gt;Pokemon List:&lt;/h3&gt;
      &lt;ul&gt;
        {pokemonList.map((pokemon, index) => (
          &lt;li key={index}&gt;{pokemon.name}: height {pokemon.height}&lt;/li&gt;
        ))}
      &lt;/ul&gt;
    &lt;/div&gt;
  );
}</code></pre>

## Hints

- First fetch gets list: `data.results` is an array
- Each result has a `url` property: `data.results[i].url`
- Inside the loop, fetch each pokemon: `await fetch(data.results[i].url)`
- Parse each response: `await response.json()`
- Store data objects: `pokemonData.push({ name: pokemon.name, height: pokemon.height })`
- Use `.map()` in JSX to render: `pokemonList.map((pokemon, index) => ...)`
- Use `Promise.all()` is optional but helps with performance

## Solution

<details>
<summary>Click to reveal solution</summary>

<pre><code class="language-jsx">import { useState, useEffect } from 'react';

export default function PokemonList() {
  const [pokemonList, setPokemonList] = useState([]);
  
  useEffect(() => {
    async function fetchAllPokemon() {
      // Step 1: Fetch list of pokemon
      const response = await fetch('https://pokeapi.co/api/v2/pokemon?limit=20');
      const data = await response.json();
      
      // Step 2: MAP: Fetch each pokemon and extract name/height using for loop
      const pokemonData = [];
      for (let i = 0; i &lt; data.results.length; i++) {
        const pokemonResponse = await fetch(data.results[i].url);
        const pokemon = await pokemonResponse.json();
        pokemonData.push({
          name: pokemon.name,
          height: pokemon.height
        });
      }
      
      setPokemonList(pokemonData);
    }
    
    fetchAllPokemon();
  }, []);
  
  if (pokemonList.length === 0) {
    return &lt;div&gt;Loading...&lt;/div&gt;;
  }
  
  return (
    &lt;div&gt;
      &lt;h3&gt;Pokemon List:&lt;/h3&gt;
      &lt;ul&gt;
        {pokemonList.map((pokemon, index) => (
          &lt;li key={index}&gt;{pokemon.name}: height {pokemon.height}&lt;/li&gt;
        ))}
      &lt;/ul&gt;
    &lt;/div&gt;
  );
}</code></pre>

</details>

## Concept Review

### Using For Loop for Data Transformation

- **Map pattern with for loop**: Transform each item to create a new array with different structure
- Loop through `data.results` array using a for loop
- For each result, fetch the full pokemon data
- Extract and transform data: `{ name: ..., height: ... }`
- Push transformed objects into new array: `pokemonData.push({ name: pokemon.name, height: pokemon.height })`
- Store the transformed data in state
- This is the **List Scrolling Pattern** from Code.org - see [Code.org List Scrolling Pattern](https://studio.code.org/docs/concepts/patterns/list-scrolling-pattern/)
- **Using for loop**: Good for practice and keeping sharp with list patterns. This helps you understand what's happening under the hood and reinforces the fundamental pattern.

### Using .map() Method for Rendering

- **Built-in `.map()` method**: Transform array items into JSX elements for display
- Used in the JSX return: `pokemonList.map((pokemon, index) => <li>...</li>)`
- A popular shorthand alternative in React that can be used directly in JSX
- Cleaner and more concise than a for loop for rendering
- Automatically handles creating an array of JSX elements
- The `.map()` method is the built-in JavaScript way to do the map pattern

### Why Use Both?

- **For loop in useEffect**: Good for algorithmically transforming data in. Also great for practice and understanding the underlying pattern.
- **.map() in JSX**: Ideal for rendering because it's clean, readable, and React-optimized. This is the popular shorthand you'll see in most React code.
- Storing data (not JSX) in state allows you to manipulate/filter/sort the data before rendering

**Note:** Learn more about the built-in `.map()` method at [MDN: Array.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

## Challenge Variation

Try:
- Fetch more pokemon: change `limit=20` to `limit=50`
- Add weight to the display
- Sort pokemon by height
- Group pokemon by type

---

**← [Back to Kata Index](./README.md)**

