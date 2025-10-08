Level Navigation: [1](./react-clicker-game-lv-1.md) | [2](./react-clicker-game-lv-2.md) | [3](./react-clicker-game-lv-3.md) | [4](./react-clicker-game-lv-4.md) | [5](./react-clicker-game-lv-5.md) | [6](./react-clicker-game-lv-6.md) | [7](./react-clicker-game-lv-7.md) | [8](./react-clicker-game-lv-8.md) | [9](./react-clicker-game-lv-9.md) | [10](./react-clicker-game-lv-10.md) | [11](./react-clicker-game-lv-11.md) | [12](./react-clicker-game-lv-12.md) | **13** | [14](./react-clicker-game-lv-14.md) | [15](./react-clicker-game-lv-15.md) | [16](./react-clicker-game-lv-16.md) | [17](./react-clicker-game-lv-17.md) | [18⚡](./react-clicker-game-lv-18.md) | [19](./react-clicker-game-lv-19.md)

# Level 13: Create GameBoard Component with Children

**User Story:** As a developer, I want to use the children prop pattern so that I can create flexible wrapper components.

## What You'll Do

Extract the orchard background into a `GameBoard` component that uses the `children` prop pattern.

## Instructions

- Create a new `GameBoard` component above `Stats`
- The component should accept `onMiss` and `children` as props
- Move the orchard-background div logic into this component
- The component should render `children` inside the orchard-background div
- In `App`, wrap your apple/win message with `<GameBoard onMiss={missTarget}>`
- Test that clicking the background still works

## 💡 Code Hints

Need help with the children prop? Check out these snippets:

<details>
<summary>Show Me: GameBoard component definition</summary>

<pre><code class="language-jsx">function GameBoard({ onMiss, children }) {
  return (
    &lt;div className=&#039;orchard-background&#039; onClick={onMiss}&gt;
      {children}
    &lt;/div&gt;
  )
}
</code></pre>

</details>

<details>
<summary>Show Me: using GameBoard in App</summary>

<pre><code class="language-jsx">return (
  &lt;&gt;
    &lt;Stats score={score} lives={lives} style={statsStyle} /&gt;
    &lt;GameBoard onMiss={missTarget}&gt;
      { score &lt; 100 ? 
        &lt;div className=&quot;apple-target&quot; onClick={clickTarget} style={appleStyle}&gt;&lt;/div&gt;
        : &lt;h1 className=&quot;win&quot;&gt; You Win!&lt;/h1&gt;
      }
    &lt;/GameBoard&gt;
  &lt;/&gt;
)
</code></pre>

</details>

<details>
<summary>Show Me: complete component structure</summary>

<pre><code class="language-jsx">import { useState } from &#039;react&#039;
import &#039;./App.css&#039;

function randomNumber(a, b) {
  return Math.floor(Math.random() * (b - a) + a);
}

// NEW: GameBoard component with children
function GameBoard({ onMiss, children }) {
  return (
    &lt;div className=&#039;orchard-background&#039; onClick={onMiss}&gt;
      {children}
    &lt;/div&gt;
  )
}

function Stats({ score, lives, style }) {
  return (
    &lt;div className=&quot;stats&quot; style={style}&gt;
      Score: {score} Lives: {lives}
    &lt;/div&gt;
  )
}

function App() {
  const [score, setScore] = useState(0)
  const [lives, setLives] = useState(3)
  const [appleSize, setAppleSize] = useState(100)
  const [appleX, setAppleX] = useState(0);
  const [appleY, setAppleY] = useState(0);

  // ... all your functions ...

  return (
    &lt;&gt;
      &lt;Stats score={score} lives={lives} style={statsStyle} /&gt;
      &lt;GameBoard onMiss={missTarget}&gt;
        { score &lt; 100 ? 
          &lt;div className=&quot;apple-target&quot; onClick={clickTarget} style={appleStyle}&gt;&lt;/div&gt;
          : &lt;h1 className=&quot;win&quot;&gt; You Win!&lt;/h1&gt;
        }
      &lt;/GameBoard&gt;
    &lt;/&gt;
  )
}

export default App
</code></pre>

</details>

## ✅ Check

1. The game should look and work exactly as before
2. Missing the apple should still decrease lives
3. Clicking the apple should still work (not trigger the miss handler)
4. No console errors
5. Your code should be more modular and organized

**Understanding Children:**
- `children` is a special prop in React
- It represents whatever is placed between component tags
- Like HTML: `<div>content here</div>` → content is children
- Makes components flexible and reusable

**The Children Pattern:**
```jsx
<GameBoard>
  <Apple />
  <WinMessage />
</GameBoard>
```
The `Apple` and `WinMessage` components become the `children` prop of `GameBoard`.

**Why Use Children?**
- **Flexibility:** GameBoard doesn't need to know what's inside it
- **Composition:** Build complex UIs from simple pieces
- **Reusability:** Same GameBoard can contain different content
- **Separation of Concerns:** Parent decides content, child handles layout

---