from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *

class GameForm(ModelForm):
	class Meta:
		model = Tier 
		fields = '__all__'
		#fields =['game','tierlist','played','won']


class MemberForm(ModelForm):
	#college = models.CharField(max_length=200, null=True)
	class Meta:
		model = Member
		fields = ['name','email','college','phone']

		def save(self, request):
			# college = request.user.first_name
			# print(college)
			user = Member.create(name=self.cleaned_data['name'],
								email = self.cleaned_data['email'],
								college = self.cleaned_data['college'],
								phone=self.cleaned_data['phone'],
								)


class CreateUserForm(UserCreationForm):
	
	class Meta:
		model = User 
		fields = ['username' ,'password1', 'password2']


class UserUpdateForm(ModelForm):
	class Meta:
		model = User 
		fields = ['username', 'email']


class ProfileUpdateForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['phone', 'college', 'adhaar','image']


class TournamentForm(ModelForm):
	class Meta:
		model = Tournament
		fields = ['name', 'game']


class TeamForm(ModelForm):
	class Meta:
		model = Team
		fields = ['name', 'game']

class TeamMemberForm(ModelForm):
	class Meta:
		model = TeamMembers
		fields = ['member','team']
			
