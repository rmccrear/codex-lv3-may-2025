Level Navigation: [1](./react-clicker-game-lv-1.md) | [2](./react-clicker-game-lv-2.md) | [3](./react-clicker-game-lv-3.md) | [4](./react-clicker-game-lv-4.md) | [5](./react-clicker-game-lv-5.md) | [6](./react-clicker-game-lv-6.md) | [7](./react-clicker-game-lv-7.md) | [8](./react-clicker-game-lv-8.md) | [9](./react-clicker-game-lv-9.md) | [10](./react-clicker-game-lv-10.md) | [11](./react-clicker-game-lv-11.md) | **12** | [13](./react-clicker-game-lv-13.md) | [14](./react-clicker-game-lv-14.md) | [15](./react-clicker-game-lv-15.md) | [16](./react-clicker-game-lv-16.md) | [17](./react-clicker-game-lv-17.md) | [18⚡](./react-clicker-game-lv-18.md) | [19](./react-clicker-game-lv-19.md)

# Level 12: Extract Stats Component with Props

**User Story:** As a developer, I want to organize my code into reusable components so that my application is easier to maintain and understand.

## What You'll Do

Extract the stats display into its own component that accepts props for score, lives, and styling.

## Instructions

- Create a new `Stats` component above the `App` component
- The component should accept `score`, `lives`, and `style` as props
- Move the stats div JSX into this component
- In `App`, replace the stats div with `<Stats score={score} lives={lives} style={statsStyle} />`
- Test that the stats display still works correctly

## 💡 Code Hints

Need help with components and props? Check out these snippets:

<details>
<summary>Show Me: Stats component definition</summary>

<pre><code class="language-jsx">function Stats({ score, lives, style }) {
  return (
    &lt;div className=&quot;stats&quot; style={style}&gt;
      Score: {score} Lives: {lives}
    &lt;/div&gt;
  )
}
</code></pre>

</details>

<details>
<summary>Show Me: using the Stats component in App</summary>

<pre><code class="language-jsx">function App() {
  // ... all your state and functions ...
  
  const statsStyle = {
    backgroundColor: &quot;brown&quot;,
    color: &quot;whitesmoke&quot;
  }
  
  // ... conditional styling logic ...
  
  return (
    &lt;&gt;
      &lt;Stats score={score} lives={lives} style={statsStyle} /&gt;
      &lt;div className=&#039;orchard-background&#039; onClick={missTarget}&gt;
        { score &lt; 100 ? 
          &lt;div className=&quot;apple-target&quot; onClick={clickTarget} style={appleStyle}&gt;&lt;/div&gt;
          : &lt;h1 className=&quot;win&quot;&gt; You Win!&lt;/h1&gt;
        }
      &lt;/div&gt;
    &lt;/&gt;
  )
}
</code></pre>

</details>

<details>
<summary>Show Me: complete file structure</summary>

<pre><code class="language-jsx">import { useState } from &#039;react&#039;
import &#039;./App.css&#039;

function randomNumber(a, b) {
  return Math.floor(Math.random() * (b - a) + a);
}

// NEW: Stats component
function Stats({ score, lives, style }) {
  return (
    &lt;div className=&quot;stats&quot; style={style}&gt;
      Score: {score} Lives: {lives}
    &lt;/div&gt;
  )
}

function App() {
  // ... rest of App component
}

export default App
</code></pre>

</details>

## ✅ Check

1. Stats should still display correctly
2. Colors should still change based on score
3. No console errors about missing props
4. The game should function exactly as before
5. Your code should feel more organized

**Understanding Props:**
- Props are like function parameters for components
- They pass data from parent to child
- Use destructuring `{ score, lives }` to extract props
- Props are read-only (never modify them directly)

**Why Extract Components?**
- **Reusability:** Use the same component in multiple places
- **Organization:** Each component has a single responsibility
- **Testing:** Easier to test small components
- **Readability:** Clearer code structure

---