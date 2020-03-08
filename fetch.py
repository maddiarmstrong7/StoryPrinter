import urllib.request
import lxml as lh


#pulls URL, length 1 only, length 2 broken (look into later)
url = "http://readpoopfiction.com/story.php?length=1"
#open url
page = urllib.request.urlopen(url)
#read page
doc = str(page.read())
#format author section
index = doc.find("<p class=\"author\">")
doc = doc[index:-1]
index = doc.find("<p>")
doc = doc[index+3:-1]
end = doc.find("<p class=\"more\">")
#paragraph settings
print(doc[:end].replace("<br />", "\n").replace("</p>", "").replace("\\t", "").replace("\\n","").replace("\\r", "").replace("<p>", "\n").replace("&nbsp;"," ").replace("&ldquo;","\"").replace("&rdquo;", "\""))
