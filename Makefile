antlr: Js2Py.g4 
	java -Xmx500M -cp "/usr/local/lib/antlr-4.7.2-complete.jar:$CLASSPATH" org.antlr.v4.Tool -Dlanguage=Python3 Js2Py.g4

clean:
	rm -f *.interp *.tokens Js2PyParser.py Js2PyListener.py Js2PyLexer.py