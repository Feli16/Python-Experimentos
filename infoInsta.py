from instagramy import InstagramUser

name = input("Meta su Username: ")

user = InstagramUser(name)

bio =  user.biography

print('Bio:\n', bio)

link_in_bio = user.website

print('Link in Bio:', link_in_bio)

