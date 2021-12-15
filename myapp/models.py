from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw
from django.contrib.auth.models import User

class YourModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.TextField()
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)
    color  = models.CharField(max_length=255,null=True, blank=True)

    
    def save(self, *args, **kwargs):
        qr_code_img = qrcode.QRCode()
        qr_code_img.add_data(self.url)
        canvas = qr_code_img.make_image(fill_color=self.color)
        fname = f"qr_code-{self.title}"+".png"
        buffer = BytesIO()
        canvas.save(buffer,"PNG")
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args,**kwargs)
