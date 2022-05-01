# from app.schemas import DemoUser
# from app.messages import Message


# def test_create_msg():
#     data = DemoUser().user_2()
#     message = Message(data)
#     assert message.create_msg() == (
#         "Good mornin' 🌳\n\n"
#         "Here's the weather for London, GB:\n\n"
#         "🌡️ Max: 40.3°F\n"
#         "🌡️ Min: 40.6°F\n"
#         "🌡️ Feels like: 45.29°F\n"
#         "💨 Wind: 34.5 mph\n"
#         "🌬️ Status: Clear sky\n"
#         "🌞 UV Index: 4"
#     )


# def test_error_msg():
#     assert (
#         Message.error_msg() == "Sorry, I couldn't find that location. Please try again."
#     )


# def test_daily_limit_msg():
#     assert (
#         Message.daily_limit_msg()
#         == "Sorry, you've reached your daily limit. Please try again tomorrow."
#     )


# def test_welcome_msg():
#     assert Message.welcome_msg() == (
#         "Welcome to Morning Bot! 🤖\n\n"
#         "This message is generated the first time you use me. "
#         "If you ever get tired of me, just remove your shortcut. "
#         "You can always add me back with the same shortcut.\n\n"
#         "Here is your first weather update!\n"
#     )
