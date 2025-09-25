Level Navigation: [1](./capstone-lv-1.md) | [2](./capstone-lv-2.md) | [3](./capstone-lv-3.md) | [4](./capstone-lv-4.md) | [5](./capstone-lv-5.md) | [6](./capstone-lv-6.md) | [7](./capstone-lv-7.md) | [8](./capstone-lv-8.md) | [9](./capstone-lv-9.md) | [10](./capstone-lv-10.md) | [11](./capstone-lv-11.md) | [12](./capstone-lv-12.md) | [13](./capstone-lv-13.md) | [14](./capstone-lv-14.md) | [15](./capstone-lv-15.md) | [16](./capstone-lv-16.md) | [17](./capstone-lv-17.md) | [18](./capstone-lv-18.md) | [19](./capstone-lv-19.md) | [20](./capstone-lv-20.md) | **Current Level:** 21 | [22](./capstone-lv-22.md) | [23](./capstone-lv-23.md) | [24](./capstone-lv-24.md) | [25](./capstone-lv-25.md) | [26](./capstone-lv-26.md) | [27](./capstone-lv-27.md) | [28](./capstone-lv-28.md) | [29](./capstone-lv-29.md) | [30](./capstone-lv-30.md) | [31](./capstone-lv-31.md) | [32](./capstone-lv-32.md) | [33](./capstone-lv-33.md) | [34](./capstone-lv-34.md)

---

# Level 21: AI Error Handling (Optional Challenge)

## What You'll Do
Add proper error handling to your AI model calls.

## Instructions
- Use `.catch()` to handle AI errors (similar to Level 16 API error handling)
- Use `if(response.ok === false) { console.log('AI Error: ' + response.status + ' ' + response.statusText) }` to handle AI API errors
- Display user-friendly error messages to your users (not just console logs)
- Test your error handling by temporarily breaking the AI API call:
  - Change `https://` to `thtps://` (typo in protocol)
  - Put a typo in the endpoint path, for example: change `/v1/chat/completions` to `/v1/chat/completionss` (extra 's')
  - Add invalid data to the request body like `"model": "invalid-model-name"` (Look at the POJO sent as an argument to the fetch function call.)
  - **Remember to fix the API call back to working state when done testing**

## 💡 Code Hints
Need help with AI error handling? Check out these snippets:
- **Error handling:** See [SNIPPETS.md](../SNIPPETS.md#hugging-face-generated-code) for `.catch()` examples
- **User messages:** Use `setText()` to show error messages to users

## ✅ Check
1. Open your webpage in a browser
2. Click the button to trigger your AI call
3. You should see the AI response in the output area
4. Temporarily break your AI API URL (add "x" to the end)
5. Click the button again - you should see a user-friendly error message
6. Fix the AI API URL and test again - it should work normally

---


---

<!-- LEVEL_END -->


---

Level Navigation: [1](./capstone-lv-1.md) | [2](./capstone-lv-2.md) | [3](./capstone-lv-3.md) | [4](./capstone-lv-4.md) | [5](./capstone-lv-5.md) | [6](./capstone-lv-6.md) | [7](./capstone-lv-7.md) | [8](./capstone-lv-8.md) | [9](./capstone-lv-9.md) | [10](./capstone-lv-10.md) | [11](./capstone-lv-11.md) | [12](./capstone-lv-12.md) | [13](./capstone-lv-13.md) | [14](./capstone-lv-14.md) | [15](./capstone-lv-15.md) | [16](./capstone-lv-16.md) | [17](./capstone-lv-17.md) | [18](./capstone-lv-18.md) | [19](./capstone-lv-19.md) | [20](./capstone-lv-20.md) | **Current Level:** 21 | [22](./capstone-lv-22.md) | [23](./capstone-lv-23.md) | [24](./capstone-lv-24.md) | [25](./capstone-lv-25.md) | [26](./capstone-lv-26.md) | [27](./capstone-lv-27.md) | [28](./capstone-lv-28.md) | [29](./capstone-lv-29.md) | [30](./capstone-lv-30.md) | [31](./capstone-lv-31.md) | [32](./capstone-lv-32.md) | [33](./capstone-lv-33.md) | [34](./capstone-lv-34.md)
