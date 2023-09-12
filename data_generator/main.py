import asyncio
import asyncclick as click
from runs import user_generator, user_logins_generator, frame_generator


@click.command()
@click.option("--users", is_flag=True, help="API for user registrations.")
@click.option("--logins", is_flag=True, help="API for user logins.")
@click.option("--frames", is_flag=True, help="API for frames.")
async def main(users: bool, logins: bool, frames: bool):
    if users:
        await user_generator.load()
    
    if logins:
        await user_logins_generator.load()
    
    if frames:    
        await frame_generator.load()


if __name__ == '__main__':
    asyncio.run(main())
