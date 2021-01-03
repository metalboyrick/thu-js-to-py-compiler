from Js2PyListener import Js2PyListener
from Js2PyParser import Js2PyParser

class Js2PyCodeGenListener(Js2PyListener) :
    def __init__(self, output):
        self.output = output
        self.indentCount = 0

    # Enter a parse tree produced by Js2PyParser#line.
    def enterLine(self, ctx:Js2PyParser.LineContext):
        self.output.write("%s" % ("\t"*self.indentCount))
        pass

    # Exit a parse tree produced by Js2PyParser#line.
    def exitLine(self, ctx:Js2PyParser.LineContext):
        self.output.write("\n")

    # Enter a parse tree produced by Js2PyParser#statement.
    def enterStatement(self, ctx:Js2PyParser.StatementContext):
        pass

    # Exit a parse tree produced by Js2PyParser#statement.
    def exitStatement(self, ctx:Js2PyParser.StatementContext):
        pass

    
    # Enter a parse tree produced by Js2PyParser#condition.
    def enterCondition(self, ctx:Js2PyParser.ConditionContext):
        pass

    # Exit a parse tree produced by Js2PyParser#condition.
    def exitCondition(self, ctx:Js2PyParser.ConditionContext):
        self.output.write(":\n")

    # Enter a parse tree produced by Js2PyParser#conditional_statement.
    def enterConditional_statement(self, ctx:Js2PyParser.Conditional_statementContext):
        self.output.write("%s" % ("\t"*self.indentCount))
        self.output.write("%s " % (ctx.IF()))
        
        self.indentCount += 1

    # Exit a parse tree produced by Js2PyParser#conditional_statement.
    def exitConditional_statement(self, ctx:Js2PyParser.Conditional_statementContext):
        self.indentCount -= 1


    # Enter a parse tree produced by Js2PyParser#ternary_statement.
    def enterTernary_statement(self, ctx:Js2PyParser.Ternary_statementContext):
        self.output.write("%s" % ('\t' * self.indentCount))
        self.output.write("%s if %s else %s" % (ctx.statement()[0].getText(),ctx.expression().getText(),ctx.statement()[1].getText()))

    # Exit a parse tree produced by Js2PyParser#ternary_statement.
    def exitTernary_statement(self, ctx:Js2PyParser.Ternary_statementContext):
        self.output.write("\n")


    # Enter a parse tree produced by Js2PyParser#value.
    def enterValue(self, ctx:Js2PyParser.ValueContext):
        if ctx.VARIABLE():
            self.output.write("%s" % (ctx.VARIABLE()))
        elif ctx.NUMBER():
            self.output.write("%s" % (ctx.NUMBER()))
        elif ctx.TEXT():
            self.output.write("%s" % (ctx.TEXT()))

    # Exit a parse tree produced by Js2PyParser#value.
    def exitValue(self, ctx:Js2PyParser.ValueContext):
        pass


    # Enter a parse tree produced by Js2PyParser#assignment.
    def enterAssignment(self, ctx:Js2PyParser.AssignmentContext):
        self.output.write("%s%s = %s" % ("\t"*self.indentCount,ctx.VARIABLE(),ctx.value().getText()))

    # Exit a parse tree produced by Js2PyParser#assignment.
    def exitAssignment(self, ctx:Js2PyParser.AssignmentContext):
        pass


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


    # Enter a parse tree produced by Js2PyParser#function_call.
    def enterFunction_call(self, ctx:Js2PyParser.Function_callContext):
        pass

    # Exit a parse tree produced by Js2PyParser#function_call.
    def exitFunction_call(self, ctx:Js2PyParser.Function_callContext):
        pass


    # Enter a parse tree produced by Js2PyParser#function_return.
    def enterFunction_return(self, ctx:Js2PyParser.Function_returnContext):
        self.output.write("%s" % ("\t"*self.indentCount))
        self.output.write("%s " % (ctx.RETURN()))
        if(ctx.value()):
            self.output.write("%s\n" % (ctx.value().getText()))
        else:
            self.output.write("%s\n " % (ctx.array_concat().getText()))

    # Exit a parse tree produced by Js2PyParser#function_return.
    def exitFunction_return(self, ctx:Js2PyParser.Function_returnContext):
        pass


    # Enter a parse tree produced by Js2PyParser#op.
    def enterOp(self, ctx:Js2PyParser.OpContext):
        pass

    # Exit a parse tree produced by Js2PyParser#op.
    def exitOp(self, ctx:Js2PyParser.OpContext):
        pass


    # Enter a parse tree produced by Js2PyParser#arithmetic.
    def enterArithmetic(self, ctx:Js2PyParser.ArithmeticContext):
        self.output.write("%s" % (ctx.getText()))

    # Exit a parse tree produced by Js2PyParser#arithmetic.
    def exitArithmetic(self, ctx:Js2PyParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by Js2PyParser#relop.
    def enterRelop(self, ctx:Js2PyParser.RelopContext):
        self.output.write("%s " % (ctx.getText()))   

    # Exit a parse tree produced by Js2PyParser#relop.
    def exitRelop(self, ctx:Js2PyParser.RelopContext):
        pass


    # Enter a parse tree produced by Js2PyParser#expression.
    def enterExpression(self, ctx:Js2PyParser.ExpressionContext):
        pass

    # Exit a parse tree produced by Js2PyParser#expression.
    def exitExpression(self, ctx:Js2PyParser.ExpressionContext):
        pass


    # Enter a parse tree produced by Js2PyParser#array_item.
    def enterArray_item(self, ctx:Js2PyParser.Array_itemContext):
        pass

    # Exit a parse tree produced by Js2PyParser#array_item.
    def exitArray_item(self, ctx:Js2PyParser.Array_itemContext):
        pass


    # Enter a parse tree produced by Js2PyParser#array_length.
    def enterArray_length(self, ctx:Js2PyParser.Array_lengthContext):
        self.output.write("len(%s)" % (ctx.VARIABLE()))

    # Exit a parse tree produced by Js2PyParser#array_length.
    def exitArray_length(self, ctx:Js2PyParser.Array_lengthContext):
        pass


    # Enter a parse tree produced by Js2PyParser#array.
    def enterArray(self, ctx:Js2PyParser.ArrayContext):
        pass

    # Exit a parse tree produced by Js2PyParser#array.
    def exitArray(self, ctx:Js2PyParser.ArrayContext):
        pass


    # Enter a parse tree produced by Js2PyParser#array_ops.
    def enterArray_ops(self, ctx:Js2PyParser.Array_opsContext):
        pass

    # Exit a parse tree produced by Js2PyParser#array_ops.
    def exitArray_ops(self, ctx:Js2PyParser.Array_opsContext):
        pass


    # Enter a parse tree produced by Js2PyParser#array_concat.
    def enterArray_concat(self, ctx:Js2PyParser.Array_concatContext):
        pass

    # Exit a parse tree produced by Js2PyParser#array_concat.
    def exitArray_concat(self, ctx:Js2PyParser.Array_concatContext):
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
        pass

    # Exit a parse tree produced by Js2PyParser#console_log.
    def exitConsole_log(self, ctx:Js2PyParser.Console_logContext):
        pass


    # Enter a parse tree produced by Js2PyParser#while_loop.
    def enterWhile_loop(self, ctx:Js2PyParser.While_loopContext):
        self.output.write("while ")
        self.indentCount += 1

    # Exit a parse tree produced by Js2PyParser#while_loop.
    def exitWhile_loop(self, ctx:Js2PyParser.While_loopContext):
        self.indentCount -= 1

