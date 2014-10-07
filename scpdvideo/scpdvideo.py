from re import match

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope
from xblock.fields import String
from xblock.fragment import Fragment


class SCPDVideo(XBlock):
    name = String(
        default="SCPD Video",
        scope=Scope.settings,
        help='TODO',
    )
    videoUrl = String(
        default="https://mvideos.stanford.edu/Viewer/Video/PlayVideo/?assetId=64819bff-bf15-49b9-96c5-5a09f9997b9c",
        scope=Scope.settings,
        help='TODO',
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def resource_url(self, path):
        url = path or ''
        if not match(r'^(([a-z]+:\/)?\/)', url):
            url = self.runtime.local_resource_url(self, url)
        return url

    def student_view(self, context=None):
        html = self.resource_string("private/html/view.html")
        frag = Fragment(html.format(
            name=self.name,
            videoUrl=self.videoUrl,
        ))
        frag.add_css_url(self.resource_url("public/view.less.min.css"))
        frag.add_javascript_url(self.resource_url("public/view.js.min.js"))
        frag.initialize_js('SCPDVideoView')
        return frag

    def studio_view(self, context=None):
        html = self.resource_string("private/html/edit.html")
        frag = Fragment(html.format(
            name=self.name,
            videoUrl=self.videoUrl,
        ))
        frag.add_javascript_url(self.resource_url("public/edit.js.min.js"))
        frag.initialize_js('SCPDVideoEdit')
        return frag

    @XBlock.json_handler
    def studio_view_post(self, data, suffix=''):
        self.name = data['xblock_scpdvideo_name']
        self.videoUrl = data['xblock_scpdvideo_video_url']
        return {
            'xblock_scpdvideo_name': self.name,
            'xblock_scpdvideo_video_url': self.videoUrl,
        }

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("SCPDVideo",
             """<vertical_demo>
                    <scpdvideo name="My First XBlock" videoUrl="https://mvideos.stanford.edu/Viewer/Video/PlayVideo/?assetId=64819bff-bf15-49b9-96c5-5a09f9997b9c" />
                </vertical_demo>
             """),
        ]
