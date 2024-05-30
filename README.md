# my-discord-bot
Demo discord bot for Discord Bot Initiallizer.
Made with https://www.youtube.com/watch?v=eLcAZIeqLu8&list=PLESMQx4LeD3N0-KKPPDaToZhBsom2E_Ju

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

# Command group
Command group can be made with attribute "@bot.group()".
Commands in the group becomes sub_commands of the group.
Group name is decided with function name, and the sub_commands' attribute should be changed to "(group name).command()".
Commands under the group can be executed as "(group name) (command) (arguments)".
Group can be nested multiple times. In this case, you should write the command with hierarchical order as the group is nested.

# Load commands
Commands can be load with file.
Check the file directory and load with file name.

Commands can be load with bot_cog.
Can be load with file name or stated class.
* When you write the bot command as cog command, you need to add self parameter on your method(command) *
Loading cog files iteratively can be done.

# Permission check
Permission can be checked with the method that check permission of the command.
@commands.check_method, @commands.check(check_method)
If permission denied, throws error. 