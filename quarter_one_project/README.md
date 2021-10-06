# quarter one project

> My quarter one project is a simple calculator. It is made using python.

![calculator_test](https://raw.githubusercontent.com/YazeedAlKhalaf/grade_12_ict_projects/main/qurater_one_project/assets/calculator_test.gif)

## ✨ Features

- ➕ Add two numbers.
- ➖ Subtract two numbers.
- ✖️ Multiply two numbers.
- ➗ Divide two numbers.
- 🚪 Exit the calculator.
- 🔋 Batteries included!

## Code2Flow Code:

```
START;
while(active) {
  print menu for the user;
  /get option from the user/;
  if (user_choice <= 4 and user_choice != 0) {
    /get first number from the user/;
    /get the second number from the user/;
  }
  
  if (user_choice == 1) {
            result = add(first, second);
        }else if (user_choice == 2) {
            result = subtract(first, second);
        } else if (user_choice == 3) {
            result = multiply(first, second);
        }else if (user_choice == 4) {
            result = divide(first, second);
        }else if (user_choice == 0)
            print("Good Bye 👋");
        }else {
            print("This choice is not listed in the options.");
  }
END;
```