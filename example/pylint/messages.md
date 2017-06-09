# Pylint error codes
## :blacklisted-name
---
#### (C0102):
Used when the name is listed in the black list (unauthorized names).
## :invalid-name
---
#### (C0103):
Used when the name doesn't match the regular expression associated to its type
(constant, variable, class...).
## :missing-docstring
---
#### (C0111):
Used when a module, function, class or method has no docstring.Some special
methods like __init__ doesn't necessary require a docstring.
## :empty-docstring
---
#### (C0112):
Used when a module, function, class or method has an empty docstring (it would
be too easy ;).
## :unneeded-not
---
#### (C0113):
Used when a boolean expression contains an unneeded negation.
## :singleton-comparison
---
#### (C0121):
Used when an expression is compared to singleton values like True, False or
None.
## :misplaced-comparison-constant
---
#### (C0122):
Used when the constant is placed on the left sideof a comparison. It is
usually clearer in intent to place it in the right hand side of the
comparison.
## :unidiomatic-typecheck
---
#### (C0123):
The idiomatic way to perform an explicit typecheck in Python is to use
isinstance(x, Y) rather than type(x) == Y, type(x) is Y. Though there are
unusual situations where these give different results.
## :consider-using-enumerate
---
#### (C0200):
Emitted when code that iterates with range and len is encountered. Such code
can be simplified by using the enumerate builtin.
## :consider-iterating-dictionary
---
#### (C0201):
Emitted when the keys of a dictionary are iterated through the .keys() method.
It is enough to just iterate through the dictionary itself, as in "for key in
dictionary".
## :bad-classmethod-argument
---
#### (C0202):
Used when a class method has a first argument named differently than the value
specified in valid-classmethod-first-arg option (default to "cls"),
recommended to easily differentiate them from regular instance methods.
## :bad-mcs-method-argument
---
#### (C0203):
Used when a metaclass method has a first agument named differently than the
value specified in valid-classmethod-first-arg option (default to "cls"),
recommended to easily differentiate them from regular instance methods.
## :bad-mcs-classmethod-argument
---
#### (C0204):
Used when a metaclass class method has a first argument named differently than
the value specified in valid-metaclass-classmethod-first-arg option (default
to "mcs"), recommended to easily differentiate them from regular instance
methods.
## :line-too-long
---
#### (C0301):
Used when a line is longer than a given number of characters.
## :too-many-lines
---
#### (C0302):
Used when a module has too much lines, reducing its readability.
## :trailing-whitespace
---
#### (C0303):
Used when there is whitespace between the end of a line and the newline.
## :missing-final-newline
---
#### (C0304):
Used when the last line in a file is missing a newline.
## :trailing-newlines
---
#### (C0305):
Used when there are trailing blank lines in a file.
## :multiple-statements
---
#### (C0321):
Used when more than on statement are found on the same line.
## :superfluous-parens
---
#### (C0325):
Used when a single item in parentheses follows an if, for, or other keyword.
## :bad-whitespace
---
#### (C0326):
Used when a wrong number of spaces is used around an operator, bracket or
block opener.
## :mixed-line-endings
---
#### (C0327):
Used when there are mixed (LF and CRLF) newline signs in a file.
## :unexpected-line-ending-format
---
#### (C0328):
Used when there is different newline than expected.
## :bad-continuation
---
#### (C0330):
TODO
## :wrong-spelling-in-comment
---
#### (C0401):
Used when a word in comment is not spelled correctly.
## :wrong-spelling-in-docstring
---
#### (C0402):
Used when a word in docstring is not spelled correctly.
## :invalid-characters-in-docstring
---
#### (C0403):
Used when a word in docstring cannot be checked by enchant.
## :multiple-imports
---
#### (C0410):
Used when import statement importing multiple modules is detected.
## :wrong-import-order
---
#### (C0411):
Used when PEP8 import order is not respected (standard imports first, then
third-party libraries, then local imports)
## :ungrouped-imports
---
#### (C0412):
Used when imports are not grouped by packages
## :wrong-import-position
---
#### (C0413):
Used when code and imports are mixed
## :syntax-error
---
#### (E0001):
Used when a syntax error is raised for a module.
## :unrecognized-inline-option
---
#### (E0011):
Used when an unknown inline option is encountered.
## :bad-option-value
---
#### (E0012):
Used when a bad value for an inline option is encountered.
## :init-is-generator
---
#### (E0100):
Used when the special class method __init__ is turned into a generator by a
yield in its body.
## :return-in-init
---
#### (E0101):
Used when the special class method __init__ has an explicit return value.
## :function-redefined
---
#### (E0102):
Used when a function / class / method is redefined.
## :not-in-loop
---
#### (E0103):
Used when break or continue keywords are used outside a loop.
## :return-outside-function
---
#### (E0104):
Used when a "return" statement is found outside a function or method.
## :yield-outside-function
---
#### (E0105):
Used when a "yield" statement is found outside a function or method.
## :nonexistent-operator
---
#### (E0107):
Used when you attempt to use the C-style pre-increment orpre-decrement
operator -- and ++, which doesn't exist in Python.
## :duplicate-argument-name
---
#### (E0108):
Duplicate argument names in function definitions are syntax errors.
## :abstract-class-instantiated
---
#### (E0110):
Used when an abstract class with `abc.ABCMeta` as metaclass has abstract
methods and is instantiated.
## :bad-reversed-sequence
---
#### (E0111):
Used when the first argument to reversed() builtin isn't a sequence (does not
implement __reversed__, nor __getitem__ and __len__
## :too-many-star-expressions
---
#### (E0112):
Emitted when there are more than one starred expressions (`*x`) in an
assignment. This is a SyntaxError. This message can't be emitted when using
Python < 3.0.
## :invalid-star-assignment-target
---
#### (E0113):
Emitted when a star expression is used as a starred assignment target. This
message can't be emitted when using Python < 3.0.
## :star-needs-assignment-target
---
#### (E0114):
Emitted when a star expression is not used in an assignment target. This
message can't be emitted when using Python < 3.0.
## :nonlocal-and-global
---
#### (E0115):
Emitted when a name is both nonlocal and global. This message can't be emitted
when using Python < 3.0.
## :continue-in-finally
---
#### (E0116):
Emitted when the `continue` keyword is found inside a finally clause, which is
a SyntaxError.
## :nonlocal-without-binding
---
#### (E0117):
Emitted when a nonlocal variable does not have an attached name somewhere in
the parent scopes This message can't be emitted when using Python < 3.0.
## :method-hidden
---
#### (E0202):
Used when a class defines a method which is hidden by an instance attribute
from an ancestor class or set by some client code.
## :access-member-before-definition
---
#### (E0203):
Used when an instance member is accessed before it's actually assigned.
## :no-method-argument
---
#### (E0211):
Used when a method which should have the bound instance as first argument has
no argument defined.
## :no-self-argument
---
#### (E0213):
Used when a method has an attribute different the "self" as first argument.
This is considered as an error since this is a so common convention that you
shouldn't break it!
## :invalid-slots-object
---
#### (E0236):
Used when an invalid (non-string) object occurs in __slots__.
## :assigning-non-slot
---
#### (E0237):
Used when assigning to an attribute not defined in the class slots.
## :invalid-slots
---
#### (E0238):
Used when an invalid __slots__ is found in class. Only a string, an iterable
or a sequence is permitted.
## :inherit-non-class
---
#### (E0239):
Used when a class inherits from something which is not a class.
## :inconsistent-mro
---
#### (E0240):
Used when a class has an inconsistent method resolutin order.
## :duplicate-bases
---
#### (E0241):
Used when a class has duplicate bases.
## :non-iterator-returned
---
#### (E0301):
Used when an __iter__ method returns something which is not an iterable (i.e.
has no `__next__` method)
## :unexpected-special-method-signature
---
#### (E0302):
Emitted when a special method was defined with an invalid number of
parameters. If it has too few or too many, it might not work at all.
## :invalid-length-returned
---
#### (E0303):
Used when an __len__ method returns something which is not a non-negative
integer
## :import-error
---
#### (E0401):
Used when pylint has been unable to import a module.
## :used-before-assignment
---
#### (E0601):
Used when a local variable is accessed before it's assignment.
## :undefined-variable
---
#### (E0602):
Used when an undefined variable is accessed.
## :undefined-all-variable
---
#### (E0603):
Used when an undefined variable name is referenced in __all__.
## :invalid-all-object
---
#### (E0604):
Used when an invalid (non-string) object occurs in __all__.
## :no-name-in-module
---
#### (E0611):
Used when a name cannot be found in a module.
## :unbalanced-tuple-unpacking
---
#### (E0632):
Used when there is an unbalanced tuple unpacking in assignment
## :unpacking-non-sequence
---
#### (E0633):
Used when something which is not a sequence is used in an unpack assignment
## :bad-except-order
---
#### (E0701):
Used when except clauses are not in the correct order (from the more specific
to the more generic). If you don't fix the order, some exceptions may not be
catched by the most specific handler.
## :raising-bad-type
---
#### (E0702):
Used when something which is neither a class, an instance or a string is
raised (i.e. a `TypeError` will be raised).
## :bad-exception-context
---
#### (E0703):
Used when using the syntax "raise ... from ...", where the exception context
is not an exception, nor None. This message can't be emitted when using Python
< 3.0.
## :misplaced-bare-raise
---
#### (E0704):
Used when a bare raise is not used inside an except clause. This generates an
error, since there are no active exceptions to be reraised. An exception to
this rule is represented by a bare raise inside a finally clause, which might
work, as long as an exception is raised inside the try block, but it is
nevertheless a code smell that must not be relied upon.
## :raising-non-exception
---
#### (E0710):
Used when a new style class which doesn't inherit from BaseException is
raised.
## :notimplemented-raised
---
#### (E0711):
Used when NotImplemented is raised instead of NotImplementedError
## :catching-non-exception
---
#### (E0712):
Used when a class which doesn't inherit from BaseException is used as an
exception in an except clause.
## :bad-super-call
---
#### (E1003):
Used when another argument than the current class is given as first argument
of the super builtin.
## :no-member
---
#### (E1101):
Used when a variable is accessed for an unexistent member.
## :not-callable
---
#### (E1102):
Used when an object being called has been inferred to a non callable object
## :assignment-from-no-return
---
#### (E1111):
Used when an assignment is done on a function call but the inferred function
doesn't return anything.
## :no-value-for-parameter
---
#### (E1120):
Used when a function call passes too few arguments.
## :too-many-function-args
---
#### (E1121):
Used when a function call passes too many positional arguments.
## :unexpected-keyword-arg
---
#### (E1123):
Used when a function call passes a keyword argument that doesn't correspond to
one of the function's parameter names.
## :redundant-keyword-arg
---
#### (E1124):
Used when a function call would result in assigning multiple values to a
function parameter, one value from a positional argument and one from a
keyword argument.
## :missing-kwoa
---
#### (E1125):
Used when a function call does not pass a mandatory keyword-only argument.
This message can't be emitted when using Python < 3.0.
## :invalid-sequence-index
---
#### (E1126):
Used when a sequence type is indexed with an invalid type. Valid types are
ints, slices, and objects with an __index__ method.
## :invalid-slice-index
---
#### (E1127):
Used when a slice index is not an integer, None, or an object with an
__index__ method.
## :assignment-from-none
---
#### (E1128):
Used when an assignment is done on a function call but the inferred function
returns nothing but None.
## :not-context-manager
---
#### (E1129):
Used when an instance in a with statement doesn't implement the context
manager protocol(__enter__/__exit__).
## :invalid-unary-operand-type
---
#### (E1130):
Emitted when an unary operand is used on an object which does not support this
type of operation
## :unsupported-binary-operation
---
#### (E1131):
Emitted when a binary arithmetic operation between two operands is not
supported.
## :repeated-keyword
---
#### (E1132):
Emitted when a function call got multiple values for a keyword.
## :not-an-iterable
---
#### (E1133):
Used when a non-iterable value is used in place whereiterable is expected
## :not-a-mapping
---
#### (E1134):
Used when a non-mapping value is used in place wheremapping is expected
## :unsupported-membership-test
---
#### (E1135):
Emitted when an instance in membership test expression doesn'timplement
membership protocol (__contains__/__iter__/__getitem__)
## :unsubscriptable-object
---
#### (E1136):
Emitted when a subscripted value doesn't support subscription(i.e. doesn't
define __getitem__ method)
## :logging-unsupported-format
---
#### (E1200):
Used when an unsupported format character is used in a logging statement
format string.
## :logging-format-truncated
---
#### (E1201):
Used when a logging statement format string terminates before the end of a
conversion specifier.
## :logging-too-many-args
---
#### (E1205):
Used when a logging format string is given too few arguments.
## :logging-too-few-args
---
#### (E1206):
Used when a logging format string is given too many arguments
## :bad-format-character
---
#### (E1300):
Used when a unsupported format character is used in a format string.
## :truncated-format-string
---
#### (E1301):
Used when a format string terminates before the end of a conversion specifier.
## :mixed-format-string
---
#### (E1302):
Used when a format string contains both named (e.g. '%(foo)d') and unnamed
(e.g. '%d') conversion specifiers. This is also used when a named conversion
specifier contains generate.bash messages.md test_file.md for the minimum field width and/or precision.
## :format-needs-mapping
---
#### (E1303):
Used when a format string that uses named conversion specifiers is used with
an argument that is not a mapping.
## :missing-format-string-key
---
#### (E1304):
Used when a format string that uses named conversion specifiers is used with a
dictionary that doesn't contain all the keys required by the format string.
## :too-many-format-args
---
#### (E1305):
Used when a format string that uses unnamed conversion specifiers is given too
many arguments.
## :too-few-format-args
---
#### (E1306):
Used when a format string that uses unnamed conversion specifiers is given too
few arguments
## :bad-str-strip-call
---
#### (E1310):
The argument to a str.{l,r,}strip call contains a duplicate character,
## :fatal
---
#### (F0001):
Used when an error occurred preventing the analysis of a module (unable to
find it for instance).
## :astroid-error
---
#### (F0002):
Used when an unexpected error occurred while building the Astroid
representation. This is usually accompanied by a traceback. Please report such
errors !
## :parse-error
---
#### (F0010):
Used when an exception occured while building the Astroid representation which
could be handled by astroid.
## :method-check-failed
---
#### (F0202):
Used when Pylint has been unable to check methods signature compatibility for
an unexpected reason. Please report this kind if you don't make sense of it.
## :raw-checker-failed
---
#### (I0001):
Used to inform that a built-in module has not been checked using the raw
checkers.
## :bad-inline-option
---
#### (I0010):
Used when an inline option is either badly formatted or can't be used inside
modules.
## :locally-disabled
---
#### (I0011):
Used when an inline option disables a message or a messages category.
## :locally-enabled
---
#### (I0012):
Used when an inline option enables a message or a messages category.
## :file-ignored
---
#### (I0013):
Used to inform that the file will not be checked
## :suppressed-message
---
#### (I0020):
A message was triggered on a line, but suppressed explicitly by a disable=
comment in the file. This message is not generated for messages that are
ignored due to configuration settings.
## :useless-suppression
---
#### (I0021):
Reported when a message is explicitly disabled for a line or a block of code,
but never triggered.
## :deprecated-pragma
---
#### (I0022):
Some inline pylint options have been renamed or reworked, only the most recent
form should be used. NOTE:skip-all is only available with pylint >= 0.26
## :too-many-nested-blocks
---
#### (R0101):
Used when a function or a method has too many nested blocks. This makes the
code less understandable and maintainable.
## :simplifiable-if-statement
---
#### (R0102):
Used when an if statement can be replaced with 'bool(test)'.
## :no-self-use
---
#### (R0201):
Used when a method doesn't use its bound instance, and so could be written as
a function.
## :no-classmethod-decorator
---
#### (R0202):
Used when a class method is defined without using the decorator syntax.
## :no-staticmethod-decorator
---
#### (R0203):
Used when a static method is defined without using the decorator syntax.
## :redefined-variable-type
---
#### (R0204):
Used when the type of a variable changes inside a method or a function.
## :cyclic-import
---
#### (R0401):
Used when a cyclic import between two or more modules is detected.
## :duplicate-code
---
#### (R0801):
Indicates that a set of similar lines has been detected among multiple file.
This usually means that the code should be refactored to avoid this
duplication.
## :too-many-ancestors
---
#### (R0901):
Used when class has too many parent classes, try to reduce this to get a
simpler (and so easier to use) class.
## :too-many-instance-attributes
---
#### (R0902):
Used when class has too many instance attributes, try to reduce this to get a
simpler (and so easier to use) class.
## :too-few-public-methods
---
#### (R0903):
Used when class has too few public methods, so be sure it's really worth it.
## :too-many-public-methods
---
#### (R0904):
Used when class has too many public methods, try to reduce this to get a
simpler (and so easier to use) class.
## :too-many-return-statements
---
#### (R0911):
Used when a function or method has too many return statement, making it hard
to follow.
## :too-many-branches
---
#### (R0912):
Used when a function or method has too many branches, making it hard to
follow.
## :too-many-arguments
---
#### (R0913):
Used when a function or method takes too many arguments.
## :too-many-locals
---
#### (R0914):
Used when a function or method has too many local variables.
## :too-many-statements
---
#### (R0915):
Used when a function or method has too many statements. You should then split
it in smaller functions / methods.
## :too-many-boolean-expressions
---
#### (R0916):
Used when a if statement contains too many boolean expressions
## :unreachable
---
#### (W0101):
Used when there is some code behind a "return" or "raise" statement, which
will never be accessed.
## :dangerous-default-value
---
#### (W0102):
Used when a mutable value as list or dictionary is detected in a default value
for an argument.
## :pointless-statement
---
#### (W0104):
Used when a statement doesn't have (or at least seems to) any effect.
## :pointless-string-statement
---
#### (W0105):
Used when a string is used as a statement (which of course has no effect).
This is a particular case of W0104 with its own message so you can easily
disable it if you're using those strings as documentation, instead of
comments.
## :expression-not-assigned
---
#### (W0106):
Used when an expression that is not a function call is assigned to nothing.
Probably something else was intended.
## :unnecessary-pass
---
#### (W0107):
Used when a "pass" statement that can be avoided is encountered.
## :unnecessary-lambda
---
#### (W0108):
Used when the body of a lambda expression is a function call on the same
argument list as the lambda itself; such lambda expressions are in all but a
few cases replaceable with the function being called in the body of the
lambda.
## :duplicate-key
---
#### (W0109):
Used when a dictionary expression binds the same key multiple times.
## :useless-else-on-loop
---
#### (W0120):
Loops should only have an else clause if they can exit early with a break
statement, otherwise the statements under else should be on the same scope as
the loop itself.
## :exec-used
---
#### (W0122):
Used when you use the "exec" statement (function for Python 3), to discourage
its usage. That doesn't mean you can not use it !
## :eval-used
---
#### (W0123):
Used when you use the "eval" function, to discourage its usage. Consider using
`ast.literal_eval` for safely evaluating strings containing Python expressions
from untrusted sources.
## :confusing-with-statement
---
#### (W0124):
Emitted when a `with` statement component returns multiple values and uses
name binding with `as` only for a part of those values, as in with ctx() as a,
b. This can be misleading, since it's not clear if the context manager returns
a tuple or if the node without a name binding is another context manager.
## :using-constant-test
---
#### (W0125):
Emitted when a conditional statement (If or ternary if) uses a constant value
for its test. This might not be what the user intended to do.
## :lost-exception
---
#### (W0150):
Used when a break or a return statement is found inside the finally clause of
a try...finally block: the exceptions raised in the try clause will be
silently swallowed instead of being re-raised.
## :assert-on-tuple
---
#### (W0199):
A call of assert on a tuple will always evaluate to true if the tuple is not
empty, and will always evaluate to false if it is.
## :attribute-defined-outside-init
---
#### (W0201):
Used when an instance attribute is defined outside the __init__ method.
## :bad-staticmethod-argument
---
#### (W0211):
Used when a static method has "self" or a value specified in valid-
classmethod-first-arg option or valid-metaclass-classmethod-first-arg option
as first argument.
## :protected-access
---
#### (W0212):
Used when a protected member (i.e. class member with a name beginning with an
underscore) is access outside the class or a descendant of the class where
it's defined.
## :arguments-differ
---
#### (W0221):
Used when a method has a different number of arguments than in the implemented
interface or in an overridden method.
## :signature-differs
---
#### (W0222):
Used when a method signature is different than in the implemented interface or
in an overridden method.
## :abstract-method
---
#### (W0223):
Used when an abstract method (i.e. raise NotImplementedError) is not
overridden in concrete class.
## :super-init-not-called
---
#### (W0231):
Used when an ancestor class method has an __init__ method which is not called
by a derived class.
## :no-init
---
#### (W0232):
Used when a class has no __init__ method, neither its parent classes.
## :non-parent-init-called
---
#### (W0233):
Used when an __init__ method is called on a class which is not in the direct
ancestors for the analysed class.
## :unnecessary-semicolon
---
#### (W0301):
Used when a statement is ended by a semi-colon (";"), which isn't necessary
(that's python, not C ;).
## :bad-indentation
---
#### (W0311):
Used when an unexpected number of indentation's tabulations or spaces has been
found.
## :mixed-indentation
---
#### (W0312):
Used when there are some mixed tabs and spaces in a module.
## :wildcard-import
---
#### (W0401):
Used when `from module import *` is detected.
## :deprecated-module
---
#### (W0402):
Used a module marked as deprecated is imported.
## :reimported
---
#### (W0404):
Used when a module is reimported multiple times.
## :import-self
---
#### (W0406):
Used when a module is importing itself.
## :misplaced-future
---
#### (W0410):
Python 2.5 and greater require __future__ import to be the first non docstring
statement in the module.
## :fixme
---
#### (W0511):
Used when a warning note as FIXME or XXX is detected.
## :global-variable-undefined
---
#### (W0601):
Used when a variable is defined through the "global" statement but the
variable is not defined in the module scope.
## :global-variable-not-assigned
---
#### (W0602):
Used when a variable is defined through the "global" statement but no
assignment to this variable is done.
## :global-statement
---
#### (W0603):
Used when you use the "global" statement to update a global variable. Pylint
just try to discourage this usage. That doesn't mean you can not use it !
## :global-at-module-level
---
#### (W0604):
Used when you use the "global" statement at the module level since it has no
effect
## :unused-import
---
#### (W0611):
Used when an imported module or variable is not used.
## :unused-variable
---
#### (W0612):
Used when a variable is defined but not used.
## :unused-argument
---
#### (W0613):
Used when a function or method argument is not used.
## :unused-wildcard-import
---
#### (W0614):
Used when an imported module or variable is not used from a `'from X import
*'` style import.
## :redefined-outer-name
---
#### (W0621):
Used when a variable's name hide a name defined in the outer scope.
## :redefined-builtin
---
#### (W0622):
Used when a variable or function override a built-in.
## :redefine-in-handler
---
#### (W0623):
Used when an exception handler assigns the exception to an existing name
## :undefined-loop-variable
---
#### (W0631):
Used when an loop variable (i.e. defined by a for loop or a list comprehension
or a generator expression) is used outside the loop.
## :cell-var-from-loop
---
#### (W0640):
A variable used in a closure is defined in a loop. This will result in all
closures using the same value for the closed-over variable.
## :bare-except
---
#### (W0702):
Used when an except clause doesn't specify exceptions type to catch.
## :broad-except
---
#### (W0703):
Used when an except catches a too general exception, possibly burying
unrelated errors.
## :duplicate-except
---
#### (W0705):
Used when an except catches a type that was already caught by a previous
handler.
## :binary-op-exception
---
#### (W0711):
Used when the exception to catch is of the form "except A or B:". If intending
to catch multiple, rewrite as "except (A, B):"
## :logging-not-lazy
---
#### (W1201):
Used when a logging statement has a call form of "logging.<logging
method>(format_string % (format_args...))". Such calls should leave string
interpolation to the logging method itself and be written "logging.<logging
method>(format_string, format_args...)" so that the program may avoid
incurring the cost of the interpolation in those cases in which no message
will be logged. For more, see http://www.python.org/dev/peps/pep-0282/.
## :logging-format-interpolation
---
#### (W1202):
Used when a logging statement has a call form of "logging.<logging
method>(format_string.format(format_args...))". Such calls should use %
formatting instead, but leave interpolation to the logging function by passing
the parameters as arguments.
## :bad-format-string-key
---
#### (W1300):
Used when a format string that uses named conversion specifiers is used with a
dictionary whose keys are not all strings.
## :unused-format-string-key
---
#### (W1301):
Used when a format string that uses named conversion specifiers is used with a
dictionary that contains keys not required by the format string.
## :bad-format-string
---
#### (W1302):
Used when a PEP 3101 format string is invalid. This message can't be emitted
when using Python < 2.7.
## :missing-format-argument-key
---
#### (W1303):
Used when a PEP 3101 format string that uses named fields doesn't receive one
or more required keywords. This message can't be emitted when using Python <
2.7.
## :unused-format-string-argument
---
#### (W1304):
Used when a PEP 3101 format string that uses named fields is used with an
argument that is not required by the format string. This message can't be
emitted when using Python < 2.7.
## :format-combined-specification
---
#### (W1305):
Usen when a PEP 3101 format string contains both automatic field numbering
(e.g. '{}') and manual field specification (e.g. '{0}'). This message can't be
emitted when using Python < 2.7.
## :missing-format-attribute
---
#### (W1306):
Used when a PEP 3101 format string uses an attribute specifier ({0.length}),
but the argument passed for formatting doesn't have that attribute. This
message can't be emitted when using Python < 2.7.
## :invalid-format-index
---
#### (W1307):
Used when a PEP 3101 format string uses a lookup specifier ({a[1]}), but the
argument passed for formatting doesn't contain or doesn't have that key as an
attribute. This message can't be emitted when using Python < 2.7.
## :anomalous-backslash-in-string
---
#### (W1401):
Used when a backslash is in a literal string but not as an escape.
## :anomalous-unicode-escape-in-string
---
#### (W1402):
Used when an escape like u is encountered in a byte string where it has no
effect.
## :bad-open-mode
---
#### (W1501):
Python supports: r, w, a[, x] modes with b, +, and U (only with r) options.
See http://docs.python.org/2/library/functions.html#open
## :boolean-datetime
---
#### (W1502):
Using datetime.time in a boolean context can hide subtle bugs when the time
they represent matches midnight UTC. This behaviour was fixed in Python 3.5.
See http://bugs.python.org/issue13936 for reference. This message can't be
emitted when using Python >= 3.5.
## :redundant-unittest-assert
---
#### (W1503):
The first argument of assertTrue and assertFalse is a condition. If a constant
is passed as parameter, that condition will be always true. In this case a
warning should be emitted.
## :deprecated-method
---
#### (W1505):
The method is marked as deprecated and will be removed in a future version of
Python. Consider looking for an alternative in the documentation.

