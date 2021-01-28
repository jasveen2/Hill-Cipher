# Hill-Cipher

To use the Hill Cipher, you need to download SymPy and NumPy to help with matrix functions. Personally, I found it easiest to download Anaconda and then run the command "conda install numpy" in order to download the library onto my device. SymPy can be downloaded directly from a source installer on GitHub (https://github.com/sympy/sympy/releases). 

The makefile is the easiest way to use the cipher. Run the command "make run (key) (message) (mode)" or the command "Python Hill.py (key) (message) (mode)". 

The key will need to be a 4 letter phrase/word, as this version only works for 2x2 matrix keys. The mode must be the word "encrypt" or "decrypt" (case insensitive).
