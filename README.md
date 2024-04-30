# my-discord-bot
Demo discord bot for 

# activate virtualenv
source .venv/bin/activate
# deactivate
deactivate

# Solving SSL Certification Error
Open Macintosh HD - python folder.
Run "Install Certificates.command"

# Intents type
Check which type of intent is needed for selected features.

# Help
!help command shows available commands and their description.
Add description with """ """ when no specific descriptions are set.
Specific descriptions can be set in the bracket of command().

# Command inputs
You can set the number and type of the input which command will listen.
Default type is String, can be changed with "(variable) : (type)."
You can limit the number of variable by listing as a parameter.
Can use unlimited number of variable with asterisk(*).

# Error handler
Error handler with local command can be add with attribute "@(command name).error".
Define the expected error type and set the handler.
Global error handler can be set with the attribute "@bot.event".
If there are both local and global error hander, bot will handle both of errors, in the order of local, global.