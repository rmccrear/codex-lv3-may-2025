Level Navigation: [1](./react-clicker-game-lv-1.md) | [2](./react-clicker-game-lv-2.md) | [3](./react-clicker-game-lv-3.md) | [4](./react-clicker-game-lv-4.md) | [5](./react-clicker-game-lv-5.md) | [6](./react-clicker-game-lv-6.md) | [7](./react-clicker-game-lv-7.md) | [8](./react-clicker-game-lv-8.md) | [9](./react-clicker-game-lv-9.md) | [10](./react-clicker-game-lv-10.md) | **11** | [12](./react-clicker-game-lv-12.md) | [13](./react-clicker-game-lv-13.md) | [14](./react-clicker-game-lv-14.md) | [15](./react-clicker-game-lv-15.md) | [16](./react-clicker-game-lv-16.md) | [17](./react-clicker-game-lv-17.md) | [18⚡](./react-clicker-game-lv-18.md) | [19](./react-clicker-game-lv-19.md)

# Level 11: Hide Apple on Win

**User Story:** As a player, I want the apple to disappear when I win so that I don't accidentally keep clicking after winning.

## What You'll Do

Replace the conditional && with a ternary operator to show EITHER the apple OR the win message.

## Instructions

- Replace the apple-target div and win message with a ternary expression
- Use: `score < 100 ? ... : ...`
- If score < 100, show the apple-target div
- If score >= 100, show the win message
- Test that the apple disappears when you win

## 💡 Code Hints

Need help with ternary operators? Check out these snippets:

<details>
<summary>Show Me: ternary operator syntax</summary>

<pre><code class="language-jsx">&lt;div className=&#039;orchard-background&#039; onClick={missTarget}&gt;
  { score &lt; 100 ? 
    &lt;div className=&quot;apple-target&quot; onClick={clickTarget} style={appleStyle}&gt;&lt;/div&gt;
    : &lt;h1 className=&quot;win&quot;&gt; You Win!&lt;/h1&gt;
  }
&lt;/div&gt;
</code></pre>

</details>

## ✅ Check

1. Play the game with score below 100 - apple should be visible
2. Reach exactly 100 points
3. Apple should disappear immediately
4. "You Win!" message should appear
5. You should NOT be able to click the apple anymore
6. The game should feel complete and finished

**Ternary vs && operator:**
- `&&` operator: Shows component OR nothing
- Ternary `? :`: Shows component A OR component B
- Use ternary when you need mutual exclusivity

---