import instaloader

ig = instaloader.Instaloader()
dp = input("Agregue el usuario de Instagram: ")

ig.download_profile(dp, profile_pic_only = True) 