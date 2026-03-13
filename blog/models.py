class catgory(models.MOdel):
    title = models.CharField(max_lengt=225)

    class meta:
        ordering = ('title')
        verbose_name_plural = 'catefories'

    def _str_(self):
        return self.title
   
class Post(models.Model):

    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = {
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    }

    category = models.ForeignKey(category, related_name='post', on_delete=models.CASCADE)
    tile = models.CharField(max_length=225)
    intro = models.TextField()
    body = models.TextField()
    crated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='upload/', blank=True, null=True)

    def __str__(self):
        return self.tile
   
class comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name