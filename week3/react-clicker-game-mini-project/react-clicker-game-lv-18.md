Level Navigation: [1](./react-clicker-game-lv-1.md) | [2](./react-clicker-game-lv-2.md) | [3](./react-clicker-game-lv-3.md) | [4](./react-clicker-game-lv-4.md) | [5](./react-clicker-game-lv-5.md) | [6](./react-clicker-game-lv-6.md) | [7](./react-clicker-game-lv-7.md) | [8](./react-clicker-game-lv-8.md) | [9](./react-clicker-game-lv-9.md) | [10](./react-clicker-game-lv-10.md) | [11](./react-clicker-game-lv-11.md) | [12](./react-clicker-game-lv-12.md) | [13](./react-clicker-game-lv-13.md) | [14](./react-clicker-game-lv-14.md) | [15](./react-clicker-game-lv-15.md) | [16](./react-clicker-game-lv-16.md) | [17](./react-clicker-game-lv-17.md) | **18⚡** | [19](./react-clicker-game-lv-19.md)

# Level 18: Challenge Extensions ⚡

**CHALLENGE LEVEL**

**User Story:** As a developer, I want to implement advanced features so that I can challenge myself and create a more impressive game.

## What You'll Do

Choose from these advanced challenges to extend your game.

## Challenge Options

### Challenge 1: Game Over Condition
**Difficulty:** ⭐ Easy

Add a game over condition when lives reach 0.

**Instructions:**
- Add conditional rendering for when `lives <= 0`
- Show a "Game Over!" message
- Hide the apple
- Display final score
- Optionally add a restart button

<details>
<summary>Hint: Conditional structure</summary>

<pre><code class="language-jsx">if (lives &lt;= 0) {
  return &lt;GameOverScreen score={score} /&gt;
}
</code></pre>

</details>

---

### Challenge 2: Restart Functionality
**Difficulty:** ⭐ Easy

Add a button to restart the game.

**Instructions:**
- Create a `restartGame()` function
- Reset all state variables to initial values
- Add a restart button (visible on win or game over)
- Style the button

<details>
<summary>Hint: Reset function</summary>

<pre><code class="language-jsx">function restartGame() {
  setScore(0)
  setLives(3)
  setAppleSize(100)
  setAppleX(0)
  setAppleY(0)
}
</code></pre>

</details>

---

### Challenge 3: High Score with localStorage
**Difficulty:** ⭐⭐ Medium

Track and display the highest score using browser storage.

**Instructions:**
- Use `localStorage.getItem()` and `setItem()`
- Create state for `highScore`
- Update high score when game ends
- Display high score in stats or on win screen

<details>
<summary>Hint: localStorage usage</summary>

<pre><code class="language-jsx">// Load high score on mount
const [highScore, setHighScore] = useState(() =&gt; {
  return parseInt(localStorage.getItem(&#039;highScore&#039;)) || 0
})

// Save when game ends
if (score &gt; highScore) {
  setHighScore(score)
  localStorage.setItem(&#039;highScore&#039;, score)
}
</code></pre>

</details>

---

### Challenge 4: Sound Effects
**Difficulty:** ⭐⭐ Medium

Add sound effects for clicks, misses, and winning.

**Instructions:**
- Find or create sound files
- Use HTML5 Audio API or `<audio>` elements
- Play sounds on different game events
- Consider adding a mute button

<details>
<summary>Hint: Playing sounds</summary>

<pre><code class="language-jsx">const clickSound = new Audio(&#039;/click.mp3&#039;)

function clickTarget(event) {
  event.stopPropagation();
  clickSound.play()
  setScore(score + 1)
  // ... rest of function
}
</code></pre>

</details>

---

### Challenge 5: Timer/Countdown Mode
**Difficulty:** ⭐⭐⭐ Hard

Add a timer that counts down, creating urgency.

**Instructions:**
- Add state for `timeRemaining`
- Use `useEffect` with `setInterval` for countdown
- Game ends when time reaches 0
- Display timer in stats
- Clean up interval on unmount

<details>
<summary>Hint: Timer with useEffect</summary>

<pre><code class="language-jsx">useEffect(() =&gt; {
  if (timeRemaining &gt; 0) {
    const timer = setInterval(() =&gt; {
      setTimeRemaining(time =&gt; time - 1)
    }, 1000)
    
    return () =&gt; clearInterval(timer)
  }
}, [timeRemaining])
</code></pre>

</details>

---

### Challenge 6: Difficulty Levels
**Difficulty:** ⭐⭐⭐ Hard

Add Easy/Medium/Hard difficulty levels.

**Instructions:**
- Create difficulty selection screen
- Adjust game parameters based on difficulty:
  - Easy: Larger apples, slower changes
  - Medium: Current settings
  - Hard: Smaller apples, more lives lost
- Store difficulty in state
- Allow changing difficulty

---

### Challenge 7: Animations
**Difficulty:** ⭐⭐⭐ Hard

Add smooth animations for apple movement and size changes.

**Instructions:**
- Use CSS transitions for smooth size changes
- Consider React Spring or Framer Motion for animations
- Animate apple movement between positions
- Add particle effects on click

<details>
<summary>Hint: CSS transitions</summary>

<pre><code class="language-css">.apple-target {
  transition: all 0.3s ease-in-out;
}
</code></pre>

</details>

---

### Challenge 8: Mobile Support
**Difficulty:** ⭐⭐ Medium

Make the game work well on mobile devices.

**Instructions:**
- Add touch event support
- Make game board responsive
- Adjust sizes for smaller screens
- Test on mobile devices

---

## ✅ Check

1. Choose at least one challenge to implement
2. Test your new feature thoroughly
3. Update your README with new features
4. Commit your changes with descriptive messages
5. Consider adding screenshots or GIFs

---