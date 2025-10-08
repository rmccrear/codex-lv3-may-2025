Level Navigation: [1](./react-clicker-game-lv-1.md) | [2](./react-clicker-game-lv-2.md) | [3](./react-clicker-game-lv-3.md) | [4](./react-clicker-game-lv-4.md) | [5](./react-clicker-game-lv-5.md) | [6](./react-clicker-game-lv-6.md) | [7](./react-clicker-game-lv-7.md) | [8](./react-clicker-game-lv-8.md) | [9](./react-clicker-game-lv-9.md) | [10](./react-clicker-game-lv-10.md) | [11](./react-clicker-game-lv-11.md) | [12](./react-clicker-game-lv-12.md) | [13](./react-clicker-game-lv-13.md) | **14** | [15](./react-clicker-game-lv-15.md) | [16](./react-clicker-game-lv-16.md) | [17](./react-clicker-game-lv-17.md) | [18⚡](./react-clicker-game-lv-18.md) | [19](./react-clicker-game-lv-19.md)

# Level 14: Testing and Polish

**User Story:** As a developer, I want to test my game thoroughly so that I can ensure it works perfectly.

## What You'll Do

Perform comprehensive testing and add any final improvements.

## Instructions

- Test all game mechanics:
  - Clicking the apple increases score
  - Missing decreases lives
  - Apple changes size randomly
  - Apple moves to random positions
  - Stats bar changes colors
  - Win condition triggers at 100
- Test edge cases:
  - What happens if lives reach 0? (Currently nothing - this is okay)
  - Can you click past 100 points? (No - game ends)
  - Do small apples still work?
- Check styling:
  - Is everything centered properly?
  - Are colors readable?
  - Does the layout look good?
- Consider improvements:
  - Add a "Game Over" condition when lives = 0
  - Add a reset button
  - Add sound effects
  - Track high score

## 💡 Code Hints

Need help with testing? Check out these tips:

**Testing Checklist:**
- [ ] Score increases on apple click
- [ ] Lives decrease on background click
- [ ] Apple size changes randomly
- [ ] Apple position changes randomly
- [ ] Stats colors change at correct thresholds
- [ ] Win message appears at 100 points
- [ ] Apple disappears when winning
- [ ] No console errors

**Common Issues:**
- If clicks don't work: Check `onClick` handlers
- If state doesn't update: Check `setState` calls
- If styling is broken: Check CSS class names
- If images don't load: Check file paths

## ✅ Check

1. Run through the complete game at least twice
2. Try to break it with rapid clicks
3. Test with very small apples (harder to click)
4. Verify win condition works consistently
5. Check browser console for any errors
6. Test in different browsers if possible

---