Level Navigation: [1](./react-clicker-game-lv-1.md) | [2](./react-clicker-game-lv-2.md) | [3](./react-clicker-game-lv-3.md) | [4](./react-clicker-game-lv-4.md) | [5](./react-clicker-game-lv-5.md) | [6](./react-clicker-game-lv-6.md) | [7](./react-clicker-game-lv-7.md) | **8** | [9](./react-clicker-game-lv-9.md) | [10](./react-clicker-game-lv-10.md) | [11](./react-clicker-game-lv-11.md) | [12](./react-clicker-game-lv-12.md) | [13](./react-clicker-game-lv-13.md) | [14](./react-clicker-game-lv-14.md) | [15](./react-clicker-game-lv-15.md) | [16](./react-clicker-game-lv-16.md) | [17](./react-clicker-game-lv-17.md) | [18⚡](./react-clicker-game-lv-18.md) | [19](./react-clicker-game-lv-19.md)

# Level 8: Random Apple Position

**User Story:** As a player, I want the apple to appear in different locations so that I have to search for it and the game is more engaging.

## What You'll Do

Add state variables for apple position and randomize the position on each interaction.

## Instructions

- Create state variables `appleX` and `appleY` with initial value of 0
- Create a `randomSpot()` function that:
  - Sets `appleX` to a random value between 0 and 400
  - Sets `appleY` to a random value between 0 and 600
- Call `randomSpot()` in both `clickTarget` and `missTarget` functions
- Add `left` and `top` properties to the `appleStyle` object
- Test that the apple moves to different positions

## 💡 Code Hints

Need help with positioning? Check out these snippets:

<details>
<summary>Show Me: position state variables</summary>

<pre><code class="language-jsx">const [score, setScore] = useState(0)
const [lives, setLives] = useState(3)
const [appleSize, setAppleSize] = useState(100)
const [appleX, setAppleX] = useState(0);    // NEW
const [appleY, setAppleY] = useState(0);    // NEW
</code></pre>

</details>

<details>
<summary>Show Me: randomSpot function</summary>

<pre><code class="language-jsx">function randomSpot() {
  setAppleX(randomNumber(0, 400))
  setAppleY(randomNumber(0, 600))
}
</code></pre>

</details>

<details>
<summary>Show Me: updated click handlers</summary>

<pre><code class="language-jsx">function clickTarget(event) {
  event.stopPropagation();
  setScore(score + 1)
  randomSize();
  randomSpot()  // NEW
}

function missTarget() {
  setLives(lives - 1)
  randomSize();
  randomSpot()  // NEW
}
</code></pre>

</details>

<details>
<summary>Show Me: complete appleStyle object</summary>

<pre><code class="language-jsx">const appleStyle = {
  width: appleSize + &quot;px&quot;,
  height: appleSize + &quot;px&quot;,
  left: appleX + &quot;px&quot;,      // NEW
  top: appleY + &quot;px&quot;        // NEW
}
</code></pre>

</details>

## ✅ Check

1. Click the apple - it should move to a new random location
2. Click the background - apple should also move
3. The apple should stay within the game board boundaries
4. Both size and position should change simultaneously
5. If apple goes off-screen:
   - Check your random ranges (400 for X, 600 for Y)
   - Remember the game board is 500x700

**CSS Positioning Review:**
- `position: absolute` allows us to place elements anywhere
- `left` sets distance from the left edge
- `top` sets distance from the top edge
- Coordinates (0, 0) are at the top-left corner

---