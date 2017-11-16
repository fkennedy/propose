from django.db import models

from account.models import Client, Freelancer
from project.models import Project

# Create your models here.
class WorkApplication(models.Model):
	creator = models.ForeignKey(
		Freelancer,
		blank = False)

	project = models.ForeignKey(
		Project,
		blank = False)

	client = models.ForeignKey(
		Client,
		blank = False)

	timestamp = models.DateTimeField(
		auto_now_add = True,
		editable = False,
		null = False,
		blank = False)

	is_accepted = models.BooleanField(
		default = False,
		blank = False)

	is_expired = models.BooleanField(
		default = False,
		blank = False)

	def __str__(self):
		return "{0}'s application to {1} for project {2}".format(self.creator, self.client, self.project)

class WorkOffer(models.Model):
	creator =  models.ForeignKey(
		Client,
		blank = False)

	project = models.ForeignKey(
		Project,
		blank = False)

	freelancer = models.ForeignKey(
		Freelancer,
		blank = False)

	timestamp = models.DateTimeField(
		auto_now_add = True,
		editable = False,
		null = False,
		blank = False)

	is_accepted = models.BooleanField(
		default = False,
		blank = False)

	is_expired = models.BooleanField(
		default = False,
		blank = False)

	def __str__(self):
		return "{0}'s offer to {1} for project {2}".format(self.creator, self.freelancer, self.project)
