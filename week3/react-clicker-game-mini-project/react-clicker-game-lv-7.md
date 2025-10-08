Level Navigation: [1](./react-clicker-game-lv-1.md) | [2](./react-clicker-game-lv-2.md) | [3](./react-clicker-game-lv-3.md) | [4](./react-clicker-game-lv-4.md) | [5](./react-clicker-game-lv-5.md) | [6](./react-clicker-game-lv-6.md) | **7** | [8](./react-clicker-game-lv-8.md) | [9](./react-clicker-game-lv-9.md) | [10](./react-clicker-game-lv-10.md) | [11](./react-clicker-game-lv-11.md) | [12](./react-clicker-game-lv-12.md) | [13](./react-clicker-game-lv-13.md) | [14](./react-clicker-game-lv-14.md) | [15](./react-clicker-game-lv-15.md) | [16](./react-clicker-game-lv-16.md) | [17](./react-clicker-game-lv-17.md) | [18⚡](./react-clicker-game-lv-18.md) | [19](./react-clicker-game-lv-19.md)

# Level 7: Random Apple Size

**User Story:** As a player, I want the apple to change size randomly so that the game becomes more challenging and interesting.

## What You'll Do

Create a utility function for random numbers and make the apple size change on each click.

## Instructions

- Create a `randomNumber(a, b)` helper function outside the App component
  - It should return a random integer between `a` and `b`
  - Use `Math.random()` and `Math.floor()`
- Create state variable `appleSize` with initial value of 100
- Create a `randomSize()` function that sets appleSize to a random value between 20 and 100
- Call `randomSize()` in both `clickTarget` and `missTarget` functions
- Create an `appleStyle` object with dynamic width and height
- Apply the style object to the apple-target div using the `style` attribute

## 💡 Code Hints

Need help with random numbers and dynamic styling? Check out these snippets:

<details>
<summary>Show Me: random number utility function</summary>

<pre><code class="language-jsx">function randomNumber(a, b) {
  return Math.floor(Math.random() * (b - a) + a);
}

function App() {
  // ... state and functions
}
</code></pre>

</details>

<details>
<summary>Show Me: apple size state and function</summary>

<pre><code class="language-jsx">const [score, setScore] = useState(0)
const [lives, setLives] = useState(3)
const [appleSize, setAppleSize] = useState(100)  // NEW

function randomSize() {
  const randomSize = randomNumber(20, 100)
  setAppleSize(randomSize)
}
</code></pre>

</details>

<details>
<summary>Show Me: updated click handlers</summary>

<pre><code class="language-jsx">function clickTarget(event) {
  event.stopPropagation();
  setScore(score + 1)
  randomSize();  // NEW
}

function missTarget() {
  setLives(lives - 1)
  randomSize();  // NEW
}
</code></pre>

</details>

<details>
<summary>Show Me: dynamic style object</summary>

<pre><code class="language-jsx">const appleStyle = {
  width: appleSize + &quot;px&quot;,
  height: appleSize + &quot;px&quot;
}

return (
  &lt;&gt;
    {/* ... stats div ... */}
    &lt;div className=&#039;orchard-background&#039; onClick={missTarget}&gt;
      &lt;div className=&quot;apple-target&quot; onClick={clickTarget} style={appleStyle}&gt;&lt;/div&gt;
    &lt;/div&gt;
  &lt;/&gt;
)
</code></pre>

</details>

## ✅ Check

1. Click the apple - it should change to a random size
2. Click the background - apple should also change size
3. Sizes should vary between very small and medium-large
4. The apple should maintain its aspect ratio
5. If size doesn't change:
   - Check that `randomSize()` is called in both handlers
   - Verify the style object is applied with `style={appleStyle}`

**How Math.random() works:**
- `Math.random()` returns a decimal between 0 and 1
- Multiply by range `(b - a)` to scale it
- Add `a` to shift to desired range
- `Math.floor()` rounds down to get an integer

---