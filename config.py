
from typing import Literal

import pydantic_settings

EnvContext = Literal['local_emulator', 'bstack', 'local_real']


class Config(pydantic_settings.BaseSettings):
    context: EnvContext = 'bstack'
    timeout: float = 10.0

config = Config()

# if config.context == 'bstack':
#     load_dotenv(file.env('.env.bstack'))
# elif config.context == 'local_real':
#     load_dotenv(file.env('.env.local_real'))
# else:
#     load_dotenv(file.env('.env.local_emulator'))
#
# remote_url = os.getenv('REMOTE_URL')
# device_name = os.getenv('DEVICE_NAME')
#
# if config.context == 'bstack':
#     apk_path = os.getenv('APP')
# else:
#     apk_path = file.apk_app_alpha_universal_release()
#
#
#
# # if config.context == 'bstack':
# #     load_dotenv(file.env('.env.bstack'))
# # elif config.context == 'local_real':
# #     load_dotenv(file.env('.env.local_real'))
# # else:
# #     load_dotenv(file.env('.env.local_emulator'))
# #
# # remote_url = os.getenv('REMOTE_URL')
# # device_name = os.getenv('DEVICE_NAME')
# #
# # if config.context == 'bstack':
# #     apk_path = os.getenv('APP')
# # else:
# #     apk_path = file.apk_app_alpha_universal_release()
#
#
# def driver_options():
#     if config.context == 'local_emulator':
#
#
#         options = UiAutomator2Options().load_capabilities({
#       "app": config.apk_path,
#       "appWaitActivity": "org.wikipedia.*"
#     })
#
#     if config.context == 'bstack':
#         options = UiAutomator2Options().load_capabilities({
#             "platformName": os.getenv('PLATFORM_NAME'),
#             "platformVersion": os.getenv('PLATFORM_VERSION'),
#             "deviceName": os.getenv('DEVICE_NAME'),
#             "app": os.getenv('APP'),
#             'bstack:options': {
#                 "projectName": "First Python project",
#                 "buildName": "browserstack-build-1",
#                 "sessionName": "BStack first_test",
#                 "userName": os.getenv('USER_NAME'),
#                 "accessKey": os.getenv('ACCESS_KEY')
#             }
#         })
#
#
#     return options

