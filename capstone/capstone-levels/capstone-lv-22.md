Level Navigation: [1](./capstone-lv-1.md) | [2](./capstone-lv-2.md) | [3](./capstone-lv-3.md) | [4](./capstone-lv-4.md) | [5](./capstone-lv-5.md) | [6](./capstone-lv-6.md) | [7](./capstone-lv-7.md) | [8](./capstone-lv-8.md) | [9](./capstone-lv-9.md) | [10](./capstone-lv-10.md) | [11](./capstone-lv-11.md) | [12](./capstone-lv-12.md) | [13](./capstone-lv-13.md) | [14](./capstone-lv-14.md) | [15](./capstone-lv-15.md) | [16](./capstone-lv-16.md) | [17](./capstone-lv-17.md) | [18](./capstone-lv-18.md) | [19](./capstone-lv-19.md) | [20](./capstone-lv-20.md) | [21](./capstone-lv-21.md) | **Current Level:** 22 | [23](./capstone-lv-23.md) | [24](./capstone-lv-24.md) | [25](./capstone-lv-25.md) | [26](./capstone-lv-26.md) | [27](./capstone-lv-27.md) | [28](./capstone-lv-28.md) | [29](./capstone-lv-29.md) | [30](./capstone-lv-30.md) | [31](./capstone-lv-31.md) | [32](./capstone-lv-32.md) | [33](./capstone-lv-33.md) | [34](./capstone-lv-34.md)

---

# Level 22: AI Interaction Design

## What You'll Do
Design and implement user interactions that make your AI calls more dynamic and engaging. This is where you can really showcase your creativity with AI! Think about how users will interact with your AI - will they ask questions, give instructions, or explore different AI personalities? Consider what would make your AI app feel magical and intuitive. This is your opportunity to create something that demonstrates the power of AI while being fun and useful for your users.

## Instructions
- Think about how you want your user to interact with your AI and what makes it special
- Consider different AI interaction patterns:
  - **Question-Answer:** Users ask questions and get AI responses
  - **Creative Writing:** Users provide prompts and get AI-generated stories, poems, or content
  - **Personality Chat:** Users chat with an AI that has a specific personality (pirate, robot, etc.)
  - **Task Assistant:** Users give instructions and AI helps complete tasks
  - **Interactive Story:** Users make choices that influence AI-generated story outcomes
  - **Multi-turn Conversations:** Users have ongoing conversations with context
  - **Special Challenge - Data-Enhanced AI:** Use your API data to create richer, more personalized AI prompts (e.g., "Based on the weather in [city], write a poem about the day" or "Create a story using this Pokemon's stats: [pokemon data]")
- Choose the AI interaction pattern that best fits your vision and user needs
- Implement your chosen AI interaction pattern
- Test different prompts and responses to ensure your AI feels engaging
- Remember to test as you go, as we did in the previous levels

## 💡 Code Hints
Need help with AI interactions? Check out these snippets:
- **AI calls:** See [SNIPPETS.md](../SNIPPETS.md#hugging-face-generated-code) for AI integration examples
- **Input handling:** Use `getValue()` to get user input and add it to your AI prompt
- **Data-enhanced prompts:** Combine your API data with AI prompts using template literals:
  ```js
  let prompt = `Based on the weather in ${cityName}: ${weatherDescription}, write a creative story about the day.`;
  ```
- **Response formatting:** Use template literals to format AI responses nicely
- **Conditional logic:** Use `if` statements to handle different user inputs or AI responses

## ✅ Check
1. Open your webpage in a browser
2. Test your chosen AI interaction pattern:
   - If using question-answer, try different types of questions
   - If using creative writing, test different prompt styles
   - If using personality chat, verify the AI maintains its character
   - If using task assistance, test different types of tasks
   - If using data-enhanced AI, test with different API data to see how it affects AI responses
3. Verify that your AI calls work smoothly with the user interactions
4. Make sure the AI responses feel engaging and relevant to user inputs
5. Test edge cases like empty inputs or very long prompts
6. If using API data in prompts, verify the data is properly formatted and the AI uses it meaningfully (see [Preformatted Raw Text Formatting with CSS](../SNIPPETS.md#-preformatted-raw-text-formatting-with-css) for formatting help)

---

<!-- LEVEL_END -->


---

Level Navigation: [1](./capstone-lv-1.md) | [2](./capstone-lv-2.md) | [3](./capstone-lv-3.md) | [4](./capstone-lv-4.md) | [5](./capstone-lv-5.md) | [6](./capstone-lv-6.md) | [7](./capstone-lv-7.md) | [8](./capstone-lv-8.md) | [9](./capstone-lv-9.md) | [10](./capstone-lv-10.md) | [11](./capstone-lv-11.md) | [12](./capstone-lv-12.md) | [13](./capstone-lv-13.md) | [14](./capstone-lv-14.md) | [15](./capstone-lv-15.md) | [16](./capstone-lv-16.md) | [17](./capstone-lv-17.md) | [18](./capstone-lv-18.md) | [19](./capstone-lv-19.md) | [20](./capstone-lv-20.md) | [21](./capstone-lv-21.md) | **Current Level:** 22 | [23](./capstone-lv-23.md) | [24](./capstone-lv-24.md) | [25](./capstone-lv-25.md) | [26](./capstone-lv-26.md) | [27](./capstone-lv-27.md) | [28](./capstone-lv-28.md) | [29](./capstone-lv-29.md) | [30](./capstone-lv-30.md) | [31](./capstone-lv-31.md) | [32](./capstone-lv-32.md) | [33](./capstone-lv-33.md) | [34](./capstone-lv-34.md)
