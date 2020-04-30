import discord.ext.commands as dec

txt_positive = [
    'affirmative', 'agree', 'agreed', 'all right', 'amen', 'aye',
    'beyond a doubt', 'by all means', 'certainly', 'definitely', 'even so',
    'exactly', 'fine', 'gladly', 'good', 'good enough', 'granted',
    'indubitably', 'just so', 'make it so', 'most assuredly', 'naturally',
    'of course', 'ok', 'okay', 'positively', 'precisely', 'sure', 'sure thing',
    'surely', 'true', 'undoubtedly', 'y', 'yah', 'ye', 'yea', 'yeah',
    'yee', 'yes']
txt_negative = [
    'cancel', 'forget it', 'n', 'nah', 'naw', 'nay', 'negative', 'negatory',
    'never', 'nix', 'no', 'not', 'null', 'refusal', 'refuse', 'reject',
    'rejection']
txt_ambiguous_answer = [
    """User doesn't know what they want.""",
    """Beg'pardon?""",
    """It's really not a hard question....""",
    """Hmm?""",
    """Like I really have nothing better to do than listen to you babble...""",
    """..."""]


class Persona(dec.Cog):

    def __init__(self, bot: dec.Bot):
        super().__init__()
        self.bot = bot
