Level Navigation: [1](./capstone-lv-1.md) | [2](./capstone-lv-2.md) | [3](./capstone-lv-3.md) | [4](./capstone-lv-4.md) | [5](./capstone-lv-5.md) | [6](./capstone-lv-6.md) | [7](./capstone-lv-7.md) | **Current Level:** 8 | [9](./capstone-lv-9.md) | [10](./capstone-lv-10.md) | [11](./capstone-lv-11.md) | [12](./capstone-lv-12.md) | [13](./capstone-lv-13.md) | [14](./capstone-lv-14.md) | [15](./capstone-lv-15.md) | [16](./capstone-lv-16.md) | [17](./capstone-lv-17.md) | [18](./capstone-lv-18.md) | [19](./capstone-lv-19.md) | [20](./capstone-lv-20.md) | [21](./capstone-lv-21.md) | [22](./capstone-lv-22.md) | [23](./capstone-lv-23.md) | [24](./capstone-lv-24.md) | [25](./capstone-lv-25.md) | [26](./capstone-lv-26.md) | [27](./capstone-lv-27.md) | [28](./capstone-lv-28.md) | [29](./capstone-lv-29.md) | [30](./capstone-lv-30.md) | [31](./capstone-lv-31.md) | [32](./capstone-lv-32.md) | [33](./capstone-lv-33.md) | [34](./capstone-lv-34.md)

---

# Level 8: IDs and Testing

## What You'll Do
Add meaningful IDs to all elements and test that they can be accessed.

## Instructions
- Add meaningful `id` attributes to all elements (input, button, card, etc.)
- Test that you can access them with `getElementById()` in the console
- Use `setProperty()` to test that you can modify element properties

## 💡 Code Hints
Need help with IDs? Check out these snippets:
- **HTML IDs and JavaScript access:** See [SNIPPETS.md](../SNIPPETS.md#html-ids-and-javascript-access) for ID naming and element access
- **Testing elements:** Use `console.log(document.getElementById("your-id"))` to test access

## ✅ Check
1. Open your webpage in a browser
2. Open Chrome DevTools (F12) and go to the Console tab
3. Type `document.getElementById("your-input-id")` and press Enter
4. You should see the input element returned (not null)
5. Test all your IDs this way to make sure they work
6. Try using `setProperty()` to test element modification:
   - `setProperty("your-input-id", "backgroundColor", "yellow")`
   - `setProperty("your-button-id", "border", "3px solid red")`
7. If any return `null`, check that the ID is spelled correctly in your HTML

## 🔍 Optional: Diving Deeper - DOM Operations
For extra practice, you can also test element access with:
```javascript
console.log(document.getElementById("your-input-id"))
```
This will show you the full element object in the console, which can help you understand what properties and methods are available.

You can also use the native DOM `style` property to modify elements directly:
```javascript
// Same as setProperty("your-input-id", "backgroundColor", "yellow")
document.getElementById("your-input-id").style.backgroundColor = "yellow";

// Same as setProperty("your-button-id", "border", "3px solid red")
document.getElementById("your-button-id").style.border = "3px solid red";
```

The DOM Operations approach is the standard way to manipulate styles in professional JavaScript development and is used across all major frameworks and libraries. Learning the native DOM API prepares you for real-world codebases where helper functions aren't available.

---


---

<!-- LEVEL_END -->


---

Level Navigation: [1](./capstone-lv-1.md) | [2](./capstone-lv-2.md) | [3](./capstone-lv-3.md) | [4](./capstone-lv-4.md) | [5](./capstone-lv-5.md) | [6](./capstone-lv-6.md) | [7](./capstone-lv-7.md) | **Current Level:** 8 | [9](./capstone-lv-9.md) | [10](./capstone-lv-10.md) | [11](./capstone-lv-11.md) | [12](./capstone-lv-12.md) | [13](./capstone-lv-13.md) | [14](./capstone-lv-14.md) | [15](./capstone-lv-15.md) | [16](./capstone-lv-16.md) | [17](./capstone-lv-17.md) | [18](./capstone-lv-18.md) | [19](./capstone-lv-19.md) | [20](./capstone-lv-20.md) | [21](./capstone-lv-21.md) | [22](./capstone-lv-22.md) | [23](./capstone-lv-23.md) | [24](./capstone-lv-24.md) | [25](./capstone-lv-25.md) | [26](./capstone-lv-26.md) | [27](./capstone-lv-27.md) | [28](./capstone-lv-28.md) | [29](./capstone-lv-29.md) | [30](./capstone-lv-30.md) | [31](./capstone-lv-31.md) | [32](./capstone-lv-32.md) | [33](./capstone-lv-33.md) | [34](./capstone-lv-34.md)
