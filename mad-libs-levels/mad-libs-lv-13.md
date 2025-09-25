Level Navigation: [1](./mad-libs-lv-1.md) | [2](./mad-libs-lv-2.md) | [3](./mad-libs-lv-3.md) | [4](./mad-libs-lv-4.md) | [5](./mad-libs-lv-5.md) | [6](./mad-libs-lv-6.md) | [7](./mad-libs-lv-7.md) | [8](./mad-libs-lv-8.md) | [9](./mad-libs-lv-9.md) | [10⚡](./mad-libs-lv-10.md) | [11⚡](./mad-libs-lv-11.md) | [12⚡](./mad-libs-lv-12.md) | **13⚡** | [14⚡](./mad-libs-lv-14.md) | [15](./mad-libs-lv-15.md) | [16](./mad-libs-lv-16.md) | [17](./mad-libs-lv-17.md) | [18⚡](./mad-libs-lv-18.md) | [19](./mad-libs-lv-19.md) | [20](./mad-libs-lv-20.md)

# Level 13: Navigation Between Stories ⚡ CHALLENGE LEVEL

**User Story:** As a user, I want to easily move between different Mad Libs stories so that I can browse through my collection without getting lost.

## What You'll Do
Add navigation links to move between stories and improve user experience.

## Instructions
- Add "Next Story" link when available
- Add navigation links to random story and main form
- Handle boundary conditions (no next story at end)

## 💡 Code Hints
Need help with navigation? Check out these snippets:
- **Conditional links:** Use `if (hasNextStory)` to show/hide links
- **Link generation:** Use template literals for dynamic URLs
- **Boundary checking:** Check `storyNumber < stories.length`

## ✅ Check
1. Navigate to individual stories
2. You should see appropriate navigation links
3. "Next Story" should only appear when there is a next story
4. All navigation should work correctly
5. If navigation doesn't work, check your conditional logic

---