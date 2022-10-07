__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# part 1

from importlib.resources import contents


def clean_cache():
    import os
    import glob

    cache = r"C:\Users\LilAlex\Documents\wincprojects\files\cache"
        
    if not os.path.exists(cache):    
        os.mkdir(cache)
        return "New cache created!"
    elif os.path.exists(cache):
        cache = glob.glob(r"C:\Users\LilAlex\Documents\wincprojects\files\cache\*")
        for files in cache:
            os.remove(files)
        return "The existing cache was cleaned!"

print(clean_cache())
    
#part 2

def cache_zip(file_path, cache_path):
    import zipfile

    zip = zipfile.ZipFile(file_path)
    zip.extractall(cache_path)
    return "Unzipped file to cache"

print(cache_zip(r"C:\Users\LilAlex\Documents\wincprojects\files\data.zip", r"C:\Users\LilAlex\Documents\wincprojects\files\cache"))

# part 3

def cached_files():
    import os
    
    cache = r"C:\Users\LilAlex\Documents\wincprojects\files\cache"
    onlyfiles = [os.path.join(cache, f) for f in os.listdir(cache) if 
    os.path.isfile(os.path.join(cache, f))]
    return onlyfiles

# print (cached_files())

# part 4

def find_password(cached_files):
    for file in cached_files:

        f_contents = open(file, 'r')
        contents = f_contents.read()
        f_contents.close()
        if "pass" in contents:
            password_location = contents.find("password")
            start = contents.find(" ", password_location) +1
            end = contents.find("\n", password_location) 
            return contents[start:end]


print(find_password(cached_files()))