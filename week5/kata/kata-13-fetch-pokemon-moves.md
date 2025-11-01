# Kata 13: Fetch Pokemon and Display Moves

**Concept:** Map pattern with fetched data (using for loop)

## Challenge

Create a `PokemonMoves` component that:
1. Fetches a pokemon from: `https://pokeapi.co/api/v2/pokemon/pikachu`
2. Uses a **for loop** in `useEffect` to extract all move names from the pokemon
3. Stores the move names in state
4. Uses `.map()` in JSX to display all moves as a list

**🔗 [Practice on CodeSandbox](https://codesandbox.io/)**

## Expected Output

When loaded, displays all move names:
<pre><code>Moves:
- thunder-shock
- quick-attack
- thunderbolt
- ... (and more)</code></pre>

## Starter Code

<pre><code class="language-jsx">import { useState, useEffect } from 'react';

export default function PokemonMoves() {
  const [moveList, setMoveList] = useState([]);
  
  useEffect(() => {
    async function fetchPokemon() {
      const response = await fetch('https://pokeapi.co/api/v2/pokemon/pikachu');
      const data = await response.json();
      
      // MAP: Use for loop to extract move names
      const moveNames = [];
      // Your for loop here
      
      setMoveList(moveNames);
    }
    
    fetchPokemon();
  }, []);
  
  if (moveList.length === 0) {
    return &lt;div&gt;Loading...&lt;/div&gt;;
  }
  
  return (
    &lt;div&gt;
      &lt;h3&gt;Moves:&lt;/h3&gt;
      &lt;ul&gt;
        {moveList.map((move, index) => (
          &lt;li key={index}&gt;{move}&lt;/li&gt;
        ))}
      &lt;/ul&gt;
    &lt;/div&gt;
  );
}</code></pre>

## Hints

- Fetch the pokemon data first
- The pokemon has a `moves` array
- Each move has structure: `{ move: { name: 'thunder-shock' } }`
- Use a for loop in `useEffect`: `for (let i = 0; i < data.moves.length; i++)`
- Access move name: `data.moves[i].move.name`
- Store move names: `moveNames.push(data.moves[i].move.name)`
- Use `.map()` in JSX to render: `moveList.map((move, index) => ...)`

## Solution

<details>
<summary>Click to reveal solution</summary>

<pre><code class="language-jsx">import { useState, useEffect } from 'react';

export default function PokemonMoves() {
  const [moveList, setMoveList] = useState([]);
  
  useEffect(() => {
    async function fetchPokemon() {
      const response = await fetch('https://pokeapi.co/api/v2/pokemon/pikachu');
      const data = await response.json();
      
      // MAP: Use for loop to extract move names
      const moveNames = [];
      for (let i = 0; i &lt; data.moves.length; i++) {
        moveNames.push(data.moves[i].move.name);
      }
      
      setMoveList(moveNames);
    }
    
    fetchPokemon();
  }, []);
  
  if (moveList.length === 0) {
    return &lt;div&gt;Loading...&lt;/div&gt;;
  }
  
  return (
    &lt;div&gt;
      &lt;h3&gt;Moves:&lt;/h3&gt;
      &lt;ul&gt;
        {moveList.map((move, index) => (
          &lt;li key={index}&gt;{move}&lt;/li&gt;
        ))}
      &lt;/ul&gt;
    &lt;/div&gt;
  );
}</code></pre>

</details>

## Concept Review

### Using For Loop for Data Transformation

- **Map pattern with for loop**: Transform each item to create a new array with different structure
- Loop through `data.moves` array using a for loop
- Extract move names: `data.moves[i].move.name`
- Push move names into new array: `moveNames.push(data.moves[i].move.name)`
- Store the transformed data in state
- This is the **List Scrolling Pattern** from Code.org - see [Code.org List Scrolling Pattern](https://studio.code.org/docs/concepts/patterns/list-scrolling-pattern/)
- **Using for loop**: Good for practice and keeping sharp with list patterns. This helps you understand what's happening under the hood and reinforces the fundamental pattern.

### Using .map() Method for Rendering

- **Built-in `.map()` method**: Transform array items into JSX elements for display
- Used in the JSX return: `moveList.map((move, index) => <li>...</li>)`
- A popular shorthand alternative in React that can be used directly in JSX
- Cleaner and more concise than a for loop for rendering
- Automatically handles creating an array of JSX elements
- The `.map()` method is the built-in JavaScript way to do the map pattern

### Why Use Both?

- **For loop in useEffect**: Good for algorithmically transforming data. Also great for practice and understanding the underlying pattern.
- **.map() in JSX**: Ideal for rendering because it's clean, readable, and React-optimized. This is the popular shorthand you'll see in most React code.
- Storing data (not JSX) in state allows you to manipulate/filter/sort the data before rendering

**Note:** Learn more about the built-in `.map()` method at [MDN: Array.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

## Challenge Variation

Try mapping other pokemon data:
- Display pokemon types: `pokemon.types[i].type.name`
- Display pokemon abilities: `pokemon.abilities[i].ability.name`

---

**← [Back to Kata Index](./README.md)**

