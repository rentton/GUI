# GUI
Graphic interfaces using Python tkinter library 

-----------------------------------------------------------------------------------------------------
## Calculator:
* The calculator can:
  - Know if the syntax of the expression is valid or not (e.g. x-2/ is not valid)
  - Know if the math of the expression is valid or not (e.g. 2/0 is not valid)
  - Calculate operations between integers with =
  - Delete the actual expression with AC
Note: The result of operations will be always an integer number, so round procces are used.

* Important points:
  1. To know if the expression is valid, I've used a LEX program (coded for me too) called  **ArithmeticalAnalizer**. 
 You can find it in this repo or in https://github.com/rentton/learning/blob/master/FormalLanguagesAndCompilers/ArithmeticAnalizer.py.
  2. The calculator understand the order of the operations because of reverse Polish notation (also called postfix notation). 
 The modules that coding this are *postfix* and * op_condition * (both commented) and the var hierarchy that represent for each operator his priority (less number, more priority).
 ![Screenshot](Captura.png)
 

-----------------------------------------------------------------------------------------------------

