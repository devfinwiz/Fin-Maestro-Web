from telegram.ext import Updater, CommandHandler

# Define your existing method here
def your_method():
    return "test success"

def execute_your_method(update, context):
    # Call your existing method here
    result = your_method()

    # Send the result back to the user
    update.message.reply_text(result)

# Create an updater and pass your bot token
updater = Updater("bot token here")

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Add a command handler for executing your method
dispatcher.add_handler(CommandHandler("your_command", execute_your_method))

# Start the bot
updater.start_polling()
updater.idle()