Help Parser
===========

``HelpParser`` is built-in ``Telegrask`` module which parses ``/help`` command automatically.
To disable this feature you have to set ``bot.config["HELP_MESSAGE"] = False`` (where ``bot``
is instance of ``Telegrask`` class.

We recommend to use ``bot.help`` object which is default instance of ``HelpParser`` class.


@custom_help_command
--------------------

This is another ``Telegrask`` decorator which is helpful when you want to create own help command.

.. code-block:: python

    from telegram import Update
    from telegram.ext import CallbackContext
    
    @bot.custom_help_command
    def help(update: Update, context: CallbackContext, commands):
        # commands is a dict {"command_name": "command_description", ...}
        # reference for `bot.help.commands_descriptions`
        pass


Helpful Hacks
-------------

* ``bot.help.header = "Custom help message header"`` 
* ``bot.help.help_description = "custom /help command description"``
 