Name(s)\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Period \_\_\_\_\_\_ Date \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

|  | Activity Guide \- Conditionals Make | ![][image1] |
| :---- | :---- | :---- |

**Step 1 \- Try the app**  
Try making tickets for different combinations of inputs. 

* Make a ticket for a weekend.  
* Make a ticket for a weekday (Monday \- Friday) and someone 18 or younger.  
* Try the discount code "FREEFRIDAY" on a Friday.

Discuss with a Partner

* What variables would you need to program this app?  
* Where does this app use conditionals (if-statements)?

**Step 2 \- Plan**  
**Variables:** Fill in the table below for each variable you'll need to create.

| Variable Name | What the Variable Stores |
| :---- | :---- |
|  |   |
|  |   |
|  |   |

**Conditionals**: Draw a flowchart that follows the rules below. There's more than one way to do it. Use the table to make sure that your flowchart works for different combinations of age, day, and discount code.

* On the weekends ("Saturday" and "Sunday") everyone pays full price of $10  
* On weekdays (Monday through Friday) if you are 18 years or younger you pay $5.  
* If you use the discount code "FREEFRIDAY" on a Friday you get in for $0. No other discount codes will work and the code only works on Fridays.

**Test Cases**

| Age | Day | Discount Code | Price |
| :---: | :---: | :---: | :---: |
| 18 | Monday | *none* | $5 |
| 18 | Saturday | *none* | $10 |
| 50 | Monday | *none* | $10 |
| 50 | Saturday | *none* | $10 |
| 18 | Tuesday | FREEFRIDAY | $5 |
| 50 | Friday | FREEFRIDAY | $0 |
| 18 | Friday | FREE | $5 |
| 50 | Friday | FREE | $10 |

**Step 3 \- Write Your Code**

* Write the code for the app, using your plan above and the comments provided in Code Studio to help  
* Step You Can Follow  
  * Create all the variables from your table above.  
  * Give your variables a starting value using the assignment operator (=)  
  * Create an event handler (onEvent) for the "calculate\_button"  
  * Inside the event handler start writing code for your conditional using your flowchart  
  * Test your code as you go using the table below. At the end it should work for every combination of outputs in the table on the first page.  
  * Use your debugging skills to identify unexpected behavior and fix your program  
  * Comment your code as you go, explaining what each event handler does  
* Check the Help & Tips tab for ideas about Programming Patterns you can use  
* Extension Ideas  
  * Add another discount code for a different day of the week or age range  
  * Make guests 65 and older always pay $5 unless they use a discount code

**Step 4 \- Submit**  
Before you submit, check the rubric below to make sure your program meets the requirements of the task. 

| Category | Extensive Evidence | Convincing Evidence | Limited Evidence | No Evidence |
| :---- | ----- | ----- | ----- | ----- |
| Input | onEvents are created for all the required inputs.  | onEvents are created for most of the inputs.  | onEvents are created for some of the inputs.  | onEvents are not created for any inputs.  |
| Storage: Variables | Variables are created and appropriately used for all pieces of information used in the app. | Most information is stored in a variable and appropriately updated throughout the app. | Some information is stored in a variable and appropriately updated throughout the app. | There are no variables which store the necessary information for the app to work correctly. |
| Processing: Conditional Logic  | The code correctly determines the price for all combinations of inputs (age, price, discount code). | The code correctly determines the price for most but not all combinations of inputs (age, price, discount code). | The code correctly determines the price for some but not all combinations of inputs (age, price, discount code). | The code does not correctly determine the price for any combination of inputs (age, price, discount code). |
| Code: Output | The screen correctly displays the day, age, and price of the ticket. | The screen displays most but not all information correctly in the ticket. | The screen displays some but not all information correctly in the ticket. | The screen does not correctly display any information in the ticket. |
| Code runs without errors. | No errors are present in the required code. | On or two errors are present in the required code. | Three or four errors are present in the required code. | More than four errors are present in the required code.  |
| Coding Comments | Comments are used to correctly explain the purpose and function of all onEvents and conditional logic. | Comments are used to explain the purpose and function of most onEvents and conditional logic. | Comments are used to explain the purpose and function of some onEvents and conditional logic. | Comments are not present. |

**Step 5 \-  Create Performance Task Writing Practice**

This question is based on the project you submitted.

Describe a Boolean expression in your program that uses a relational operator. Explain what this expression does and how it influences the program’s behavior.

|  |
| :---- |

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAsCAMAAAApWqozAAADAFBMVEVHcEwHCQp/f39AQUIbHR4ICgv+/v5ERUWLi4u/v7/k5OUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXFP+GAAAABXRSTlMA6SeAxYST9hIAAACGSURBVHhe7ZHbDoAgDEO5yP9/MEFUxnCsYkw0PnFeGkIpS2fMZPIBVh2XIpFV3hnj+iN5Tu1R5h1bP2MVYEQmsVUlmHwDmn0okgNe4RgpkaomDtTzVekLdD80cGzaocbgt+TVDDZ4DfbTNojpGMWb87VCASYzGetDM//unozBdf26wclkxAZzwxQ/NrCQGwAAAABJRU5ErkJggg==>