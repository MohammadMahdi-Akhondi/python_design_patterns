# Singleton

Singleton is a creational design pattern that lets you ensure that a class has only one instance, \
while providing a global access point to this instance.


## Applications
- Use the Singleton pattern when a class in your program should have just a single instance available to all clients; 
for example, a single database object shared by different parts of the program.

- Use the Singleton pattern when you need stricter control over global variables.

## Explanation simple logger

In this example I implemented the singleton pattern for logger object.
this example behaves incorrectly in a multithreaded environment. 
Multiple threads can call the creation method simultaneously and get several instances of Singleton class.

## Explanation advance logger

In this example I implemented the singleton pattern for logger object.
In this example, multiple threads cannot simultaneously receive multiple instances of the Singleton class.

## Contributing
I welcome contributions from everyone! If you have an idea for a new example or an improvement for an existing one, please fork the repository and submit a pull request.
