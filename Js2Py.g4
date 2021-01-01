grammar Js2Py;

/*
 * Parser Rules
 */

program: (line | function)+ EOF;

line: (statement ';'? | conditional_statment | ternary_statement) NEWLINE;

// Statement

statement: assignment | array_ops | function_call | arithmetic;

conditional_statment:
	IF '(' expression (relop expression)* ')' '{' line '}';

ternary_statement: expression '?' statement ':' statement;

// Assignment
value: (
		VARIABLE
		| NUMBER
		| TEXT
		| function_call
		| array
		| array_length
	);

assignment: VAR VARIABLE '=' value;

// Function 
function: FUNCTION '(' value* ')' '{' line+ RETURN value '}';

function_call: VARIABLE '(' value* ')';

// Arithmetic
op: (ADD_OP | SUB_OP | MUL_OP | DIV_OP);

arithmetic: (
		(value op value (op value)*)
		| VARIABLE (UNNARY_ADD | UNNARY_MINUS)
	);

// Relational
relop: (LT | LTE | GT | GTE | EQ | NEQ);

expression: value relop value;

// Array
array: '[' value ( ',' value)* ']';

array_ops: VARIABLE '.' ('push' | 'pop') '(' value+ ')';

array_length: VARIABLE '.' 'length';

// Console
console_log: CONSOLE '.log' '(' value ( ',' value)* ')';

// Loop
while_loop:
	WHILE '(' expression (relop expression)* ')' '{' (
		line
		| BREAK NEWLINE
	)+ '}';

/*
 * Lexer Rules
 */
fragment LOWERCASE: [a-z];
fragment UPPERCASE: [A-Z];
fragment DIGIT: [0-9];

FUNCTION: 'function';
RETURN: 'return';
WHILE: 'while';
VAR: 'var';
IF: 'if';
ELSE: 'else';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
EQ: '==';
NEQ: '!=';
CONSOLE: 'console';
BREAK: 'break';
ADD_OP: '+';
SUB_OP: '-';
MUL_OP: '*';
DIV_OP: '/';
UNNARY_ADD: '++';
UNNARY_MINUS: '--';

VARIABLE: (LOWERCASE | UPPERCASE) (
		LOWERCASE
		| UPPERCASE
		| DIGIT
		| '_'
	)+;

NUMBER: DIGIT+ .? DIGIT*;

WHITESPACE: (' ' | '\t')+ -> skip;

NEWLINE: ('\r'? '\n' | '\r')+;

TEXT: ('"' | '\'') ~['"]+ ('\'' | '"');
