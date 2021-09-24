class Commands():
    async def cmd_test(self, ctx):
        '''Send the message "This is a test command"'''
        await ctx.channel.send(f"This is a test command")

    async def cmd_embed(self, ctx):
        '''Send an example embed'''
        embed_content = self.load_embed("test_embed")
        embed = self.create_embed(embed_content)

        await ctx.channel.send(embed = embed)
    