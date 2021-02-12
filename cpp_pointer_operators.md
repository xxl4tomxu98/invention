C++ & and * Operators
By Matt Butrovich (edits by Tej Vuligonda and Jason Kreinberg)

// ref_pointer_operators
// Clarifying & and * operators


// C++ loves to reuse keywords and operators, so it's no surprise that students
// can become confused by * and & showing up everywhere in code with different
// results. Let's see if we can clear that up a bit...

#include <iostream>

int main()
{
     int a {4};
     // a is an integer.
     a = 7;
     // a can be assigned values that are integral

     // ----- The & Operator -----

     int& ra = a;
     // When & is placed in front of a name during a variable declaration, that
     // means that a "reference to" is being declared. ra's declarations reads
     // that ra is a reference to an integer. As such, it can only be assigned an
     // l-value, in this case a. For example...

     // int& rb = 9;

     // ...doesn't work. 9 is an r-value and can't have a reference to it, at
     // least not with this syntax. It's also worth noting that references must
     // be initialized at declaration. For example...

     // int& rc;

     // ...doesn't work. &rc needs to be initialized.
     // The most frequent use of reference declarations is in the parameter list
     // of a function. Declaring a parameter as a reference allows a function to
     // modify the original argument, rather than being passed a local copy that
     // is restricted to the scope of the function.

     // One final comment about reference initialization: Once a reference is
     // initialized, it is a reference that is constant. Note that this does not
     // mean that the data it refers to is constant, only that where it refers
     // cannot be changed. For example, you might think that this code...

     int b {5};            // ...which creates a new integer variable with a value
     ra = b;                     // of 5, and then assigns b to ra, would result in ra
     b = 6;                      // referencing b instead of a.

     // Instead, what happened is that a got assigned the value of b, because ra
     // is forever a reference to a. b is then changed to 6, and we can try
     // printing a, b, and ra...

     std::cout << a << b << ra << std::endl;

     // ... which results in 565, or numbers that correspond to the variable aba
     // respectively.

     &a;

     // putting & in front of a variable name denotes "address of" in C++. The
     // result of this expression is an r-value address of a. That doesn't seem
     // terribly interesting until we get to the next operator...

     // ----- The * Operator -----

     int* pa;

     // When * is placed in front of a name during a variable declaration, that
     // means that a "pointer to" is being declared. pa's declaration reads that
     // pa is a pointer to an integer. As such, it can only be assigned a memory
     // address to point to. For example...

/* Visually this can be represented as pa -> (an integer)
* This integer value needs to be initialized
*/


     pa = &a;

     // If we use the & operator to get the address of a, we can assign that
     // value into pa to make it a pointer to a;
    
/* Visually this can be represented as pa -> (address of a)*/

     *pa;

     // Putting * in front of a variable name denotes "dereference" in C++. The
     // result of this expression is an l-value corresponding to the data pointed
     // to by pa. Currently that value is 5, so if we want to print a by using
     // the pointer pa, the syntax is...

/* Visually this can be represented as pa -> (a = 5)
* Deferencing pa gives us the value of a or a = 5.
*/

     std::cout << *pa << std::endl;

     // If we didn't put the dereference operator, we would instead be printing
     // the raw memory value that pa represents.
    
/*This raw memory value is usually not very useful for high-level programming*/

     pa = new int {9};

     // Perhaps the most common use of a raw/dumb pointer is when using dynamic
     // memory allocation to put objects on the heap. Using pointers to stack
     // allocated items can be risky because you don't really have ownership of
     // that memory, and as such don't have as much control over object lifetime.
     // You can easily end up with dangling pointers (pointer to memory that
     // isn't what you think it is anymore) that can crash your program, or at
     // best produce unexpected results. In this case though, we've allocated a
     // new int on the heap with the value of 9, and pa now points to it. Any
     // time the new keyword is used, a memory address is returned, so a pointer
     // is the correct type to use to store that information. You might have
     // noticed that we reused pa without issue. Unlike references, pointers are
     // not constant unless explicitly declared as such. They can be reassigned
     // to other memory addresses at any time.

     *pa = 2;

/*Visually, this can be represented as:
* pa -> (a=5) x
* pa -> (2)
*/

     // If we want to change the value that pa points to, we first dereference
     // it, and then assign into it.

     delete pa;

     // We don't want to leak memory, so we delete the object pointed to by pa.
     return 0;
}

// Summary:

//    & when used with a variable declaration: "reference to"
//    Example: int &ra = a;
//    "ra is a reference to a"

//    * when used with a variable declaration: "pointer to"
//    Example: int *pa;
//    "pa is a pointer to an integer"

//    & when used with an already declared variable: "address of"
//    Example: &a;
//    "address of a"

//    * when used with an already declared pointer: "dereference"
//    Example: std::cout << *pa << std::endl;
//    "print the underlying value of a"