Level Navigation: [1](./react-clicker-game-lv-1.md) | [2](./react-clicker-game-lv-2.md) | [3](./react-clicker-game-lv-3.md) | [4](./react-clicker-game-lv-4.md) | [5](./react-clicker-game-lv-5.md) | **6** | [7](./react-clicker-game-lv-7.md) | [8](./react-clicker-game-lv-8.md) | [9](./react-clicker-game-lv-9.md) | [10](./react-clicker-game-lv-10.md) | [11](./react-clicker-game-lv-11.md) | [12](./react-clicker-game-lv-12.md) | [13](./react-clicker-game-lv-13.md) | [14](./react-clicker-game-lv-14.md) | [15](./react-clicker-game-lv-15.md) | [16](./react-clicker-game-lv-16.md) | [17](./react-clicker-game-lv-17.md) | [18⚡](./react-clicker-game-lv-18.md) | [19](./react-clicker-game-lv-19.md)

# Level 6: Add Lives Tracking

**User Story:** As a player, I want to lose a life when I miss the apple so that the game has challenge and consequences.

## What You'll Do

Add a lives state variable and create a miss handler for clicking the background.

## Instructions

- Create a new state variable for `lives` with initial value of 3
- Create a `missTarget` function that decrements lives by 1
- Add an `onClick` handler to the orchard-background div
- Update the stats display to show both score and lives
- Test that clicking the apple doesn't trigger the miss handler

## 💡 Code Hints

Need help with multiple state variables? Check out these snippets:

<details>
<summary>Show Me: adding lives state</summary>

<pre><code class="language-jsx">function App() {
  const [score, setScore] = useState(0)
  const [lives, setLives] = useState(3)  // NEW
  
  // ... rest of component
}
</code></pre>

</details>

<details>
<summary>Show Me: miss handler function</summary>

<pre><code class="language-jsx">function missTarget() {
  setLives(lives - 1)
}
</code></pre>

</details>

<details>
<summary>Show Me: updated JSX with onClick handlers</summary>

<pre><code class="language-jsx">return (
  &lt;&gt;
    &lt;div className=&quot;stats&quot;&gt;
      Score: {score} Lives: {lives}
    &lt;/div&gt;
    &lt;div className=&#039;orchard-background&#039; onClick={missTarget}&gt;
      &lt;div className=&quot;apple-target&quot; onClick={clickTarget}&gt;&lt;/div&gt;
    &lt;/div&gt;
  &lt;/&gt;
)
</code></pre>

</details>

## ✅ Check

1. You should see "Score: 0 Lives: 3" in the stats bar
2. Click the apple - score increases, lives stay the same
3. Click the background (miss the apple) - lives decrease
4. Click the apple again - only score increases (lives unchanged)
5. If both handlers fire when clicking apple:
   - Make sure `event.stopPropagation()` is in `clickTarget`

**Understanding Event Propagation:**
Try removing `event.stopPropagation()` temporarily to see what happens. You'll notice clicking the apple triggers BOTH handlers because clicks "bubble up" from child to parent. That's why we need `stopPropagation()`!

---