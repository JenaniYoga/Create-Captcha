from captcha.image import ImageCaptcha

k=ImageCaptcha()

image=k.generate('1119')
k.write('1119','Captcha_sample.png')