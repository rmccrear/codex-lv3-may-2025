Level Navigation: [1](./react-clicker-game-lv-1.md) | [2](./react-clicker-game-lv-2.md) | [3](./react-clicker-game-lv-3.md) | [4](./react-clicker-game-lv-4.md) | [5](./react-clicker-game-lv-5.md) | [6](./react-clicker-game-lv-6.md) | [7](./react-clicker-game-lv-7.md) | [8](./react-clicker-game-lv-8.md) | [9](./react-clicker-game-lv-9.md) | **10** | [11](./react-clicker-game-lv-11.md) | [12](./react-clicker-game-lv-12.md) | [13](./react-clicker-game-lv-13.md) | [14](./react-clicker-game-lv-14.md) | [15](./react-clicker-game-lv-15.md) | [16](./react-clicker-game-lv-16.md) | [17](./react-clicker-game-lv-17.md) | [18⚡](./react-clicker-game-lv-18.md) | [19](./react-clicker-game-lv-19.md)

# Level 10: Add Win Condition Message

**User Story:** As a player, I want to see a "You Win!" message when I reach 100 points so that I know I've completed the game.

## What You'll Do

Add conditional rendering to show a win message at 100 points.

## Instructions

- After the apple-target div, add a conditional render for the win message
- Use `score >= 100 &&` to conditionally show an `<h1>` element
- Give it className "win" with text "You Win!"
- In `App.css`, style the `.win` class:
  - Use `position: absolute` to center it
  - Set background color and text color
  - Use `left: 50%; top: 50%` for positioning
  - Use `translate: -50% -50%` to perfectly center it

## 💡 Code Hints

Need help with conditional rendering? Check out these snippets:

<details>
<summary>Show Me: conditional rendering with &&</summary>

<pre><code class="language-jsx">&lt;div className=&#039;orchard-background&#039; onClick={missTarget}&gt;
  &lt;div className=&quot;apple-target&quot; onClick={clickTarget} style={appleStyle}&gt;&lt;/div&gt;
  {score &gt;= 100 &amp;&amp; &lt;h1 className=&quot;win&quot;&gt;You Win!&lt;/h1&gt;}
&lt;/div&gt;
</code></pre>

</details>

<details>
<summary>Show Me: win class CSS styling</summary>

<pre><code class="language-css">.win {
  position: absolute;
  background-color: green;
  color: red;
  left: 50%;
  top: 50%;
  translate: -50% -50%;
}
</code></pre>

</details>

## ✅ Check

1. Play the game and reach 100 points
2. "You Win!" message should appear in the center
3. The message should overlay the game board
4. Both the apple AND the win message should be visible
5. If message doesn't appear:
   - Check the conditional: `{score >= 100 && ...}`
   - Verify you've reached 100 points

**Understanding the && operator:**
- In JSX, `condition && <Component />` works like: "If condition is true, render Component"
- If false, React renders nothing
- This is called "short-circuit evaluation"

---