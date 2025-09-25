Level Navigation: [1](./mad-libs-lv-1.md) | [2](./mad-libs-lv-2.md) | [3](./mad-libs-lv-3.md) | [4](./mad-libs-lv-4.md) | [5](./mad-libs-lv-5.md) | [6](./mad-libs-lv-6.md) | [7](./mad-libs-lv-7.md) | [8](./mad-libs-lv-8.md) | [9](./mad-libs-lv-9.md) | [10⚡](./mad-libs-lv-10.md) | [11⚡](./mad-libs-lv-11.md) | [12⚡](./mad-libs-lv-12.md) | [13⚡](./mad-libs-lv-13.md) | **14⚡** | [15](./mad-libs-lv-15.md) | [16](./mad-libs-lv-16.md) | [17](./mad-libs-lv-17.md) | [18⚡](./mad-libs-lv-18.md) | [19](./mad-libs-lv-19.md) | [20](./mad-libs-lv-20.md)

# Level 14: Error Handling and Validation ⚡ CHALLENGE LEVEL

**User Story:** As a user, I want to get clear, helpful messages when something goes wrong so that I know how to fix the problem.

## What You'll Do
Add basic validation and error handling to improve the user experience.

## Instructions
- Add validation for required form fields
- Handle edge cases (empty stories, invalid numbers)
- Display user-friendly error messages

## 💡 Code Hints
Need help with validation? Check out these snippets:
- **Field validation:** Use `if (!fieldName)` to check for empty fields
- **Error messages:** Use `res.status(400).send()` for error responses
- **User feedback:** Display clear error messages

## ✅ Check
1. Submit form with empty fields
2. You should see validation error messages
3. Try accessing invalid story numbers
4. Error messages should be user-friendly
5. If validation doesn't work, check your conditional statements

---