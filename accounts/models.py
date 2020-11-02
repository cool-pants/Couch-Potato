from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	college = models.CharField(max_length=200, null=True, unique = True)
	phone = models.CharField(max_length=200, null=True, unique = True)
	adhaar = models.CharField(max_length=200, null=True, unique = True)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	is_apply = models.BooleanField(default=False)
	is_lead = models.BooleanField(default=False)


	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

class Game(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Team(models.Model):
	name = models.CharField(max_length=200, null=True)
	game = models.ForeignKey(Game, null=True, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name

class University(models.Model):
	college = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.college

class Member(models.Model):

	name = models.CharField(max_length=200, null=True, unique = True)
	#college = models.ForeignKey(University, null=True, on_delete=models.CASCADE)
	college = models.CharField(max_length=200, null=True)
	email = models.EmailField(max_length=255, null=True,unique=True)
	phone = models.CharField(max_length=200, null=True, unique = True)
	team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)

	date_created = models.DateTimeField(auto_now_add=True, null=True)

	@classmethod
	def create(self, name, email=None, college=None, phone=None, team=None):
		member=self(name=name, email=email, college=college,phone=phone, team=team)
		return member

	def __str__(self):
		return self.name

# class UserMember(models.Model):

# 	name = models.CharField(max_length=200, null=True)
# 	college = models.ForeignKey(University, null=True, on_delete=models.CASCADE)
# 	phone = models.CharField(max_length=200, null=True)

# 	date_created = models.DateTimeField(auto_now_add=True, null=True)

# 	def __str__(self):
# 		return self.name

class Tier(models.Model):
	TIER = (
		('Tier 1', 'Tier 1'),
		('Tier 2', 'Tier 2'),
		('Tier 3', 'Tier 3'),
		)
	member = models.ForeignKey(Member, null=True, on_delete=models.CASCADE)
	game = models.ForeignKey(Game, null=True, on_delete=models.CASCADE)
	tierlist = models.CharField(max_length=200, null=True, choices=TIER)
	played = models.IntegerField(default=0)
	won = models.IntegerField(default=0, null=True)

	@classmethod
	def create(cls, member):
		tier = cls(member=member)
		return tier



class Tournament(models.Model):
	name = models.CharField(max_length=200, null=True)
	game = models.ForeignKey(Game, null=True, on_delete=models.CASCADE)

	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class TeamMembers(models.Model):
	team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
	member = models.ForeignKey(Member, null=True, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name

