Level Navigation: [1](./react-clicker-game-lv-1.md) | [2](./react-clicker-game-lv-2.md) | [3](./react-clicker-game-lv-3.md) | [4](./react-clicker-game-lv-4.md) | [5](./react-clicker-game-lv-5.md) | [6](./react-clicker-game-lv-6.md) | [7](./react-clicker-game-lv-7.md) | [8](./react-clicker-game-lv-8.md) | **9** | [10](./react-clicker-game-lv-10.md) | [11](./react-clicker-game-lv-11.md) | [12](./react-clicker-game-lv-12.md) | [13](./react-clicker-game-lv-13.md) | [14](./react-clicker-game-lv-14.md) | [15](./react-clicker-game-lv-15.md) | [16](./react-clicker-game-lv-16.md) | [17](./react-clicker-game-lv-17.md) | [18⚡](./react-clicker-game-lv-18.md) | [19](./react-clicker-game-lv-19.md)

# Level 9: Dynamic Stats Styling

**User Story:** As a player, I want the stats bar color to change as my score increases so that I get visual feedback on my progress.

## What You'll Do

Create dynamic styling that changes the stats bar color based on the current score.

## Instructions

- Create a `statsStyle` object with initial backgroundColor and color properties
- Write conditional logic (if/else statements) to change colors based on score
- Apply the `statsStyle` object to the stats div using the `style` attribute
- Choose your own colors and score thresholds!

**Suggested Color Scheme (feel free to customize):**
- Score 0-9: `brown` background, `whitesmoke` text
- Score 10-19: `darkGreen` background, `whitesmoke` text
- Score 20-29: `navy` background, `whitesmoke` text
- Score 30+: `black` background, `pink` text

**Other color ideas:** `purple`, `teal`, `crimson`, `goldenrod`, `indigo`, `coral`, `forestgreen`

## ✅ Check

1. Stats bar changes color when you reach different score milestones
2. Colors change immediately when crossing your thresholds
3. Text color is readable against background color
4. You're happy with your creative color choices!

**Why modify objects before rendering?**
In React, you can create style objects and modify them based on state before the return statement. Each time state changes, the component re-renders and the conditionals run again, creating fresh style objects.

---