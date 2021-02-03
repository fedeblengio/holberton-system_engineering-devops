# Tasks:
# 0. <o>
  Create a script that creates an alias.
- Name: ls
- Value: rm *
>```0-alias```
# 1. Hello you 
  Create a script that prints ```hello user```, where user is the current Linux user.
  > File: 1-hello_you
  
  # 2. The path to success is to take massive, determined action
  Add ```/action``` to the ```PATH```. ```/action``` should be the last directory the shell looks into when looking for a program.
  > File: 2-path
  
  # 3. If the path be beautiful, let us not ask where it leads
  Create a script that counts the number of directories in the ```PATH```.
  > File: 3-paths
  # 4. Global variables 
  Create a script that lists environment variables.
  > File: 4-global_variables
  # 5. Local variables 
  Create a script that lists all local variables and environment variables, and functions.
  > File: 5-local_variables
  # 6. Local variable
  Create a script that creates a new local variable.
  - Name: BETTY
- Value: Holberton
> File: 6-create_local_variable

# 7. Global variable 
Create a script that creates a new global variable.
- Name: HOLBERTON
- Value: Betty
> File: 7-create_global_variable

# 8. Every addition to true knowledge is an addition to human power 
Write a script that prints the result of the addition of 128 with the value stored in the environment variable ```TRUEKNOWLEDGE```, followed by a new line.
- ```export TRUEKNOWLEDGE=1209```
- ``` ./8-true_knowledge | cat -e```
> File: 8-true_knowledge

# 9. Divide and rule
Write a script that prints the result of ```POWER``` divided by ```DIVIDE```, followed by a new line.
- ```POWER``` and ```DIVIDE``` are environment variables
- ``` export POWER=42784```
- ```export DIVIDE=32```
- ```./9-divide_and_rule | cat -e```
> File: 9-divide_and_rule

# 10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath 
Write a script that displays the result of ```BREATH``` to the power ```LOVE```
- ```BREATH``` and ```LOVE``` are environment variables
- The script should display the result, followed by a new line
- ```export BREATH=4 ```
- ```export LOVE=3```
- ```./10-love_exponent_breath ```
> File: 10-love_exponent_breath

# There are 10 types of people in the world -- Those who understand binary, and those who don't 
Write a script that converts a number from base 2 to base 10.

- The number in base 2 is stored in the environment variable ```BINARY```
- The script should display the number in base 10, followed by a new line
- ```export BINARY=10100111001```
- ```./11-binary_to_decimal```
> File: 11-binary_to_decimal

# 12. Combination 
Create a script that prints all possible combinations of two letters, except oo.

- Letters are lower cases, from ```a``` to ```z```
- One combination per line
- The output should be alpha ordered, starting with``` aa```
- Do not print ```oo```
- Your script file should contain maximum 64 characters

> File: 12-combinations

# 13. Floats
Write a script that prints a number with two decimal places, followed by a new line.

The number will be stored in the environment variable ```NUM```.
- ```export NUM=0```
- ```./13-print_float```
> File: 13-print_float

# 14. Decimal to Hexadecimal 
Write a script that converts a number from base 10 to base 16.

The number in base 10 is stored in the environment variable ```DECIMAL```
The script should display the number in base 16, followed by a new line

- ```export DECIMAL=16```
- ```./14-decimal_to_hexadecimal```
> File: 14-decimal_to_hexadecimal

# 15. What is the difference between a hard link and a symbolic link? 
Write a blog post explaining what are hard and symbolic links on Linux, how to create them, and what is the difference between the two. Use examples to illustrate.

- Have at least one picture, at the top of the blog post
- Publish your blog post on Medium or LinkedIn
- Share your blog post at least on LinkedIn
When done, please add all urls below (blog post, LinkedIn post, etc.)

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings

# 16. Everyone is a proponent of strong encryption

Write a script that encodes and decodes text using the rot13 encryption. Assume ASCII.
> File: 100-rot13

# 17. The eggs of the brood need to be an odd number 
Write a script that prints every other line from the input, starting with the first line.



> File: 101-odd

# 18. I'm an instant star. Just add water and stir. 
Write a shell script that adds the two numbers stored in the environment variables ```WATER``` and ```STIR``` and prints the result.

- ```WATER``` is in base ```water```
- ```STIR``` is in base ```stir```.
- The result should be in base ```behlnort```
- export WATER="ewwatratewa"
- export STIR="ti.itirtrtr"
- ./102-water_and_stir
```holberton```









