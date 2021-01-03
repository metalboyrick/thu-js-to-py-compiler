grammar Js2Py;

/*
 * Parser Rules
 */

// Note : scopes must be NEWLINED

program: (line | function)+ EOF;

line: (ternary_statement | statement | conditional_statement) ';'? NEWLINE+;

// Statement

statement: (
		assignment
		| array_ops
		| array_concat
		| function_return
		| function_call
		| arithmetic
		| console_log
		| while_loop
	);

// TODO: fix error here issues lie within the value production , the parser parses 1) as a value
conditional_statement:
	IF '(' expression (relop expression)* ')' '{' NEWLINE* line+ '}';

ternary_statement: expression '?' statement ':' statement;

// Assignment
value: (
		VARIABLE
		| NUMBER
		| TEXT
		| function_call
		| array_item
		| array_length
		| array
	);

assignment: ( VAR | CONST | LET) VARIABLE '=' value;

// Function 
function: (
		FUNCTION VARIABLE? '(' value* ')' '{' NEWLINE* line+ '}' ';'? NEWLINE+
	);

function_call: VARIABLE '(' value* ')';

function_return: RETURN (value | array_concat);

// Arithmetic
op: (ADD_OP | SUB_OP | MUL_OP | DIV_OP);

arithmetic: (
		(value op value (op value)*)
		| VARIABLE (UNNARY_ADD | UNNARY_MINUS)
	);

// Relational
relop: (LT | LTE | GT | GTE | EQ | NEQ);

expression: (value | arithmetic) relop (value | arithmetic);

// Array

array_item: VARIABLE '[' (value | arithmetic) ']';

array_length: VARIABLE '.' 'length';

array: '[' value? ( ',' value)* ']';

array_ops:
	VARIABLE '.' ('push' | 'pop') '(' (value | array_item)+ ')';

array_concat:
	value '.' 'concat' '(' (value | array_item) (
		',' (value | array_item)
	)* ')';

// Console
console_log: CONSOLE '.log' '(' value ( ',' value)* ')';

// Loop
while_loop:
	WHILE '(' expression (relop expression)* ')' '{' NEWLINE* (
		line+
		| (BREAK NEWLINE)
	) '}';

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
CONST: 'const';
LET: 'let';
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
	)*;

NUMBER: DIGIT+ ([.,] DIGIT+)?;

WHITESPACE: (' ' | '\t')+ -> skip;

NEWLINE: ('\r'? '\n' | '\r')+;

TEXT: ('"' | '\'') ~['"]+ ('\'' | '"');
