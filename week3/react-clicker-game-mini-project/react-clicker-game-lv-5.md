Level Navigation: [1](./react-clicker-game-lv-1.md) | [2](./react-clicker-game-lv-2.md) | [3](./react-clicker-game-lv-3.md) | [4](./react-clicker-game-lv-4.md) | **5** | [6](./react-clicker-game-lv-6.md) | [7](./react-clicker-game-lv-7.md) | [8](./react-clicker-game-lv-8.md) | [9](./react-clicker-game-lv-9.md) | [10](./react-clicker-game-lv-10.md) | [11](./react-clicker-game-lv-11.md) | [12](./react-clicker-game-lv-12.md) | [13](./react-clicker-game-lv-13.md) | [14](./react-clicker-game-lv-14.md) | [15](./react-clicker-game-lv-15.md) | [16](./react-clicker-game-lv-16.md) | [17](./react-clicker-game-lv-17.md) | [18⚡](./react-clicker-game-lv-18.md) | [19](./react-clicker-game-lv-19.md)

# Level 5: Add Score Tracking

**User Story:** As a player, I want to see my score increase when I click the apple so that I can track my progress.

## What You'll Do

Add React state to track the score and create a click handler for the apple.

## Instructions

- Import `useState` from React
- Create a state variable for `score` with initial value of 0
- Create a `clickTarget` function that:
  - Accepts an `event` parameter
  - Calls `event.stopPropagation()` to prevent click bubbling
  - Increments the score by 1
- Add an `onClick` handler to the apple-target div
- Create a stats div above the game board to display the score
- Style the stats div in CSS

## 💡 Code Hints

Need help with state and events? Check out these snippets:

<details>
<summary>Show Me: useState import and setup</summary>

<pre><code class="language-jsx">import { useState } from &#039;react&#039;
import &#039;./App.css&#039;

function App() {
  const [score, setScore] = useState(0)
  
  // ... rest of component
}
</code></pre>

</details>

<details>
<summary>Show Me: click handler function</summary>

<pre><code class="language-jsx">function clickTarget(event) {
  event.stopPropagation();  // Prevents triggering parent clicks
  setScore(score + 1)
}
</code></pre>

</details>

<details>
<summary>Show Me: JSX with stats display</summary>

<pre><code class="language-jsx">return (
  &lt;&gt;
    &lt;div className=&quot;stats&quot;&gt;
      Score: {score}
    &lt;/div&gt;
    &lt;div className=&#039;orchard-background&#039;&gt;
      &lt;div className=&quot;apple-target&quot; onClick={clickTarget}&gt;&lt;/div&gt;
    &lt;/div&gt;
  &lt;/&gt;
)
</code></pre>

</details>

<details>
<summary>Show Me: stats CSS styling</summary>

<pre><code class="language-css">.stats {
  background-color: brown;
  color: whitesmoke;
  width: 500px;
  padding: 5px;
}
</code></pre>

</details>

## ✅ Check

1. You should see "Score: 0" above the game board
2. Click the apple - the score should increase to 1
3. Click multiple times - score should keep increasing
4. The stats bar should have a brown background
5. If score doesn't update, check:
   - `useState` is imported correctly
   - `onClick` handler is attached to apple-target
   - You're using `setScore` to update state

---