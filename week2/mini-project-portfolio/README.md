# Portfolio Component Challenge

## Overview
This React portfolio project is currently built with a large, monolithic `App` component. Your challenge is to break it down into smaller, reusable components following React best practices. This project is based on the [How to Portfolio Gallery on w3schools](https://www.w3schools.com/howto/howto_css_portfolio_gallery.asp).

## Current Project Structure
- **App.jsx**: Main component containing the entire portfolio layout
- **App.css**: Styles for the portfolio grid and layout
- **HeroImage.jsx**: Already extracted hero section component (based on [W3Schools Hero Image tutorial](https://www.w3schools.com/howto/howto_css_hero_image.asp))
- **HeroImage.css**: Styles for the hero section

## Project Goals

### Phase 1: Component Extraction
Create **at least 7 components** to break down the App component:
- **3 components with no props** (simple, self-contained components)
- **3 components with props** (reusable components that accept data)
- **1 component with `children` props** (wrapper component that renders child content)

**Suggested components to create:**
- `Header` - The "MYLOGO.COM" and "PORTFOLIO" section
- `ProjectCard` - Individual project display (with props for image, title, description)
- `ProjectGrid` - Container for the portfolio grid
- `ProjectImage` - Reusable image component
- `ProjectTitle` - Title display component
- `ProjectDescription` - Description text component
- `Content` - Wrapper component that accepts children

### Phase 2: File Organization
Move each new component into its own file in the `./components` directory:
```
src/
  components/
    HeroImage.jsx (already exists)
    HeroImage.css (already exists)
    Header.jsx
    ProjectCard.jsx
    ProjectGrid.jsx
    ProjectImage.jsx
    ProjectTitle.jsx
    ProjectDescription.jsx
    Content.jsx
```

### Phase 3: Data Management & Enhancement

1. **Replace placeholder content** with your own projects from class
2. **Update the hero section** with your own photo and information
3. **Enhance the styling** with your personal touches

## Bonus Challenges

### Code Efficiency Challenge
- Use a `.map()` function to render projects from an array (see [React Lists documentation](https://react.dev/learn/rendering-lists)) or [for-loops documentation](https://studio.code.org/docs/concepts/javascript/for-loops/)
- Create a projects data array with image paths, titles, and descriptions
- Learn about [React component composition](https://react.dev/learn/your-first-component) and [passing props](https://react.dev/learn/passing-props-to-a-component)

### Styling Enhancements Challenge
- Add your own color scheme using [Coolors.co](https://coolors.co/generate)
- Update gradients using [CSS Gradient Generator](https://cssgradient.io) with alpha channels
- Add rounded borders, shadows, or other modern styling touches
- Learn more about [CSS gradients](https://www.w3schools.com/css/css3_gradients.asp)

### Personalization
- Replace placeholder projects with your actual work from class
- Update the hero image with your own photo or a professional image from [Pexels](https://www.pexels.com)
- Customize the branding and text to reflect your personal brand

## Additional Resources
- [W3Schools Portfolio Gallery Tutorial](https://www.w3schools.com/howto/howto_css_portfolio_gallery.asp) - Original tutorial this project is based on
- [W3Schools Hero Image Tutorial](https://www.w3schools.com/howto/howto_css_hero_image.asp) - Hero section implementation
- [React Component Documentation](https://react.dev/learn/your-first-component) - Learn React components
- [React Props Documentation](https://react.dev/learn/passing-props-to-a-component) - Understanding props
- [React Children Documentation](https://react.dev/learn/passing-props-to-a-component#passing-jsx-as-children) - Using children props

## Success Criteria
- ✅ App.jsx is significantly simplified and readable
- ✅ At least 7 new components created and properly organized
- ✅ Components use props appropriately
- ✅ At least one component uses children props
- ✅ Project data is managed in an array and rendered with `.map()`
- ✅ Styling reflects your personal brand and aesthetic
- ✅ All components are in separate files in the `./components` directory
- ✅ Commit frequently. Each milestone should have its own descriptive commit message.

## Getting Started

Start your project with the vite starter code.

```bash
npm create vite@latest
```

Remove the CSS from `index.css` and replace the `App.jsx` and `App.css` content with the starter code from bellow. Then add the `./components/HeroImage.jsx` and `./components/HeroImage.css` files with the starter code from bellow as well.

Finally, copy the images from the [public folder](./public) or find your own.

Commit after each milestone.

### Starter Code

```jsx
// App.jsx
import './App.css'
import HeroImage from './components/HeroImage'

function App() {

  return (
    <>
      <HeroImage />
      {/* MAIN (Center website) */}
      <div className="main">

        <h1>MYLOGO.COM</h1>
        <hr />

        <h2>PORTFOLIO</h2>
        <p>Resize the browser window to see the responsive effect.</p>

        {/* Portfolio Gallery Grid */}
        <div className="row">
          <div className="column">
            <div className="content">
              <img src="/mountains.jpg" alt="Mountains" className="project-image" />
              <h3>My Work</h3>
              <p>Lorem ipsum..</p>
            </div>
          </div>
          <div className="column">
            <div className="content">
              <img src="/lights.jpg" alt="Lights" className="project-image" />
              <h3>My Work</h3>
              <p>Lorem ipsum..</p>
            </div>
          </div>
          <div className="column">
            <div className="content">
              <img src="/nature.jpg" alt="Nature" className="project-image" />
              <h3>My Work</h3>
              <p>Lorem ipsum..</p>
            </div>
          </div>
          <div className="column">
            <div className="content">
              <img src="/mountains.jpg" alt="Mountains" className="project-image" />
              <h3>My Work</h3>
              <p>Lorem ipsum..</p>
            </div>
          </div>
        </div>

        <div className="content">
          <img src="/bear.jpg" alt="Bear" className="project-image" />
          <h3>Some Other Work</h3>
          <p>Lorem ipsum..</p>
        </div>

        {/* END MAIN */}
      </div>
    </>
  )
}

export default App
```

```css
/* App.css */
* {
  box-sizing: border-box;
}

/* Center website */
.main {
  max-width: 1000px;
  margin: auto;
}

h1 {
  font-size: 50px;
  word-break: break-all;
}

.row {
  margin: 8px -16px;
}

/* Add padding BETWEEN each column (if you want) */
.row,
.row > .column {
  padding: 8px;
}

/* Create four equal columns that floats next to each other */
.column {
  float: left;
  width: 25%;
}

/* Clear floats after rows */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* Content */
.content {
  background-color: white;
  padding: 10px;
}

/* Project Image */
.project-image {
  width: 100%;
}

/* Responsive layout - makes a two column-layout instead of four columns */
@media screen and (max-width: 900px) {
  .column {
    width: 50%;
  }
}

/* Responsive layout - makes the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 600px) {
  .column {
    width: 100%;
  }
}
```

```jsx
// ./components/HeroImage.jsx
import "./HeroImage.css";

export default function HeroImage() {
    return (
        <>
            <div className="hero-image">
                <div className="hero-text">
                    <h1>I am Jane Doe</h1>
                    <p>And I'm a Photographer</p>
                    <button>Hire me</button>
                </div>
            </div>
        </>
    );
}
```

```css
/* ./components/HeroImage.css */
.hero-image {
  /* Use "linear-gradient" to add a darken background effect to the image (photographer.jpg). This will make the text easier to read */
  background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("/photographer.jpg");

  /* Set a specific height */
  height: 100vh;

  /* Position and center the image to scale nicely on all screens */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative;
}

/* Place text in the middle of the image */
.hero-text {
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
}
```