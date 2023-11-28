J=isinstance
E='@'
import smtplib as G,random as F,os,logging as A,asyncio as H
from dotenv import load_dotenv as K
import discord as C
from discord.ext import commands as L
K()
M=os.getenv('BOT_TOKEN')
D=os.getenv('SMTP_USERNAME')
N=os.getenv('SMTP_PASSWORD')
I=['pausd.us']
O=C.Intents.all()
B=L.Bot(command_prefix='!',intents=O)
A.basicConfig(level=A.DEBUG)
def Q():return str(F.randint(100000,999999))
async def R(email,verification_code):
	F=verification_code;B=email
	if B.split(E)[-1]not in I:return f"Error: {B} is not a valid email address for verification.Please use @pausd.us instead, or contact an admin."
	H='smtp.gmail.com';J=587;K=f"Subject: Verification Code\n\nYour verification code is {F}"
	with G.SMTP(H,J)as C:C.starttls();C.login(D,N);C.sendmail(D,B,K)
	A.debug(f"Verification code {F} sent to {B}.")
async def P(ctx):
	P='Verification timed out. Please try again.';O='message';A=ctx;await A.send('Please enter your email address to receive a verification code.')
	def S(message):B=message;return B.author==A.author and E in B.content and J(B.channel,C.TextChannel)
	try:K=await B.wait_for(O,timeout=12e1,check=S)
	except H.TimeoutError:await A.send(P);return
	D=K.content.strip()
	if D.split(E)[-1]not in I:await A.send(f"Error: {D} is not a valid email address for verification.Please use @pausd.us instead, or contact an admin.");return
	L=Q();M=await R(D,L)
	if M is not None:await A.send(M);return
	await A.send(f"Please enter the verification code sent to {D}.")
	def T(message):B=message;return B.author==A.author and B.content==L and J(B.channel,C.TextChannel)
	try:K=await B.wait_for(O,timeout=12e1,check=T)
	except H.TimeoutError:await A.send(P);return
	F=A.guild;N=F.get_member(A.author.id);G=C.utils.get(F.roles,name='Verified');await N.add_roles(G);G=C.utils.get(F.roles,name='Member');await N.add_roles(G);await A.send('You have been verified!')
@B.event
async def S():A.info('Bot is ready.')
@B.event
async def T(member):A=member;await A.send(f"Welcome to the server, {A.mention}! Please verify yourself by using the `~verify` command.")
@B.command()
async def verify(ctx):await P(ctx)
B.run(M)
