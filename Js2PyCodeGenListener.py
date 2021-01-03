from Js2PyListener import Js2PyListener
from Js2PyParser import Js2PyParser

class Js2PyCodeGenListener(Js2PyListener) :
    def __init__(self, output):
        self.output = output
        self.indentCount = 0

    # Enter a parse tree produced by Js2PyParser#line.
    def enterLine(self, ctx:Js2PyParser.LineContext):
        self.output.write("%s" % ("\t"*self.indentCount))

    # Exit a parse tree produced by Js2PyParser#line.
    def exitLine(self, ctx:Js2PyParser.LineContext):
        self.output.write("\n")

    # Enter a parse tree produced by Js2PyParser#unary_arithmetic.
    def enterUnary_arithmetic(self, ctx:Js2PyParser.Unary_arithmeticContext):
        if ctx.UNARY_ADD() != None:
            self.output.write("%s += 1" % (ctx.VARIABLE()))
        elif ctx.UNARY_MINUS() != None:
            self.output.write("%s -= 1" % (ctx.VARIABLE()))

    # Enter a parse tree produced by Js2PyParser#condition.
    def exitExpression(self, ctx:Js2PyParser.ExpressionContext):
        text = ""
        for index in range(0,len(ctx.children)):
            if hasattr(ctx.children[index],'text'):
                text += ctx.children[index].text
            else:
                text += ctx.children[index].getText()
        if not isinstance(ctx.parentCtx,Js2PyParser.Ternary_statementContext):
            self.output.write(text)

    # Enter a parse tree produced by Js2PyParser#value.
    def enterValue(self, ctx:Js2PyParser.ValueContext):
        if ctx.array_length() != None:
            ctx.text = f"len({ctx.array_length().VARIABLE()})"

    # Enter a parse tree produced by Js2PyParser#condition.
    def exitCondition(self, ctx:Js2PyParser.ConditionContext):
        self.output.write(":\n")

    def exitValue(self, ctx:Js2PyParser.ValueContext):
        if ctx.array_length():
            ctx.text = f"len({ctx.array_length().VARIABLE()})"

    # Enter a parse tree produced by Js2PyParser#conditional_statement.
    def enterConditional_statement(self, ctx:Js2PyParser.Conditional_statementContext):
        self.output.write("%s " % (ctx.IF()))
        
        self.indentCount += 1

    # Exit a parse tree produced by Js2PyParser#conditional_statement.
    def exitConditional_statement(self, ctx:Js2PyParser.Conditional_statementContext):
        self.indentCount -= 1


    # Enter a parse tree produced by Js2PyParser#ternary_statement.
    def enterTernary_statement(self, ctx:Js2PyParser.Ternary_statementContext):
        self.output.write("%s if %s else %s" % (
            ctx.statement()[0].getText().replace("push","append"),
            ctx.expression().getText(),
            ctx.statement()[1].getText().replace("push","append")))

    # Exit a parse tree produced by Js2PyParser#ternary_statement.
    def exitTernary_statement(self, ctx:Js2PyParser.Ternary_statementContext):
        self.output.write("\n")

    # Enter a parse tree produced by Js2PyParser#assignment.
    def enterAssignment(self, ctx:Js2PyParser.AssignmentContext):
        if ctx.value().array_length() != None:
            self.output.write("%s = %s" % (ctx.VARIABLE(),f"len({ctx.value().array_length().VARIABLE()})"))
        else:
            self.output.write("%s = %s" % (ctx.VARIABLE(),ctx.value().getText()))

    # Enter a parse tree produced by Js2PyParser#array_concat.
    def enterArray_concat(self, ctx:Js2PyParser.Array_concatContext):
        concatStr = ""
        for i in range(2,-1,-1):
            concatStr = ctx.value()[i].getText() + concatStr
            if i != 0:
                concatStr = '+' + concatStr
        self.output.write("%s" % (concatStr))

    # Enter a parse tree produced by Js2PyParser#function.
    def enterFunction(self, ctx:Js2PyParser.FunctionContext):
        # Tab and def
        self.output.write("%sdef " % ('\t' * self.indentCount))

        # Function name
        self.output.write("%s(" % (ctx.VARIABLE()))

        self.output.write("%s" % (ctx.value()[0].getText()))

        # End the function definition
        self.output.write("):\n")
        
        # Increase tab count
        self.indentCount += 1
        

    # Exit a parse tree produced by Js2PyParser#function.
    def exitFunction(self, ctx:Js2PyParser.FunctionContext):
        
        # Decreaase tab count
        self.indentCount -= 1

    # Enter a parse tree produced by Js2PyParser#function_return.
    def enterFunction_return(self, ctx:Js2PyParser.Function_returnContext):
        self.output.write("%s " % (ctx.RETURN()))
        if(ctx.value()):
            self.output.write("%s\n" % (ctx.value().getText()))
        else:
            pass

    # Enter a parse tree produced by Js2PyParser#console_log.
    def enterConsole_log(self, ctx:Js2PyParser.Console_logContext):
        valueNodes = ctx.value()
        printedContent = ""
        first = True
        for node in valueNodes:
            if(not first):
                printedContent += ','
            first = False
            printedContent += node.getText()

        self.output.write("print(%s)\n" % (printedContent))

    # Enter a parse tree produced by Js2PyParser#while_loop.
    def enterWhile_loop(self, ctx:Js2PyParser.While_loopContext):
        self.output.write("while ")
        self.indentCount += 1

    # Exit a parse tree produced by Js2PyParser#while_loop.
    def exitWhile_loop(self, ctx:Js2PyParser.While_loopContext):
        self.indentCount -= 1

