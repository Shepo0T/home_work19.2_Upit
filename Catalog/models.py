from django.db import models



from users.models import NULLABLE, User


class Task(models.Model):
    title = models.CharField("Название", max_length=50)
    task = models.TextField("Описание")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.CharField(max_length=100, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.CharField(max_length=200, verbose_name="Описание")
    views_count = models.IntegerField(default=0, verbose_name="просмотры")
    preview = models.ImageField(
        upload_to="products/foto",
        blank=True,
        null=True,
        verbose_name="Изображение(превью)",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
    )
    purchase_price = models.FloatField(
        verbose_name="Цена за покупку",
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания(записи в БД)",
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Дата последнего изменения(записи в БД)",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Продается'
    )
    owner = models.ForeignKey(User, verbose_name='Создатель', help_text='Укажите создателя продукта',on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "purchase_price", "category", "created_at", "is_active", "owner"]
        permissions = [
            ('can_edit_description', 'Может менять описание Продукта'),
            ('can_edit_category','Может менять категорию любого продукта'),
            ('can_edit_toggle', 'Может отменять публикацию продукта')
        ]

class Version(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_versions"
    )
    version_number = models.IntegerField(default=1, verbose_name="Номер версии")
    name_version = models.CharField(max_length=20, verbose_name="Имя версии")
    current_version = models.BooleanField(
        default=True, verbose_name="Признак текущей версии"
    )
    def __str__(self):
        return f'{self.name_version} {self.version_number}'
    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продуктов"
        ordering = ['product', 'version_number', 'name_version', 'current_version']