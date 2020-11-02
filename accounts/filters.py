import django_filters
from django_filters import DateFilter

from .models import *

class TierFilter(django_filters.FilterSet):
	#start_date = DateFilter(fieldname = "date_created", lookup='gte')
	#end_date = DateFilter(fieldname = "date_created", lookup='lte')
	class Meta:
		model = Tier;
		fields = ['tierlist']
			