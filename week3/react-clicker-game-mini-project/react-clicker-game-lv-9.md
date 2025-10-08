Level Navigation: [1](./react-clicker-game-lv-1.md) | [2](./react-clicker-game-lv-2.md) | [3](./react-clicker-game-lv-3.md) | [4](./react-clicker-game-lv-4.md) | [5](./react-clicker-game-lv-5.md) | [6](./react-clicker-game-lv-6.md) | [7](./react-clicker-game-lv-7.md) | [8](./react-clicker-game-lv-8.md) | **9** | [10](./react-clicker-game-lv-10.md) | [11](./react-clicker-game-lv-11.md) | [12](./react-clicker-game-lv-12.md) | [13](./react-clicker-game-lv-13.md) | [14](./react-clicker-game-lv-14.md) | [15](./react-clicker-game-lv-15.md) | [16](./react-clicker-game-lv-16.md) | [17](./react-clicker-game-lv-17.md) | [18⚡](./react-clicker-game-lv-18.md) | [19](./react-clicker-game-lv-19.md)

# Level 9: Dynamic Stats Styling

**User Story:** As a player, I want the stats bar color to change as my score increases so that I get visual feedback on my progress.

## What You'll Do

Create dynamic styling that changes the stats bar color based on the current score.

## Instructions

- Create a `statsStyle` object with initial backgroundColor and color properties
- Write conditional logic (if/else statements) to change colors based on score:
  - Score < 10: brown background, whitesmoke text
  - Score < 20: darkGreen background, whitesmoke text
  - Score < 30: navy background, whitesmoke text
  - Score >= 30: black background, pink text
- Apply the `statsStyle` object to the stats div using the `style` attribute

## 💡 Code Hints

Need help with conditional styling? Check out these snippets:

<details>
<summary>Show Me: statsStyle object with conditionals</summary>

<pre><code class="language-jsx">const appleStyle = {
  width: appleSize + &quot;px&quot;,
  height: appleSize + &quot;px&quot;,
  left: appleX + &quot;px&quot;,
  top: appleY + &quot;px&quot;
}

// NEW: Dynamic stats styling
const statsStyle = {
  backgroundColor: &quot;brown&quot;,
  color: &quot;whitesmoke&quot;
}

if(score &lt; 10) {
  statsStyle.backgroundColor = &quot;brown&quot;
  statsStyle.color = &quot;whitesmoke&quot;
} else if (score &lt; 20) {
  statsStyle.backgroundColor = &quot;darkGreen&quot;
  statsStyle.color = &quot;whitesmoke&quot;    
} else if (score &lt; 30) {
  statsStyle.backgroundColor = &quot;navy&quot;
  statsStyle.color = &quot;whitesmoke&quot;    
} else {
  statsStyle.backgroundColor = &quot;black&quot;
  statsStyle.color = &quot;pink&quot;    
}
</code></pre>

</details>

<details>
<summary>Show Me: applying style to stats div</summary>

<pre><code class="language-jsx">return (
  &lt;&gt;
    &lt;div className=&quot;stats&quot; style={statsStyle}&gt;
      Score: {score} Lives: {lives}
    &lt;/div&gt;
    {/* ... rest of JSX ... */}
  &lt;/&gt;
)
</code></pre>

</details>

## ✅ Check

1. At score 0-9, stats bar should be brown
2. Click to reach score 10-19, stats should turn dark green
3. At score 20-29, stats should turn navy blue
4. At score 30+, stats should turn black with pink text
5. Colors should change immediately when crossing thresholds

**Why modify objects before rendering?**
In React, you can create style objects and modify them based on state before the return statement. Each time state changes, the component re-renders and the conditionals run again, creating fresh style objects.

---