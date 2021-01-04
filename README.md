# Setup ANTLR in Ubuntu

```bash
# Install java and javac
sudo apt install default-jre
sudo apt install default-jdk

# Get ANTLR
wget http://www.antlr.org/download/antlr-4.7.2-complete.jar
sudo cp antlr-4.7.2-complete.jar /usr/local/lib/

# Add this in ~/.profile
export CLASSPATH=".:/usr/local/lib/antlr-4.7.2-complete.jar:$CLASSPATH"

sudo nano ~/.bash_aliases
# In ~/.bash_aliases
# simplify the use of the tool to generate lexer and parser
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.2-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
# simplify the use of the tool to test the generated code
alias grun='java org.antlr.v4.gui.TestRig'

# Run
source ~/.bashrc

# If can't execute, try put the export & 2 aliases command in .bashrc at home, run source .bashrc

# Logout then login
```

# Setting up ANTLR Python Environment

``` bash
sudo apt install python3-pip
pip3 install antlr4-python3-runtime==4.7.2
```

It is highly recommended to set up a virtual environment.

# Generate Python Parser

```bash
make
```

# Debugging the Grammar

```bash
# Create java files
antlr4 Js2Py.g4

# Compile all java files
javac Js2Py*.java

# Or just run
make java

# View parse tree, after inputting the statement, input some strings, then press CTRL + D
grun Js2Py <your-start-production> -gui

# View tokens, procedure same as above, but do these commands instead to start
grun Js2Py <your-start-production> -tokens
```

## Running the program

With the environment installed, compilation can be done with the following script, all files would be compiled to `output.py`.

```bash
python3 main.py yourfile.js
```
