Level Navigation: [1](./mad-libs-lv-1.md) | [2](./mad-libs-lv-2.md) | [3](./mad-libs-lv-3.md) | [4](./mad-libs-lv-4.md) | [5](./mad-libs-lv-5.md) | [6](./mad-libs-lv-6.md) | [7](./mad-libs-lv-7.md) | [8](./mad-libs-lv-8.md) | [9](./mad-libs-lv-9.md) | [10⚡](./mad-libs-lv-10.md) | **11⚡** | [12⚡](./mad-libs-lv-12.md) | [13⚡](./mad-libs-lv-13.md) | [14⚡](./mad-libs-lv-14.md) | [15](./mad-libs-lv-15.md) | [16](./mad-libs-lv-16.md) | [17](./mad-libs-lv-17.md) | [18⚡](./mad-libs-lv-18.md) | [19](./mad-libs-lv-19.md) | [20](./mad-libs-lv-20.md)

# Level 11: Random Story Access ⚡ CHALLENGE LEVEL

**User Story:** As a user, I want to discover random Mad Libs stories from my collection so that I can be surprised by stories I've forgotten about.

## What You'll Do
Create a route to display a random story from the stored stories.

## Instructions
- Create `/random` route
- Use `Math.random()` to select a random story
- Display the random story in a styled format
- Add 3 dummy stories to the array for testing

## 💡 Code Hints
Need help with random selection? Check out these snippets:
- **Random number:** Use `Math.floor(Math.random() * stories.length)`
- **Array access:** Use `stories[randomIndex]`
- **Empty array check:** Handle case when no stories exist
- **Dummy stories:** Use `let stories = ['Story 1', 'Story 2', 'Story 3'];` for testing

## ✅ Check
1. Add 3 dummy stories to your array for testing
2. Navigate to `/random` route
3. You should see a random story displayed
4. Refresh the page to see different random stories
5. If no random story appears, check your random selection logic

---