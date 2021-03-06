from django.db import models


class Movie(models.Model):
    """
    Represents a movie
    """
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    year = models.IntegerField()
    length = models.IntegerField()
    description = models.TextField()
    # poster = models.ImageField(upload_to='movie_posters/')

    def __str__(self):
        return self.name


class Cinema(models.Model):
    """
    Represents a cinema saloon
    """
    cinema_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=30, default='Tehran')
    capacity = models.IntegerField()
    phone = models.CharField(max_length=20, null=True)
    address = models.TextField()

    def __str__(self):
        return self.name


class ShowTime(models.Model):
    """
    Represents a movie show in a cinema at a specific time
    """
    movie = models.ForeignKey('Movie', on_delete=models.PROTECT)
    cinema = models.ForeignKey('Cinema', on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    price = models.IntegerField()
    salable_seats = models.IntegerField()
    free_seats = models.IntegerField()

    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKET_SOLD = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6
    status_choices = (
        (SALE_NOT_STARTED, "sale is not started"),
        (SALE_OPEN, "on selling tickets"),
        (TICKET_SOLD, "all tickets are sold"),
        (MOVIE_PLAYED, "movie played"),
        (SHOW_CANCELED, "show has been canceled")
    )
    status = models.IntegerField(choices=status_choices, default=SALE_NOT_STARTED)

    def __str__(self):
        return ' {} - {} - {}'.format(self.movie, self.cinema, self.start_time)


