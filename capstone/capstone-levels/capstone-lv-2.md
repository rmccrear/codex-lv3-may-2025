Level Navigation: [1](./capstone-lv-1.md) | **Current Level:** 2 | [3](./capstone-lv-3.md) | [4](./capstone-lv-4.md) | [5](./capstone-lv-5.md) | [6](./capstone-lv-6.md) | [7](./capstone-lv-7.md) | [8](./capstone-lv-8.md) | [9](./capstone-lv-9.md) | [10](./capstone-lv-10.md) | [11](./capstone-lv-11.md) | [12](./capstone-lv-12.md) | [13](./capstone-lv-13.md) | [14](./capstone-lv-14.md) | [15](./capstone-lv-15.md) | [16](./capstone-lv-16.md) | [17](./capstone-lv-17.md) | [18](./capstone-lv-18.md) | [19](./capstone-lv-19.md) | [20](./capstone-lv-20.md) | [21](./capstone-lv-21.md) | [22](./capstone-lv-22.md) | [23](./capstone-lv-23.md) | [24](./capstone-lv-24.md) | [25](./capstone-lv-25.md) | [26](./capstone-lv-26.md) | [27](./capstone-lv-27.md) | [28](./capstone-lv-28.md) | [29](./capstone-lv-29.md) | [30](./capstone-lv-30.md) | [31](./capstone-lv-31.md) | [32](./capstone-lv-32.md) | [33](./capstone-lv-33.md) | [34](./capstone-lv-34.md)

---

# Level 2: Basic HTML Structure & Live Server Test

## What You'll Do
Set up the basic HTML structure, link all necessary files, and test with live-server.

## Instructions
- Add `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`
- Add an H1 tag with your project name
- Link Bootstrap CSS (via CDN)
- Include these scripts, in order:
  1. `helpers-full.js`
  2. `secret-variables.js`
  3. `app.js`

## Example Script Order in index.html

```html
<!-- Example script order in index.html -->
<script src="helpers-full.js"></script>
<script src="secret-variables.js"></script>
<script src="app.js"></script>
```

## Add a console log to your JavaScript `app.js`

in `app.js`

```javascript
console.log("Hello from app.js");
```

## 💡 Code Hints
Need help with the HTML structure? Check out these snippets:
- **HTML IDs and JavaScript access:** See [SNIPPETS.md](../SNIPPETS.md#html-ids-and-javascript-access) for ID naming and element access
- **Bootstrap classes:** See [SNIPPETS.md](../SNIPPETS.md#bootstrap-classes) for styling examples

## ✅ Check
1. In your terminal, run `npx live-server` in your project folder
2. Your browser should automatically open to a local URL (like http://127.0.0.1:8080)
3. You should see your project title as a large heading (H1)
4. Open Chrome DevTools (F12) and check the Console tab
   - Look for any red error messages about missing files
   - Check that you can see a console log that says "Hello from app.js"
5. If you see errors about missing files, double-check your file names and paths

---


---

<!-- LEVEL_END -->


---

Level Navigation: [1](./capstone-lv-1.md) | **Current Level:** 2 | [3](./capstone-lv-3.md) | [4](./capstone-lv-4.md) | [5](./capstone-lv-5.md) | [6](./capstone-lv-6.md) | [7](./capstone-lv-7.md) | [8](./capstone-lv-8.md) | [9](./capstone-lv-9.md) | [10](./capstone-lv-10.md) | [11](./capstone-lv-11.md) | [12](./capstone-lv-12.md) | [13](./capstone-lv-13.md) | [14](./capstone-lv-14.md) | [15](./capstone-lv-15.md) | [16](./capstone-lv-16.md) | [17](./capstone-lv-17.md) | [18](./capstone-lv-18.md) | [19](./capstone-lv-19.md) | [20](./capstone-lv-20.md) | [21](./capstone-lv-21.md) | [22](./capstone-lv-22.md) | [23](./capstone-lv-23.md) | [24](./capstone-lv-24.md) | [25](./capstone-lv-25.md) | [26](./capstone-lv-26.md) | [27](./capstone-lv-27.md) | [28](./capstone-lv-28.md) | [29](./capstone-lv-29.md) | [30](./capstone-lv-30.md) | [31](./capstone-lv-31.md) | [32](./capstone-lv-32.md) | [33](./capstone-lv-33.md) | [34](./capstone-lv-34.md)
