import os
import pprint

from app import Blogpost, db


def main():
    directories = []
    image_files = []

    db.drop_all()
    db.create_all()

    for root, dirs, files in os.walk("static/"):
        if ".DS_Store" in files:
            files.remove(".DS_Store")
        image_files.append(files)
        directories.append(dirs)

    myd = list(zip(directories[0], image_files[1:]))

    for item in myd:
        title = item[0]
        src = str("../static/{}/".format(title)) + str(item[1][0])
        subimages = f",../static/{title}/".join([i for i in item[1][1:]])
        post = Blogpost(title=title, image=src, subimages=subimages)
        db.session.add(post)
    db.session.commit()


if __name__ == "__main__":
    main()
