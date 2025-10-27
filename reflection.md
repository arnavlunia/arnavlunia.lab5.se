1. 


The easiest issues were definitely the style and formatting errors flagged by Flake8. 
Things like fixing long lines, adding the right amount of blank lines, and making sure
I used consistent naming (changing addItem to add_item)

The hardest issue was the mutable default argument (logs=[]) that Pylint flagged. That
bug is tricky because it messes with how Python objects are shared in memory, which is 
a subtle concept. My fix was necessary: changing the signature to logs=None and adding
the conditional check (if logs is None: logs = []). It required me to genuinely 
understand a core Python behavior, which was way more involved than a simple style 
correction.


2. 



Yes, I did encounter one specific warning that was essentially a false positive given 
the context of the script: Pylint's W0603 warning for Using the global statement 
(global stock_data).

Pylint flags this because global variable mutation is a bad practice. However, the 
load_data() function had to replace the entire global dictionary with data read from 
the file. Since the lab required a simple script structure, I couldn't easily redesign 
it using a class. I chose to tolerate this one warning because the code needed to 
function as designed, proving that sometimes, you have to acknowledge a tool's 
limitation based on the project scope.




3. 



Local Development: I'd use Git pre-commit hooks to run Pylint and Flake8 before any 
code is committed. That catches 90% of basic style and quality errors immediately, 
which prevents  mistakes from entering the code base.


Continuous Integration (CI): I would integrate all three tools (Pylint, Bandit, and 
Flake8) into our CI pipeline (like GitHub Actions).

Mandatory Failure: The build should be configured to fail automatically if Bandit finds 
any high-severity security issues, or if the Pylint quality score drops below a fixed 
threshold (e.g., 9.0). This ensures we maintain a high quality standard for anything 
that gets deployed.



4. 


Robustness: The code is much more reliable. I fixed the TypeError by implementing input 
validation (the script won't crash on non-numeric input anymore). I eliminated the 
major security risk by removing eval(), and using specific exceptions like except 
KeyError: means the program won't silently ignore unexpected system errors, making 
debugging easier.

Quality/Readability: The code is definitely cleaner and easier to read. Using f-strings
made the output messages more direct and concise. Most importantly, fixing the mutable 
default argument eliminated a subtle bug that would have been a nightmare to trace down
later. Overall, the consistent naming and organization (using Flake8) dramatically 
improved the maintainability.


