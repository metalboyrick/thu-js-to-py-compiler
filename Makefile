yacc_lex: c2py.h compiler.c c2py.l c2py.y
	flex c2py.l
	bison -d c2py.y
	gcc lex.yy.c c2py.tab.c compiler.c -o c2py

clean:
	rm -f lex.yy.c c2py.tab.c c2py.tab.h c2py