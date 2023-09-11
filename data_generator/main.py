import asyncio
from src.generator.user import UserDataGenerator
from src.generator.user_logins import UserLoginsDataGenerator
from src.generator.frame import FrameDataGenerator


if __name__ == '__main__':
    user_generator = UserDataGenerator()
    user_logins_generator = UserLoginsDataGenerator()
    frame_generator = FrameDataGenerator()

    asyncio.run(user_generator.load())
    
    asyncio.run(user_logins_generator.load())
    
    asyncio.run(frame_generator.load())
