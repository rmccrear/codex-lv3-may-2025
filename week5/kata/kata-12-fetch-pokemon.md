# Kata 12: Fetch and Display Pokemon

**Concept:** Promises with fetch API and data transformation

## Challenge

Create a `PokemonDisplay` component that:
1. Uses `useState` to store a simplified pokemon object
2. Uses `useEffect` to fetch a pokemon when the component loads
3. Fetches from: `https://pokeapi.co/api/v2/pokemon/pikachu`
4. Transforms the pokemon data to a simpler object: `{ name, height, weight, imgUrl }`
5. Uses a callback function defined **outside** the component in the `.then()` chain
6. Displays the pokemon's **name**, **weight**, **height**, and **image**

**🔗 [Practice on CodeSandbox](https://codesandbox.io/)**

## Expected Output

When the component loads, it should fetch and display:
<pre><code>Name: pikachu
Weight: 60
Height: 4
[Image of pikachu]</code></pre>

## Starter Code

<pre><code class="language-jsx">import { useState, useEffect } from 'react';

// Define callback function outside the component
function transformPokemon(pokemonData) {
  // Transform pokemonData to { name, height, weight, imgUrl }
  // Find the first image URL (usually in pokemonData.sprites.front_default)
}

export default function PokemonDisplay() {
  const [pokemon, setPokemon] = useState(null);
  
  useEffect(() => {
    // Fetch pokemon data here
  }, []);
  
  if (!pokemon) {
    return &lt;div&gt;Loading...&lt;/div&gt;;
  }
  
  return (
    &lt;div&gt;
      {/* Display name, weight, height, and image */}
    &lt;/div&gt;
  );
}</code></pre>

## Hints

- Use `fetch()` with the API URL - it returns a Promise
- Use `.then()` to handle the response
- Use `response.json()` to parse JSON - it also returns a Promise
- Define a `transformPokemon` function **outside** the component
- The transform function should return: `{ name, height, weight, imgUrl }`
- Find the image URL in `pokemonData.sprites.front_default`
- Chain `.then(transformPokemon)` to transform the data
- Chain `.then(setPokemon)` to store the transformed data
- Use `.catch()` to handle errors

## Solution

<details>
<summary>Click to reveal solution</summary>

<pre><code class="language-jsx">import { useState, useEffect } from 'react';

// Callback function defined outside the component
function transformPokemon(pokemonData) {
  return {
    name: pokemonData.name,
    height: pokemonData.height,
    weight: pokemonData.weight,
    imgUrl: pokemonData.sprites.front_default
  };
}

export default function PokemonDisplay() {
  const [pokemon, setPokemon] = useState(null);
  
  useEffect(() => {
    fetch('https://pokeapi.co/api/v2/pokemon/pikachu')
      .then(response => response.json())
      .then(transformPokemon)  // Use the callback function
      .then(pokemon => setPokemon(pokemon))  // Set the transformed data
      .catch(error => console.error('Error fetching pokemon:', error));
  }, []);
  
  if (!pokemon) {
    return &lt;div&gt;Loading...&lt;/div&gt;;
  }
  
  return (
    &lt;div&gt;
      &lt;p&gt;Name: {pokemon.name}&lt;/p&gt;
      &lt;p&gt;Weight: {pokemon.weight}&lt;/p&gt;
      &lt;p&gt;Height: {pokemon.height}&lt;/p&gt;
      {pokemon.imgUrl && &lt;img src={pokemon.imgUrl} alt={pokemon.name} /&gt;}
    &lt;/div&gt;
  );
}</code></pre>

</details>

## Concept Review

- **Promises**: Handle asynchronous operations with `.then()` and `.catch()`
- `fetch()` returns a Promise that resolves to a Response object
- `response.json()` returns a Promise that resolves to parsed JSON data
- Chain `.then()` calls to handle each step of the async operation
- **Callbacks**: Functions passed to `.then()` can be defined outside the component
- **Data Transformation**: Convert complex API responses to simpler objects your component needs
- Use `.catch()` to handle errors
- Use `useState` to store fetched data
- Use `useEffect` to fetch data when component loads
- Show loading state while data is being fetched
- Extract only the data you need from API responses

## Variations & Extensions

Try modifying your `transformPokemon` function to include or exclude different properties:

### Add More Properties
- **`id`**: `pokemonData.id` - The Pokemon's unique ID number
- **`types`**: `pokemonData.types.map(t => t.type.name)` - Array of type names (e.g., `['electric']`)
- **`abilities`**: `pokemonData.abilities.map(a => a.ability.name)` - Array of ability names
- **`baseExperience`**: `pokemonData.base_experience` - Base experience points
- **`stats`**: Transform `pokemonData.stats` into a simpler object with just stat names and values
- **`moves`**: `pokemonData.moves.map(m => m.move.name)` - Array of move names (first 5-10)
- **`backSprite`**: `pokemonData.sprites.back_default` - Back-facing sprite image
- **`shinySprite`**: `pokemonData.sprites.front_shiny` - Shiny variant image

### Simplify Further
- Remove `height` or `weight` if you don't need them
- Only keep `name` and `imgUrl` for a minimal card view
- Extract just the first type: `pokemonData.types[0]?.type.name`

### Transform Data
- Capitalize the name: `pokemonData.name.charAt(0).toUpperCase() + pokemonData.name.slice(1)`
- Convert weight from hectograms to kilograms: `pokemonData.weight / 10`
- Convert height from decimeters to meters: `pokemonData.height / 10`
- Create a full image URL if it's relative: `pokemonData.sprites.front_default`

### Challenge Ideas
- Create multiple transform functions for different views (summary, detailed, stats-only)
- Add error handling for missing properties (use optional chaining `?.`)
- Transform multiple pokemon at once using `map()` with your transform function

---

**← [Back to Kata Index](./README.md)**

