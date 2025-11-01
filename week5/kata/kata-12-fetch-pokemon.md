# Kata 12: Fetch and Display Pokemon

**Concept:** Async/await with fetch API

## Challenge

Create a `PokemonDisplay` component that:
1. Uses `useState` to store a pokemon object
2. Uses `useEffect` to fetch a pokemon when the component loads
3. Fetches from: `https://pokeapi.co/api/v2/pokemon/pikachu`
4. Displays the pokemon's **name**, **weight**, and **height**

**🔗 [Practice on CodeSandbox](https://codesandbox.io/)**

## Expected Output

When the component loads, it should fetch and display:
<pre><code>Name: pikachu
Weight: 60
Height: 4</code></pre>

## Starter Code

<pre><code class="language-jsx">import { useState, useEffect } from 'react';

export default function PokemonDisplay() {
  const [pokemon, setPokemon] = useState(null);
  
  useEffect(() => {
    // Fetch pokemon using async/await
    // Store result in state
  }, []);
  
  if (!pokemon) {
    return &lt;div&gt;Loading...&lt;/div&gt;;
  }
  
  return (
    &lt;div&gt;
      {/* Display name, weight, and height */}
    &lt;/div&gt;
  );
}</code></pre>

## Hints

- Create an `async` function inside `useEffect`
- Use `fetch()` with the API URL
- Use `await response.json()` to parse JSON
- The pokemon object has: `name`, `weight`, `height` properties
- Call `setPokemon()` with the fetched data

## Solution

<details>
<summary>Click to reveal solution</summary>

<pre><code class="language-jsx">import { useState, useEffect } from 'react';

export default function PokemonDisplay() {
  const [pokemon, setPokemon] = useState(null);
  
  useEffect(() => {
    async function fetchPokemon() {
      const response = await fetch('https://pokeapi.co/api/v2/pokemon/pikachu');
      const data = await response.json();
      setPokemon(data);
    }
    
    fetchPokemon();
  }, []);
  
  if (!pokemon) {
    return &lt;div&gt;Loading...&lt;/div&gt;;
  }
  
  return (
    &lt;div&gt;
      &lt;p&gt;Name: {pokemon.name}&lt;/p&gt;
      &lt;p&gt;Weight: {pokemon.weight}&lt;/p&gt;
      &lt;p&gt;Height: {pokemon.height}&lt;/p&gt;
    &lt;/div&gt;
  );
}</code></pre>

</details>

## Concept Review

- **Async/await**: Clean way to handle asynchronous operations
- `async function` allows using `await` inside
- `await fetch()` waits for the HTTP request to complete
- `await response.json()` waits for JSON parsing
- Use `useState` to store fetched data
- Use `useEffect` to fetch data when component loads
- Show loading state while data is being fetched

---

**← [Back to Kata Index](./README.md)**

