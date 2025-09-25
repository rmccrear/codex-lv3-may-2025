Level Navigation: [1](./mad-libs-lv-1.md) | [2](./mad-libs-lv-2.md) | [3](./mad-libs-lv-3.md) | [4](./mad-libs-lv-4.md) | [5](./mad-libs-lv-5.md) | [6](./mad-libs-lv-6.md) | [7](./mad-libs-lv-7.md) | [8](./mad-libs-lv-8.md) | [9](./mad-libs-lv-9.md) | [10⚡](./mad-libs-lv-10.md) | [11⚡](./mad-libs-lv-11.md) | **12⚡** | [13⚡](./mad-libs-lv-13.md) | [14⚡](./mad-libs-lv-14.md) | [15](./mad-libs-lv-15.md) | [16](./mad-libs-lv-16.md) | [17](./mad-libs-lv-17.md) | [18⚡](./mad-libs-lv-18.md) | [19](./mad-libs-lv-19.md) | [20](./mad-libs-lv-20.md)

# Level 12: Individual Story Access ⚡ CHALLENGE LEVEL

**User Story:** As a user, I want to find and read a specific Mad Libs story by its number so that I can revisit my favorite stories.

## What You'll Do
Create a route to access individual stories by number using query parameters.

## Instructions
- Create `/story-no` route
- Parse query parameter `number`
- Display the specific story requested

## 💡 Code Hints
Need help with query parameters? Check out these snippets:
- **Parameter parsing:** Use `parseInt(req.query.number)`
- **Array indexing:** Convert to 0-based index with `number - 1`
- **Error handling:** Handle invalid numbers gracefully

## ✅ Check
1. Create several stories first
2. Navigate to `/story-no?number=1`
3. You should see the first story
4. Try different numbers to access different stories
5. If stories don't appear, check your parameter parsing

---