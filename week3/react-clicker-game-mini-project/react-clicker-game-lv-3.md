Level Navigation: [1](./react-clicker-game-lv-1.md) | [2](./react-clicker-game-lv-2.md) | **3** | [4](./react-clicker-game-lv-4.md) | [5](./react-clicker-game-lv-5.md) | [6](./react-clicker-game-lv-6.md) | [7](./react-clicker-game-lv-7.md) | [8](./react-clicker-game-lv-8.md) | [9](./react-clicker-game-lv-9.md) | [10](./react-clicker-game-lv-10.md) | [11](./react-clicker-game-lv-11.md) | [12](./react-clicker-game-lv-12.md) | [13](./react-clicker-game-lv-13.md) | [14](./react-clicker-game-lv-14.md) | [15](./react-clicker-game-lv-15.md) | [16](./react-clicker-game-lv-16.md) | [17](./react-clicker-game-lv-17.md) | [18⚡](./react-clicker-game-lv-18.md) | [19](./react-clicker-game-lv-19.md)

# Level 3: Add Game Images

**User Story:** As a developer, I want to add visual assets so that my game looks appealing.

## What You'll Do

Add image files for the apple target and orchard background to your project.

## Instructions

- Find or create two images:
  - An apple image (save as `apple.png`)
  - An orchard/nature background image (save as `orchard.png`)
- Place both images in the `public/` folder
- Delete the default `vite.svg` from `public/`
- Delete `react.svg` from `src/assets/`

## 💡 Code Hints

Need help with images? Check out these tips:

**Where to find images:**
- Use free stock photo sites like Unsplash, Pexels, or Pixabay
- Search for "apple transparent background" for the target
- Search for "orchard" or "apple tree" for the background
- Make sure images are properly licensed for use

**File structure:**
```
public/
  ├── apple.png      (Your apple target image)
  └── orchard.png    (Your background image)
```

**Why the public folder?**
Files in `public/` can be referenced directly in CSS using `/filename.png` without imports.

## ✅ Check

1. Navigate to `public/` folder in your file explorer
2. You should see `apple.png` and `orchard.png`
3. No default Vite/React SVG files should remain
4. Try accessing the images directly: `http://localhost:5173/apple.png`
5. You should see your apple image in the browser

---