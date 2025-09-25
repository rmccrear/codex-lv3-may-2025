Level Navigation: [1](./capstone-lv-1.md) | [2](./capstone-lv-2.md) | [3](./capstone-lv-3.md) | [4](./capstone-lv-4.md) | [5](./capstone-lv-5.md) | [6](./capstone-lv-6.md) | [7](./capstone-lv-7.md) | [8](./capstone-lv-8.md) | **Current Level:** 9 | [10](./capstone-lv-10.md) | [11](./capstone-lv-11.md) | [12](./capstone-lv-12.md) | [13](./capstone-lv-13.md) | [14](./capstone-lv-14.md) | [15](./capstone-lv-15.md) | [16](./capstone-lv-16.md) | [17](./capstone-lv-17.md) | [18](./capstone-lv-18.md) | [19](./capstone-lv-19.md) | [20](./capstone-lv-20.md) | [21](./capstone-lv-21.md) | [22](./capstone-lv-22.md) | [23](./capstone-lv-23.md) | [24](./capstone-lv-24.md) | [25](./capstone-lv-25.md) | [26](./capstone-lv-26.md) | [27](./capstone-lv-27.md) | [28](./capstone-lv-28.md) | [29](./capstone-lv-29.md) | [30](./capstone-lv-30.md) | [31](./capstone-lv-31.md) | [32](./capstone-lv-32.md) | [33](./capstone-lv-33.md) | [34](./capstone-lv-34.md)

---

# Level 9: Event Listeners

## What You'll Do
Add event listeners to your button and input using the `onEvent` helper function.

## Instructions
- Add an event listener to your button for the "click" event
- Add an event listener to your input for the "input" event
- Use `onEvent(elementId, eventType, function)` syntax

## 💡 Code Hints
Need help with event listeners? Check out these snippets:
- **Event handling:** See [SNIPPETS.md](../SNIPPETS.md#event-handling) for `onEvent` examples
- **Anonymous functions:** Use `function() { }` syntax for your event handlers

## ✅ Check
1. Open your webpage in a browser
2. Open Chrome DevTools (F12) and go to the Console tab
3. Click your button - you should see a message in the console
4. Type in your input - you should see messages in the console as you type
5. If you don't see messages, check that your event listeners are set up correctly

## 🔍 Optional: Diving Deeper - Named Functions
Instead of using anonymous functions, you can create named functions for your event handlers:
```javascript
function clickHandler() {
    console.log("Button was clicked!");
    setText("output", "Hello from the button!");
}

// Use the named functions with onEvent
onEvent("my-button", "click", clickHandler);
```
Named functions make your code more readable and reusable, especially when you need to use the same handler for multiple elements.

## 🔍 Optional: Diving Deeper - Native addEventListener
You can also use the native DOM `addEventListener` method instead of the helper function:
```javascript
function clickHandler() {
    console.log("Button was clicked!");
    setText("output", "Hello from the button!");
}

// Use native addEventListener
document.getElementById("my-button").addEventListener("click", clickHandler);
```
This approach gives you direct access to the native DOM API and is the standard method used in professional JavaScript development.

---


---

<!-- LEVEL_END -->


---

Level Navigation: [1](./capstone-lv-1.md) | [2](./capstone-lv-2.md) | [3](./capstone-lv-3.md) | [4](./capstone-lv-4.md) | [5](./capstone-lv-5.md) | [6](./capstone-lv-6.md) | [7](./capstone-lv-7.md) | [8](./capstone-lv-8.md) | **Current Level:** 9 | [10](./capstone-lv-10.md) | [11](./capstone-lv-11.md) | [12](./capstone-lv-12.md) | [13](./capstone-lv-13.md) | [14](./capstone-lv-14.md) | [15](./capstone-lv-15.md) | [16](./capstone-lv-16.md) | [17](./capstone-lv-17.md) | [18](./capstone-lv-18.md) | [19](./capstone-lv-19.md) | [20](./capstone-lv-20.md) | [21](./capstone-lv-21.md) | [22](./capstone-lv-22.md) | [23](./capstone-lv-23.md) | [24](./capstone-lv-24.md) | [25](./capstone-lv-25.md) | [26](./capstone-lv-26.md) | [27](./capstone-lv-27.md) | [28](./capstone-lv-28.md) | [29](./capstone-lv-29.md) | [30](./capstone-lv-30.md) | [31](./capstone-lv-31.md) | [32](./capstone-lv-32.md) | [33](./capstone-lv-33.md) | [34](./capstone-lv-34.md)
