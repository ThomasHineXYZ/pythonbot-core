import discord.ext.commands as disext


class Memory(disext.Cog):
    """ Bot Memory

    This module handles DB connections. Currently only mysql is supported.
    """

    def __init__(self, bot: disext.Bot):
        super().__init__()
        self.bot = bot
        self.host_name = None
        self.port_numb = None
        self.user_name = None
        self.password = None
        self.db = None

        # we need to start off by doing a check on DB creds to see if they are
        # available, and work.
        # so the second we are online, we need to check to make sure the db is
        # 100%, or we message the owner with the wiz command.

    @disext.Cog.listener()
    async def on_ready(self):
        # Check to see if DB is setup
        # no?
        #   Wait some
        #   as OWNER if they want to set it up and tell them how to wiz
        from .discord import Discord
        cog_dis: Discord = self.bot.get_cog('Discord')
        # await cog_dis.message_developer("Implement your DB Wizard!")

    @disext.command()
    @disext.is_owner()
    async def sql(self, ctx: disext.Context, *, arg: str) -> None:
        await ctx.send(f'{ctx.guild}:{ctx.channel}:{ctx.author} -> {arg}')

    @disext.command(name='wiz_db')
    @disext.is_owner()
    async def wiz_db_setup(self, ctx: disext.Context) -> None:
        """ DB Setup Wizard.

        This will walk you through setting up your DB connection.

        :return:
        """
        await ctx.send('Implement me')
