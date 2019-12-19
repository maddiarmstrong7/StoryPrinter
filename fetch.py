import urllib.request
import lxml as lh


url = "http://readpoopfiction.com/story.php?length=1"
page = urllib.request.urlopen(url)
doc = str(page.read())
index = doc.find("<p class=\"author\">")
doc = doc[index:-1]
index = doc.find("<p>")
doc = doc[index+3:-1]
end = doc.find("<p class=\"more\">")
print(doc[:end].replace("<br />", "\n").replace("</p>", "").replace("\\t", "").replace("\\n","").replace("\\r", "").replace("<p>", "\n").replace("&nbsp;"," ").replace("&ldquo;","\"").replace("&rdquo;", "\""))