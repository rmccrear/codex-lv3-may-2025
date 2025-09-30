# 🧑‍💻 React Lesson: Pokémon Resume

---

## 🎯 Learning Goals

* Practice writing **no-props components** (`AboutMe`, `Education`, `Footer`).
* Practice writing **props components** (`ExperienceItem`, `SkillItem`, `ContactEmail`).
* Understand how each small piece contributes to a complete page.

---

## 🚀 Starter Code

```jsx
import React from "react";

// ===== No-Props Components (given) =====
function Avatar() {
  return (
    <img
      src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
      alt="Pikachu"
      width={100}
      height={100}
    />
  );
}

function Name() {
  return <h1>Ash Ketchum</h1>;
}

function JobTitle() {
  return <h2>Pokémon Trainer</h2>;
}

// ===== Exercises (students write these!) =====
// TODO: Write an AboutMe component (no props)
// TODO: Write an Education component (no props)
// TODO: Write a Footer component (no props)

// TODO: Write an ExperienceItem component (with props: role, company, years)
// TODO: Write a SkillItem component (with props: name)
// TODO: Write a ContactEmail component (with props: email)

// ===== Provided ContactPhone (example with props) =====
function ContactPhone({ phone }) {
  return <p>Phone: {phone}</p>;
}

// ===== Main App =====
export default function App() {
  return (
    <div>
      {/* Header */}
      <Avatar />
      <Name />
      <JobTitle />

      {/* Contact */}
      <h3>Contact</h3>

      <ContactPhone phone="(555) 123-POKE" />

      {/* Footer */}

    </div>
  );
}
```

---

## 📝 Exercise Instructions

👉 Students must implement the missing components:

1. **AboutMe** (no props)
   Returns a `<p>` with the text:
   `I travel across the land, searching far and wide to catch 'em all!`

2. **Education** (no props)
   Returns a `<p>` with the text:
   `Graduated from Pallet Town Pokémon Training Academy (1996)`

3. **Footer** (no props)
   Returns a `<footer>` with the text:
   `© 2025 Pokémon Resume`

4. **ExperienceItem** (with props)
   Should return a `<p>` that displays:

   ```
   <strong>{role}</strong> — {company} ({years})
   ```

5. **SkillItem** (with props)
   Should return a `<p>` that displays the skill name.

6. **ContactEmail** (with props)
   Should return a `<p>` with the format:
   `Email: {email}`

