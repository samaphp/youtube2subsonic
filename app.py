import web
import commands

# write the music folder that you need to save mp3 file, subsonic media folder as example
music_folder = "/home/" # Insert your music folder full path here

urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('./')

class Index(object):
    def GET(self):
        return render.insert_url()

    def POST(self):
        form = web.input(url="")
        cmd = "./youtube-dl-mp3 %s %s" % (form.url, music_folder)
        print commands.getstatusoutput(cmd)
        return render.result(url = form.url)

if __name__ == "__main__":
    app.run()