from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField("Жанры", max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"



class Theme(models.Model):
    name = models.CharField("Название", max_length=50)
    def __str__(self) -> str:
        return self.name



class Category(models.Model):
    name = models.CharField("Категории", max_length=159)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"




class Movies(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="posters/")
    year = models.PositiveSmallIntegerField("Год выпуска", default=1980)
    genres = models.ManyToManyField(Genre, verbose_name='жанры')
    themes = models.ManyToManyField(Theme, verbose_name='темы')
    category = models.ForeignKey(Category, verbose_name="Категории", on_delete=models.SET_NULL, null=True)
    original_title = models.CharField("Название на японском", max_length=100)
    age_permissions = models.PositiveIntegerField("Возрастной рейтинг",  default=12)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Аниме"
        verbose_name_plural = "Анимы"

class PostImage(models.Model):
    image = models.ImageField(upload_to='shots', blank=True, null= True)
    post = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='images')