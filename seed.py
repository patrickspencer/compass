from compass.models import Assignment

ass = Assignment.objects.create(name='New Assignment',
        start_date='now',
        end_date='later')

ass.save()
