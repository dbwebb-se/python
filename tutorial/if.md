If, else if, else
==============================



```
/**
 * Do something if a variable has a certain value.
 */
var val = true;

if (val) {
    console.log("YES");
}

// Above is the same as this
if (val == true) {
    console.log("YES");
}



/**
 * Add an else statement.
 */
if (val) {
    console.log("YES");
} 
else {
    console.log("NO");
}



/**
 * Use many if-tests.
 */
if (val === true) {
    console.log("TRUE");
} 
else if (val === false) {
    console.log("FALSE");
} 
else if (val === null) {
    console.log("NULL");
} 
else {
    console.log("NO");
}


```



Reference and read more
------------------------------

[MDN if...else](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)



Revision history
------------------------------

2014-06-02 (mos) PA1 First try.

